from math import factorial

def newtonbinom(n):
  k = 0
  res = ""
  for i in range(0, n+1):
    binomcalc = int(factorial(n)/(factorial(k)*factorial(n-k)))
    if binomcalc != 1:
      res += f"{binomcalc}*"
    a_str = ""
    if n-k == 1:
      a_str = "a"
    elif n-k > 1:
      a_str = f"a^{n-k}"
    b_str = ""
    if k == 1:
      b_str = "b"
    elif k > 1:
      b_str = f"b^{k}"
    if n-k != 0 and k != 0:
      a_str += "*"
    res += a_str + b_str + " + "
    k+=1
    
  return res[:-2]
