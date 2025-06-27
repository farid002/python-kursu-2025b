fib_list=[0,1]
user_lim=int(input("Fibonacci ardıcıllığı ilə yazmaq üçün 10 ilə 200 arasında rəqəm daxil eləyin"))
if 10< user_lim <200:
    i=0
    while user_lim>fib_list[-1]:
        fib_list.append(fib_list[i]+fib_list[i+1])
        i+=1
    print(f"Verdiyiniz edede qeder fibonacci ardicilliqi {fib_list[0:-1]}")
else:
    print("Duzgun eded yazin!")