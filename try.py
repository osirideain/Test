import itertools
list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
new = []
new_1 = []

for x in list:
    try:
        if numblist[x] < numblist[x + 1] - 1:
            print('yay')
        else:
            print('gap')
    except:
        pass

    
