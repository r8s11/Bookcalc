
row = 9
column = 3
bookPages = 21

counter = 1
for i in range (row):

    for j in range (column):
        print("Day" , str(counter) + ":", bookPages , "Pages", end = " \t")
        counter += 1
    print('\n')