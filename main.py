def bubble_sort(array):
    ''' Пузырьковая сортировка'''
    for j in range(len(array)-1):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array

def selection_sort(array):
    '''Сортировка выбором'''
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        return array


def insertion_sort(array):
    ''' Сортировка вставками'''
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def quick_sort (array):
    ''' Быстрая сортировка'''
    if len(array) <=1:
        return array
    element = array[0]
    left = list(filter(lambda i: i<element, array))
    center = [i for i in array if i==element]
    right = list(filter(lambda i: i > element, array))
    return quick_sort(left) + center + quick_sort(right)




print('Исходный массив: ')
mas = [5, 8, 7, 10, 4, 14, 3, 23, 8, 18,2, 99, 1]
print(mas)
print('Пузырьковая сортировка:')
print(bubble_sort(mas))
print('Быстрая сортировка:')
print(quick_sort(mas))
print('Сортировка выбором:')
print(selection_sort(mas))
print('Сортировка вcтавками:')
print(insertion_sort(mas))