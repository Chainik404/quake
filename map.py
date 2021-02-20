from settings import *

text_map = [
    'wwwwwwwwwwww',
    'w......w...w',
    'w..www...w.w',
    'w....w..ww.w',
    'w..w....w..w',
    'w..w...www.w',
    'w....w.....w',
    'wwwwwwwwwwww',
]

world_map = set()
for j, row in  enumerate(text_map):
    print("j=",j,)
    print("row",row,)
    for i, char in enumerate(row):
        print("i=",i)
        print("char",char)
        if char =="w":
            world_map.add((i * TILE, j * TILE))
