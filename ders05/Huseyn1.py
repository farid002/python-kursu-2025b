"""
FIBONACCI

Istifadəçidən 10 - 200 arasında bir tam ədəd alın və bu ədədə qədər olan fibonacci ədədlər ardıcıllığını çap edin.
Ədəd doğru olmazsa, doğru olana qədər proqram ədədi istifadəçidən istəsin.

Bilgi: Fibonacci elə ədədlər ardıcıllığıdır ki, hər ədəd öncəki iki ədədin cəminə bərabərdir.
Məsələn: 0,1,1,2,3,5,8,13,21,34...
"""

fib_list = [0,1]
number = int(input("Bir eded yazin"))

while True:
    yeni_eded = fib_list[-1] + fib_list[-2]
    fib_list.append(yeni_eded)

    if number < yeni_eded:
        break

print(fib_list)
