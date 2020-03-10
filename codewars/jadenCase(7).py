def to_jaden_case(string):
    newArray = []
    array = [1, 2, 3, 4]
    for x in array:
        newArray.append(x)
    
    newArray = [x for x in array]
    return ' '.join([x.capitalize() for x in string.split(' ')])