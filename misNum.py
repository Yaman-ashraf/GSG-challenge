def missing_numbers(arr):
    mini = min(arr)
    maxi = max(arr)
    
    rang = list(range(mini, maxi + 1))
    
    misNum = [num for num in rang if num not in arr]
    
    return misNum

arr = [3, 5, 7, 6, 10, 15, 11, 13, 12, 4, 20, 18]
misNum = missing_numbers(arr)
print("Missing numbers:", misNum)

def valid_input(arr):
    if isinstance(arr, list) and len(arr) > 0:
        for x in arr:
            if not isinstance(x, int):
                return False
        return True
    else:
        return False

if valid_input(arr):
    print("Valid input:", arr)
else:
    print("Invalid input.")

