pos = -1
def search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:  #low cant be gretare thn high
        midpoint = (low+high)  // 2         #integer division

        if list[midpoint] == target:
            globals() ['pos'] = midpoint
            pos = "midpoint"
            return True
        elif list[midpoint] < target:
            low = midpoint + 1
        elif list[midpoint] > target:
            high = midpoint - 1
    return False

list = [1, 5, 7, 52, 87, 99 ,101]
target = 99

if search(list, target):
    print("Found at", pos+1)
else:
    print("Not Found")
