def uniqEvenSort_1(lst):
    max_ele = max(lst)
    return_lst=set(range(0,max_ele+1,2))
    return sorted(return_lst.intersection(lst))


def uniqOddSortSet(lst):
    max_ele = max(lst)
    return_lst=set(range(1,max_ele+1,2))
    return sorted(return_lst.intersection(lst))


def evenSortLoop(lst):
    res_lst=[]
    for i in lst:
        if (i%2==0):
            res_lst.append(i)
    return sorted(res_lst)

def oddSortLoop(lst):
    res_lst=[]
    for i in lst:
        if (i%2!=0):
            res_lst.append(i)
    return sorted(res_lst)

def dummy():
    print("dummy")