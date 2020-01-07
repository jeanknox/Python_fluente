list = [1,2,3]
print("\tLista mutavel")
print("Id original {}".format(id(list)))
list *= 2
print("Id apos multiplicar por 2, {}".format(id(list)))

print("\n\tLista imutavel")

tuple = (1,2,3)
print("Id original {}".format(id(tuple)))
tuple *= 2
print("Id apos multiplicar por 2, {}".format(id(tuple)))

print("""O metodo __iadd__ realiza a adicao inplaceo o que acaba por ser mais eficente que o motodo comum economizando memoria """)
