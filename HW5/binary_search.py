# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.

# Двоичный (бинарный) поиск (также известен как метод деления пополам или 
# дихотомия) — классический алгоритм поиска элемента в отсортированном 
# массиве (векторе), использующий дробление массива на половины. 
# Используется в информатике, вычислительной математике и математическом 
# программировании.

#Здесь используется парадигма структурного программировани (линейная последовательность
# действий, цикл, структурные блоки).

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Искомый элемент найден, возвращаем его индекс
        elif arr[mid] < target:
            left = mid + 1  # Искомый элемент находится в правой половине
        else:
            right = mid - 1  # Искомый элемент находится в левой половине

    return -1  # Элемент не найден

# Исходный массив
arr = [1, 3, 5, 7, 9, 11, 13, 15]

# Запрашиваем искомое число у пользователя
try:
    target = int(input("Введите искомое число: "))
except ValueError:
    print("Ошибка: Введите целое число.")
    exit(1)

result = binary_search(arr, target)

if result != -1:
    print(f"Искомый элемент {target} найден в массиве по индексу {result}.")
else:
    print(f"Искомый элемент {target} не найден в массиве.")


# binary_search с использованием функциональной парадигмы

def binary_search1(arr, target):
    left1, right1 = 0, len(arr) - 1
    def binary_search_recursive(arr, target, left, right):
        if left1 > right1:
            return -1   

    mid = (left1 + right1) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right1)
    else:
        return binary_search_recursive(arr, target, left1, mid - 1)

arr = [1, 3, 5, 7, 9, 11, 13, 15]

try:
    target1 = int(input("Введите искомое число: "))
except ValueError:
    print("Ошибка: Введите целое число.")
    exit(1)

result1 = binary_search1(arr, target1)

if result1 != -1:
    print(f"Искомый элемент {target1} найден в массиве по индексу {result1}.")
else:
    print(f"Искомый элемент {target1} не найден в массиве.")


