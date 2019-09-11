
def checkSection(arr, total, func):
    result = arr[0]
    print(result)
    for i in range(len(arr) - 1):
        if(func == '+'):
            result += arr[i + 1]
        elif(func == '-'):
            result -= arr[i + 1]
        elif(func == '*'):
            result *= arr[i + 1]
        elif(func == '/'):
            result /= arr[i + 1]
        print(result)
    if(result == total):
        return True
    else:
        return False

print(checkSection([2,5,4,3], 14, '+'))
