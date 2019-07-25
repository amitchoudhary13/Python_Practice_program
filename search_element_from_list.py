'''
Write a program to search given element from the list. Use your own function to search an element from list. Note: Function should receive variable length arguments and search each of these arguments present in the list.

'''

def search_list(lst,*terms_to_search):
    for term in terms_to_search:
        if term in lst:
            print(term, 'is in the list')
        else:
            print(term, 'is not in the list')


lst = [1,2,3,4,5,6,7,8,9]
terms_to_search = list(map(int,input('enter numbers to search in list : ').split()))


