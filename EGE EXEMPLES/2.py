print('w,x,y,z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not(x or y)) and (not(w)) or (not(z or w)) and y:
                    print(w,x,y,z)
