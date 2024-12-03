import random
import sympy

   # Q1
def monte(n, k):
    num_of_exp = 0
    for i in range(k):
        seen_coupons = []
        while (len(seen_coupons) != n):
            coupon = random.randint(1, n)
            if (coupon not in seen_coupons):
                seen_coupons.append(coupon)
            num_of_exp += 1
    return (num_of_exp / k)

   # Q2
print(monte(10, 10))
print(monte(10, 100))
print(monte(10, 1000))

   # Q3
s = sympy.symbols('s')
def moment_generating_func(n):
    MGFs = []
    for i in range(1, n + 1):
        Pi = 1 - ((i - 1) / n)
        MGF = (Pi * sympy.exp(s)) / (1 - ((1 - Pi) * sympy.exp(s)))
        MGFs.append(MGF)
    return MGFs
MGF_Xi = moment_generating_func(10)   #MGF[i] is equal to MGF for Xi

   # Q4
MGF_X = 1
for mgf in MGF_Xi:
    MGF_X *= mgf

   # Q5
MGF_diff = sympy.diff(MGF_X, s)
Exp_X = MGF_diff.subs({s:0})
print(Exp_X)