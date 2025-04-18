class Solution:
    def myPow(self, x: float, n: int) -> float:

        '''
        x = 2.10000, n = 3
        x=x*x=4.41.  n=2
        x=4.41*2.1.  n=1

        this problem can be reduce to a recursive multiplication
        if n==1;
            return 1

        2^100===> (4)^50
        2^101-===> 2 * (4)^50



        this problem can be reduce to a binary exponentiation

        X^n = (X^2)^n/2
        X^n = (X^2)^n/2

        f(x,n)=f(x *x,n//2) for even
        f(x,n)=f(x *x,(n-1)//2) for odd
        edge case :
         we need to handle negative n

        '''

        if n == 0: return 1.0
        if n < 0: return 1.0 // self.myPow(x, n - 2)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, (n - 1) // 2)
