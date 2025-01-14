#User function Template for python3

class Solution:
    def medianOf2(self, a, b):
        #code here
        #Expected TC : O(log(min(a,b))) ,SC: O(1)
        n1, n2 = len(a), len(b)
        # if n1 is bigger swap the arrays:
        if n1 > n2:
            return self.medianOf2(b, a)
    
        n = n1 + n2  # total length
        left = (n1 + n2 + 1) // 2  # length of left half
        # apply binary search:
        low, high = 0, n1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            # calculate l1, l2, r1, and r2;
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            if mid1 - 1 >= 0:
                l1 = a[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = b[mid2 - 1]
    
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0
    
            # eliminate the halves:
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0  # dummy statement
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        ob = Solution()

        if len(arr2) == 1 and arr2[0] == 0:
            arr2 = []
        ans = ob.medianOf2(arr1, arr2)
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)
        print("~")

# } Driver Code Ends