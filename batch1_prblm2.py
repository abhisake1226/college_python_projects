#write a Python program to print all non-fibonacci, non-prime numbers within range a-b, where a and b are accepted as command line arguments
import sys
def is_prime(num):
    if num<2:
        return False
    for i in range (2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def generate_fibo(limit):
    fibo_set = {0,1}
    a,b = 0,1
    while(b<=limit):
        a,b=b,a+b
        fibo_set.add(b)
    return fibo_set

def non_prime_non_fibo(a,b):
    fibo_set = generate_fibo(b)
    print(fibo_set)
    for num in range(a,b+1):
        if not is_prime(num) and num not in fibo_set:
            print(num)


if __name__ =="__main__":
    if len(sys.argv)!=3:
        print("Usage: python script.py a b ")
    else:
        try:
            a=int(sys.argv[1])
            b=int(sys.argv[2])
            non_prime_non_fibo(a,b)

        except ValueError:
            print("error: Both arguments must be integers!")
