
#ordenar

def bubbleSort(nums):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                #intercambiamos los numeros
                nums[i] , nums[i+1] = nums[i+1], nums[i]
                #cambiamos a True la variable ya que ha habido un intercambio
                intercambio = True

listanumeros = [5,2,1,8,4]
bubbleSort(listanumeros)
print(listanumeros)

listanumeros1 = [9,1,45,25,813,51,1,0]
bubbleSort(listanumeros1)
print(listanumeros1)

def selectionSort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1 , len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

listanumeros2 = [9,1,45,25,813,51,11,0]
selectionSort(listanumeros2)
print(listanumeros2)

def insertionSort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i -1
        while j>=0 and nums[j] > item_to_insert:
            nums[j+1] = nums[j]
            j = j -1
        nums[j+1] = item_to_insert

listanumeros3 = [9,1,45,25,813,51,11,0]
insertionSort(listanumeros3)
print(listanumeros3)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length , right_list_length = len(left_list) ,len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index = left_list_index + 1
            else:
                sorted_list.append((right_list[right_list_index]))
                right_list_index = right_list_index +1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index = right_list_index +1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index = left_list_index +1
    return sorted_list

def mergeSort(nums):
    if len(nums) <=1:
        return nums
    mid = len(nums) // 2
    left_list = mergeSort(nums[:mid])
    right_list = mergeSort(nums[mid:])
    return merge(left_list, right_list)

listanumeros4= [9,55,28,159,4,1,2,5,6,11,0]
listar_num_ordenados = mergeSort(listanumeros4)
print(listar_num_ordenados)


##############################################
#Buble sort

def sort_bubble(nums):
    for i in range(len(nums)-1, 0,-1):
        for j in range(i):
            if nums[j] > nums[j +1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

listanumeros5= [9,55,28,159,4,1,2,5,6,11,0]
sort_bubble(listanumeros5)
print(listanumeros5)

arr = [ 5,2,1,55,84,13,20,11,10]
print('arreglo antes: ', arr)


band = False
while band == False:
    for i in range(len(arr) -1 ):
        band=True
        if arr[i] > arr[i+1]:
            aux = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = aux
            band = False

print('arreglo desp: ', arr)

## Ordenamiento por seleccion

arr1 = [4,2,7,12,9,4,1]
print(arr1, 'inicial')
for i in range(0 ,len(arr1)):
    minimo = i
    for j in range(i+1, len(arr1)):
        if arr1[minimo] > arr1[j]:
            minimo = j

    temp = arr1[i]
    arr1[i] = arr1[minimo]
    arr1[minimo] = temp

    print(arr1[minimo],arr1[i],arr1)

## ordenamiento por insercion
arreglo = [1,5,9,6,3,25,55]
for j in range(1, len(arreglo)):
    key = arreglo[j]
    i = j-1
    while i >=0 and arreglo[i] > key:
        arreglo[i+1] = arreglo[i]
        i = i-1
    arreglo[i+1] = key

print(arreglo)

#merge sort


