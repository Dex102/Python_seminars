print('X Y Z | ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
def truth_or_false():
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                print(f'{x} {y} {z}', '              ', int(not(x or y or z) == (not(x) and not(y) and not(z))))

truth_or_false()