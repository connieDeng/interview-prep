from maxConsecutiveOnes import *
from numEvenDigits import *
from sortedSquareOrder import *
from insertionSort import *
from mergeSort import *
from duplicateZeros import *
from mergeSortedArr import *
from reverseInt import *
from validParentheses import *
from searchInsertPosition import *

def main():
#test for max consecutive ones
    # arr = [1,1,0,1,1,1]
    # print(arr)
    # print('max num of consecutive 0s: ' + str(findMaxConsecutiveOnes(arr)))
    # print(len(arr)-1)

#test for num of even digits
    # arr = [12, 345, 2, 6, 7896]
    # print(findNumbers(arr))

#test for sorted square order
    # arr = [-4,-1,0,3,10]
    # print(sortedSquares(arr))

#test for insertion sort
    # arr = [5,6,1]
    # print(insertionSort(arr))

#test for merge sort
    # arr = [12, 345, 2, 6, 7896]
    # print(mergeSort(arr))

#test for duplicate zeros
    # arr = [12, 345, 0, 0, 2, 0, 6, 7896]
    # duplicateZeros(arr)
    # print(arr)

#test for merging sorted arrays
    # arr1 = [4, 0, 0, 0, 0, 0]    
    # arr2 = [1,2,3,5,6]
    # merge(arr1, 1, arr2, 5)
    # print(arr1)

#test for reverse int
    # print(reverseInt(1534269))

#test for valid parentheses
    # str1 = "){"
    # print(isValid(str1))

#test for search insert position
    arr = [1]
    target = 0
    print(searchInsert(arr, target))

if __name__ == "__main__":
    main()
