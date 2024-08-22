class Solution:
    def fib(self, n: int) -> int:
        
        memo = [None] * (n + 1)

        def fib_memo(n, mem):
            if mem[n] is not None:
                return mem[n]
            if n < 2:
                mem[n] = n
                return n
            mem[n] = fib_memo(n - 1, mem) + fib_memo(n - 2, mem)
            return mem[n]

        return fib_memo(n, memo)
