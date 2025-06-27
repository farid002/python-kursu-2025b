"""
FIBONACCI

Istifadəçidən 10 - 200 arasında bir tam ədəd alın və bu ədədə qədər olan fibonacci ədədlər ardıcıllığını çap edin.
Ədəd doğru olmazsa, doğru olana qədər proqram ədədi istifadəçidən istəsin.

Bilgi: Fibonacci elə ədədlər ardıcıllığıdır ki, hər ədəd öncəki iki ədədin cəminə bərabərdir.
Məsələn: 0,1,1,2,3,5,8,13,21,34...
"""

number = int(input("Enter number between 10-200:"))
fibonacci = [0, 1]
while True:

    sum_list=fibonacci[-1]+fibonacci[-2]

    fibonacci.append(sum_list)
    if sum_list>number:
        break
fibonacci.pop()
print(fibonacci)



