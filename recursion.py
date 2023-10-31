def printNameNTimes(name, n):
    if n == 0:
        return
    print(name)
    printNameNTimes(name, n-1)

def print1ton(i,n):
    if i > n:
        return
    print(i)
    print1ton(i+1)


def printNto1(n):
    if n == 0:
        return
    print(n)
    printNto1(n-1)

def print1toN(n):
    # backtracking
    if n == 0:
        return
    print1toN(n-1)
    print(n)

def printnto1(i,n):
    # backtracking
    if i > n:
        return
    printnto1(i+1,n)
    print(i)


# printNameNTimes("John", 5)
# print1ton(1,10)
# printNto1(10)
# print1toN(10)
# printnto1(1,10)


def sum1(i, sum):
    if i < 1:
        return sum
    return sum1(i-1, sum+i)
'''
sum1(3,0)--->sum1(2,3)--->sum1(1,5)--->sum1(0,6)
   6    <---|    6   <---|    6   <---|                            
'''

def sum2(n):
    '''functional recursion'''
    if n == 0:
        return 0
    return n + sum2(n-1)

def sum3(i, sum):
    '''parameterized recursion'''
    if i < 1:
        print(sum)
        return
    sum3(i-1, sum+i)

# sum3(3,0)
# print(sum1(3,0))

def fact1(n):
    # return 1 if n == 1 else n * fact1(n-1)
    if n == 1:
        return 1
    return n * fact1(n-1)

def fact2 (n, prod):
    if n == 1:
        print(prod)
        return
    fact2(n-1, prod*n)
# fact2(6,1)

def fact3(n, prod):
    if n == 1:
        return prod
    return fact3(n-1, prod*n)

# print(fact1(6))
# print(fact3(6, 1))


def reverseArr1(arr, l, r):
    # 2 pointer approach without returning result
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverseArr1(arr, l+1, r-1)
def reverseArr2(arr, l, r):
    # 2 pointer approach returning result
    if l >= r:
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    return reverseArr2(arr, l+1, r-1)

def reverseArr3(arr, n, i):
    # 1 pointer approach without returning result
    if i > n//2:
        return arr
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return reverseArr3(arr, n, i+1)
def reverseArr3(arr, n, i):
    # 1 pointer approach returning result
    if i > n//2:
        return arr
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return reverseArr3(arr, n, i+1)

arr = [1,2,3,4,5,6,7,8,9]

# reverseArr(arr, 0, len(arr)-1)
# print(reverseArr1(arr, 0, len(arr)-1))
# print(reverseArr3(arr, len(arr), 0))
# print(arr)

def isPalindrome1(str1, l, r):
    # M A D A M
    if l >= r:
        return True
    if str1[l] != str1[r]:
        return False
    return isPalindrome1(str1, l+1, r-1)
def isPalindrome2(str1, i, n):
    # M A D A M
    if i > n//2:
        return True
    if str1[i] != str1[n-1-i]:
        return False
    return isPalindrome2(str1, i+1, n)
str = 'madam'
# print(isPalindrome2(str, 0, 5))
# print(str[0])


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6)) # 0 1 1 2 3 5 8

def printSubsequences(arr, i, result):
    # T.C: O(n*2^n), S.C: O(n)
    if i >= len(arr):
        print(result)
        return
    
    printSubsequences(arr, i+1, result)
    result.append(arr[i])

    # result.remove(arr[i])
    printSubsequences(arr, i+1, result)
    result.pop()

    
# -----------------
# print subsequences with sum k

def printSubsequencesOfSumK(arr, i, result, k, sum):
    # all subsequences
    if i == len(arr):
        if sum == k:
            print(result)
        return
    
    result.append(arr[i])
    sum += arr[i]
    printSubsequencesOfSumK(arr, i+1, result, k, sum)

    sum -= arr[i]
    result.pop()
    printSubsequencesOfSumK(arr, i+1, result, k, sum)

def printSubsequencesOfSumK_2(arr, i, result, k):
    # all subsequences
    if i == len(arr):
        if sum(result) == k:
            print(result)
        return
    
    result.append(arr[i])
    printSubsequencesOfSumK_2(arr, i+1, result, k)

    result.pop()
    printSubsequencesOfSumK_2(arr, i+1, result, k)


def printSubsequencesOfSumK_3(arr, i, result, k, sum):
    # one subsequence
    if i == len(arr):
        if sum == k:
            print(result)
            return True
        return False
    
    result.append(arr[i])
    sum += arr[i]
    if printSubsequencesOfSumK_3(arr, i+1, result, k, sum): return True

    sum -= arr[i]
    result.pop()
    if printSubsequencesOfSumK_3(arr, i+1, result, k, sum): return True

    return False

def printSubsequencesOfSumK_4(arr, i, result, k):
    # one subsequence
    if i == len(arr):
        if sum(result) == k:
            print(result)
            return True
        else:
            return False
    
    result.append(arr[i])
    if printSubsequencesOfSumK_4(arr, i+1, result, k) == True: return True

    result.pop()
    if printSubsequencesOfSumK_4(arr, i+1, result, k) == True: return True

    return False

def printSubsequencesOfSumK_5(arr, i, k, sum):
    # count of subsequences
    if i == len(arr):
        if sum == k:
            return 1
        return 0
    
    sum += arr[i]
    l = printSubsequencesOfSumK_5(arr, i+1, k, sum)

    sum -= arr[i]
    r = printSubsequencesOfSumK_5(arr, i+1, k, sum)

    return l + r

def printSubsequencesOfSumK_6(arr, i, result, k):
    # count of subsequences
    if i == len(arr):
        if sum(result) == k:
            return 1
        else:
            return 0
    
    result.append(arr[i])
    l = printSubsequencesOfSumK_6(arr, i+1, result, k)

    result.pop()
    r = printSubsequencesOfSumK_6(arr, i+1, result, k)

    return l + r


arr = [3,1,2]
arr1 = [1,2,1]
result = []
# print(printSubsequencesOfSumK_5(arr1, 0, 2, 0))
# print(printSubsequencesOfSumK_6(arr1, 0, [], 2))

def mergeSort(arr, low, high):
    # T.C: O(nlogn), S.C: O(n)
    if low == high:
        return
    
    mid = (low+high)//2

    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)

    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    temp = []; i = low; j = mid+1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]
    # for i in range(0, len(temp)):
    #     arr[low+i] = temp[i]

arr = [2,4,1,7,5,6,3,9]
mergeSort(arr, 0, len(arr)-1)
print(arr)