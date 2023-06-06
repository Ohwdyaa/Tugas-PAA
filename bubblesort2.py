import time

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        print(f"Iterasi {i + 1}: {arr}")
        
        if not swapped:
            break
    
    return arr

# Contoh penggunaan
array = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum diurutkan:", array)
start_time = time.time()
sorted_array = bubble_sort(array)
end_time = time.time()
print("Array setelah diurutkan:", sorted_array)
print("Waktu eksekusi:", end_time - start_time, "detik")
