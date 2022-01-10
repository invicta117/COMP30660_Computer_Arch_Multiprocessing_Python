import math
import multiprocessing
import time
def my_func(x):  
    s = math.sqrt(x)  
    return s


def my_func_verbose(x):
    s = math.sqrt(x)
    print("Task", multiprocessing.current_process(), x, s)
    return s

def check_prime(num):

    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:", int(time.time()-t1))
                break
        else:
            print(num,"is a prime number")
            print("Time:", time.time()-t1) 
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    print("Task", multiprocessing.current_process(), num, res)
    return res

def calc_factorial(num):
    t1 = time.time()
    total = 1
    for i in range(2, num+1):
        total *= i
    print("Time:", time.time()-t1) 
    print("Task", multiprocessing.current_process(), num)
    return total