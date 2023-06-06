import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"Iterasi {i}: {arr}")
    
    return arr

# Contoh penggunaan
array = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum diurutkan:", array)
start_time = time.time()
sorted_array = insertion_sort(array)
end_time = time.time()
print("Array setelah diurutkan:", sorted_array)
print("Waktu eksekusi:", end_time - start_time, "detik")
