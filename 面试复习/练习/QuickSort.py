
def quick_sort(array, left, right):
	# Quick Sort  O(nlogn)

	if left >= right:
		return 
    # set the most left element as pivot
	pivot = array[left]
	low = left
	high = right 

	while low < high:
		while low < high and array[high] > pivot:
			high -= 1
		array[low] = array[high]

		while low < high and array[low] <= pivot:
			low += 1
		array[high] = array[low]

	array[low] = pivot

	quick_sort(array, left, low-1)
	quick_sort(array, low+1, right)

def quickSort(array: list[int], left: int, right: int):

	if left >= right:
		return

	pivot = array[left]

	l_pointer = left
	r_pointer = right

	while l_pointer < r_pointer:

		while l_pointer < r_pointer and array[r_pointer] > pivot:
			r_pointer -= 1
		array[l_pointer] = array[r_pointer]

		while l_pointer < r_pointer and array[l_pointer] <= pivot:
			l_pointer += 1
		array[r_pointer] = array[l_pointer]

	array[l_pointer] = pivot

	quickSort(array, left, l_pointer - 1)
	quickSort(array, l_pointer + 1, right)



array = [54,26,93,17,77,31,44,55,20]
quickSort(array, 0, len(array)-1)
print(array)
