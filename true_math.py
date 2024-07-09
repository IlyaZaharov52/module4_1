from math import inf

def divide(first, second):
    div = 0
    if second == 0:
        #print('inf')
        return inf
    else:
        div = first / second
    #print(div)
    return div

divide(4, 2)
