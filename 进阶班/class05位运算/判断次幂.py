# 取该数最右侧的1，然后判断是否和原数相等即可
# 因为，2的幂，在二进制中，只有一个1
def is2Power(num):
    if num == 0:
        return False
    rightone = num & (~num + 1)
    return rightone == num

# 4的幂的前提是必须是2的幂，即二进制中只有一个一。
# 然后判断这个一的位置，只能在0101 0101 0101 0101这些位上，与上原数不等于0就表示是4的幂
# 0x:表示16进制
def is4Power(num):
    return is2Power(num) and (num & 0x55555555 != 0)


if __name__ == "__main__":
    print(is2Power(1))
    print(is4Power(1))
