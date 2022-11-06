#Treasure map - user selects which row & column to mark with "X"
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\nInput row & column as 2 digit number. EX: row 1 column 3 = 13: ")

#Seperate user 2 digit input into row variable and column variable
column = int(position[0])
row = int(position[1])

map[column -1 ][row - 1] = "X"

#Print map with X marked ont he selected square
print(f"{row1}\n{row2}\n{row3}")

