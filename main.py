def is_prime(n):
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

def is_perfect_number(n):
    pass

if __name__ == "__main__":
    n = 0
    n = int(input("nhap n: "))
    print("n =",n)
    print("-------------")
    print(is_prime(n))
    #print(is_perfect_number(n))