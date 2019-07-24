'''
Write function to extend the tuple with elements of list. Pass list and Tuple as parameter to the function.
'''

def extend_tuple(lst,tupl):
    lst.append(list(tupl))
    return tuple(lst)

lst=list(map(int,input('enter numbers  in list : ').split()))
tupl=tuple(list(map(int,input('enter numbers  in tuple : ').split())))

print('extended tuple',extend_tuple(lst,tupl))
