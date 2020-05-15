for outer in range(2,10):
    for inner in range (2, outer):
        if not outer % inner:
            print(outer, '=', inner, '*', int(outer/inner))
            break
    else:
        print(outer, 'is prime')
