import sys

def insertionSort(arr, key, j): 
    while j >=0 and key < arr[j]: 
        arr[j+1] = arr[j] 
        j -= 1

    arr[j+1] = key 


def run_sorting(arr):
    [insertionSort(arr=arr, key=arr[x], j=x-1) for x in range(1, len(arr))]


data = []

arr = input()
arr = [arr[i] for i in range(len(arr))]
run_sorting(arr)
arr.reverse()
print("".join(arr))
