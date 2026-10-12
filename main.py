def saludar(nombre):
    return "Buenas " + nombre

print(saludar("Ana"))
print(saludar("Lu"))

def despedir(nombre:str)->str:
    return "Chau " + nombre
print(despedir("Lu"))

def sumar(a:int,b:int)->int:
    return a + b
print(sumar(2,3))