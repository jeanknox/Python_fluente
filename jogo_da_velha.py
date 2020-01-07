tabula = [["_"]*3 for i in range(3)]

Pos_y, Pos_x = str(input("Digite a posicao que deseja marcar:")).split(",")
print(Pos_x, Pos_y)
if int(Pos_x) & int(Pos_y) is not in [0, 1, 2]:
    raise "Out of index"
tabula[int(Pos_y)][int(Pos_y)] = "X"
print(tabula)
