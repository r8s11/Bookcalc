
bp_input = int(input("How many pages is the book?\n"))
days_input = int(input("How many days to read?\n"))
print("")

row = round(days_input / 3) 
column = 3
bookPages = (bp_input / days_input)

num_of_day = 1

while num_of_day <= (days_input):
    for j in range(3):
        print("Day" , str(num_of_day) + ":", round(bookPages) , "Pages", end = " \t")
        num_of_day += 1
        if num_of_day > days_input:
            break
    print('\n')