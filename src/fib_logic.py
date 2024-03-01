def fib(n):
  if not isinstance(n, int) or n < 0:
    raise ValueError("nは非負の整数でなければなりません")
  elif n == 0:
      return 0
  elif n == 1:
      return 1
  else:
      a, b = 0, 1
      for _ in range(2, n + 1):
          a, b = b, a + b
      return b