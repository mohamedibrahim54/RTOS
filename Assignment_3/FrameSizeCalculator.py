'''
calculate the largest possible frame size for the cyclic structured scheduler.
it also calculate HyperPeriod of Task set.
change the Period(p) values of Tasks and Change the Deadline(d) values.
this program written for Task set consist of 3 and 4 Tasks.
by: Mohamed Ibrahim Elsawy.
    moibra95@outlook.com

'''

def lcm(a,b):
 '''
 The Least Common Multiple:
 return LCM is the smallest positive integer that is evenly divisible by both a and b
 '''
 r = 0
 if a % b == 0:
     return a;
 if b % a == 0:
     return b;    
 while True:
     r = r + a;
     if r % b == 0:
         return r
       
       

def dividors(x):
 '''
 return all numbers which divide x evenly
 '''
 n = 0;
 result = []
 for n in range(1, x + 1):
  if x % n == 0:
   result.append(n)
 
 return result

def gcd(a, b):
 '''
 return Greatest common divisor of number a and b
 '''
 n = min(a, b)
 while n > 0:
  if a % n == 0 and b % n == 0:
   return n
  n-=1
  

'''
change the Period(p) values of Tasks and Change the Deadline(d) values.
this program written for Task set consist of 3 and 4 Tasks.
'''
p1 = 5
p2 = 7
p3 = 12
# Un Comment the following line for Task 4
p4 = 45

d1 = 5
d2 = 7
d3 = 12
# Un Comment the following line for Task 4
d4 = 45

H = lcm(lcm(p1,p2), p3)
# Un Comment the following line for Task 4
H = lcm(H, p4)
print("HyperPeriod = ", H)
divs = dividors(H)
#print("dividors: ", divs)
largePeriod = max(p1, max(p2, p3))
# Un Comment the following line for Task 4
largePeriod = max(largePeriod, p4)
largePeriodIndex = divs.index(largePeriod)
candidates = divs[:largePeriodIndex + 1]
candidates.reverse()
print("candidates: ", candidates)
for f in candidates:
 y1 = 2 * f - gcd(p1, f)
 if y1 <= d1:
  y2 = 2 * f - gcd(p2, f)
  if y2 <= d2:
   y3 = 2 * f - gcd(p3, f)
   if y3 <= d3:
    # Un Comment the following two line for Task 4
    y4 = 2 * f - gcd(p4, f)
    if y4 <= d4:    
     print("vaild frame size: " ,f)



