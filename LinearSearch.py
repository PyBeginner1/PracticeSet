pos = -1
def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals() ['pos'] = i
            return True
        i = i+1
    return False

list = [ 1, 3 ,4 ,5, 7, 9, 21, 23, 45]
n = 23

if search(list, n):
    print("Found at" ,pos+1)
else:
    print("Not Found")
