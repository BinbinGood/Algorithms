def CountSort(arr):
    if len(arr) < 2:
        return
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    help = [0] * (max + 1)
    # print(len(help))
    for i in range(len(arr)):
        help[arr[i]] += 1
    i = 0
    for j in range(len(help)):
        while (help[j] > 0):
            help[j] -= 1
            arr[i] = j
            i += 1
        j += 1


if __name__ == "__main__":
    array = [1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 2, 5, 6, 8, 8, 9, 9]
    print(array)
    CountSort(array)
    print(array)
