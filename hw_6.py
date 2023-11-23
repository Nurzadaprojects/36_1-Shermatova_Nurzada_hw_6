def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def binary_search(element, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    
    
    sorted_list = bubble_sort(unsorted_list[:]) 
    
    
    print("Отсортированный список:", sorted_list)
    
    
    element_to_find = 22
    index = binary_search(element_to_find, sorted_list)
    if index != -1:
        print(f"Элемент {element_to_find} найден по индексу {index}.")
    else:
        print(f"Элемент {element_to_find} не найден в списке.")
