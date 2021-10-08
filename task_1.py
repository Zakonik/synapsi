def find_reverse(n):
    rev = 0
    neg = False
    if n < 0:
        n = -n
        neg = True
    while n > 0:
        rev = rev * 10 + n % 10
        n = int(n / 10)
    if neg:
        rev = -rev
    if rev > 2147483647 or rev < -2147483648:
        return 0
    return rev


if __name__ == '__main__':
    print(find_reverse(192))
    print(find_reverse(-192))
    print(find_reverse(2147483647))
    print(find_reverse(-2147483648))
    print(find_reverse(-1000000012))
    print(find_reverse(1000000012))
    print(find_reverse(512))
    print(find_reverse(-954))
