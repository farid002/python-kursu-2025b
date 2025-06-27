"""
FIBONACCI

Istifadəçidən 10 - 200 arasında bir tam ədəd alın və bu ədədə qədər olan fibonacci ədədlər ardıcıllığını çap edin.
Ədəd doğru olmazsa, doğru olana qədər proqram ədədi istifadəçidən istəsin.

Bilgi: Fibonacci elə ədədlər ardıcıllığıdır ki, hər ədəd öncəki iki ədədin cəminə bərabərdir.
Məsələn: 0,1,1,2,3,5,8,13,21,34...
"""
while True:
    reqem=int(input("reqem yazin"))
    if 10 > reqem or reqem > 200:
        break

fibonacci = [0, 1]

while True:
    cem = fibonacci[-1] + fibonacci[-2]
    if cem > reqem:
      break
    fibonacci.append(cem)
print(fibonacci)


