def extend(lst):
    if lst:
        new_item = lst[-1] + 1
        lst.append(new_item)
    else:
        lst = [42]

def problem4_1():
    pass

def problem4_2():
    pass

def problem4_3():
    pass

def testfunction():
    mylist = [1, 3, 7]
    for i in range(1000):
        extend(mylist)
        if mylist[-1] > 10:
            break
    print(mylist)

if __name__ == '__main__':
    testfunction()