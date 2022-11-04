#User function Template for python3
import math
class Solution:
	def baseEquiv(self, n, m):
		# code here
        if n == 0:
          return "No"
        for i in range(2,32+1):
          val = (int)(math.log(n,i))
          if val+1 == m:
            return "Yes"
        return "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n=int(n)
		m=int(m)
		ob = Solution();
		print(ob.baseEquiv(n,m))

# } Driver Code Ends----
