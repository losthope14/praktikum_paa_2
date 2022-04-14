import time
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = []
l = int(input("Masukkan panjang array : "))
for i in range(l):
    k = int(input("Nilai array : "))
    arr.append(k)
print("Array : ", arr)

times = time.time()
bubbleSort(arr)
print("\nSorted array is : ")
for i in range(len(arr)):
    print("%d" % arr[i])
    print("%s Second" % (time.time() - times))

