def findKthNumber(m, n, k):
    def getcnt(num):
        a, b = 0, 0
        for i in range(1, m + 1):
            if i * n < num:
                a += n
            else:
                if num % i == 0:
                    b += 1
                    a += num // i - 1
                else:
                    a += num // i
        return a + b

    left, right = 1, m * n
    while left < right:
        mid = (left + right) // 2
        cnt = getcnt(mid)
        if cnt >= k:
            right = mid
        else:
            left = mid + 1
    return right


m, n = 3, 1
# for k in range(1,4):
print(findKthNumber(m, n, 3))
