for i in range(10, 25):
    a = i % 2
    b = i % 3
    if a == 0:
        print(i, 'bukan prima')
    elif b == 0:
        print(i, 'bukan prima')
    else:
        print(i, 'adalah bilangan prima')