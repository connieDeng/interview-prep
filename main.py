from maxConsecutiveOnes import *

def main():
    arr = [1,1,0,1,1,1]
    print(arr)
    print('max num of consecutive 0s: ' + str(findMaxConsecutiveOnes(arr)))
    print(len(arr)-1)

if __name__ == "__main__":
    main()
