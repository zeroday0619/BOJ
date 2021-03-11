import sys

def insertionSort(arr, key, j): 
    while j >=0 and key < arr[j]: 
        arr[j+1] = arr[j] 
        j -= 1

    arr[j+1] = key 


def run_sorting(arr):
    [insertionSort(arr=arr, key=arr[x], j=x-1) for x in range(1, len(arr))]


data = []

firt_input = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) + (i - i) for i in range(firt_input)]

arr = data

run_sorting(arr)
[print(arr[i]) for i in range(len(arr))]