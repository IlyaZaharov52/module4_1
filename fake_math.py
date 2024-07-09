def divide(first, second):
    div = 0
    if second == 0:
        #print('ошибка')
        return 'Ошибка'

    else:
        div = first / second
    #print(div)
    return div


divide(2, 0)