#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        i,j=0,0
        n=len(arr)
        count,maxCount=0,0
        while i<n:
            if arr[i]<=dep[j]:
                count+=1
                i+=1
            else :
                count-=1
                j+=1
            maxCount=max(count,maxCount)
        return maxCount
        
        #Brute force solution
        # plat_needed = 1
        # result = 1
        # n=len(arr)
        # # run a nested loop to find overlap
        # for i in range(n):
        #     # minimum platform needed
        #     plat_needed = 1
    
        #     for j in range(n):
        #         # check for overlap
        #         if i != j:
        #             if (arr[i] >= arr[j] and dep[j] >= arr[i]):
        #                 plat_needed += 1
    
        #     # update result
        #     result = max(result, plat_needed)

        # return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends