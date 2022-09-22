def abv_delete(text):
    result = []

    for i in text.split():
        if 'абв' not in i:
            result += i.split()
    
    print(' '.join(result))

abv_delete('абвгдейка - это передача')