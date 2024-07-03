def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True
        


def primeNumbers(begin, end):
    plist = []
    for i in range(begin, end + 1):
        if isPrime(i):
            plist.append(i)

    return plist


def main():
    begin = 0
    end = 20
    rlst = primeNumbers(begin, end)
    print(rlst)

    begin = 10
    end = 50
    rlst = primeNumbers(begin, end)
    print(rlst)


if __name__ == '__main__':
    main()
