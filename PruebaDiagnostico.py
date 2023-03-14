#Nombre: Javiera Cabezas
#Taller de Programación Aplicada
#La Máquina de Chistes Informáticos

        
class Chiste():
    def __init__(self):
        self.listachistes = ["Chiste1","chiste2","chiste3","chiste4","chiste5"]
        
    def mostrarchiste(self,x):
        list = self.listachistes
        print(list[x])  
                   
    
def menu(x):
    print("------ La Máquina de Chistes Informáticos ------")
    print("¿Quieres que te muestre un chiste informático?")
    print("1-. Si")
    print("2-. No")
    resp = int(input("Opción:"))
    if resp == 1:
        print("---------------------------")
        n.mostrarchiste(x)
        print("---------------------------")
        x+=1
        if x == 5:
            x = 0
        menu(x)
    elif resp == 2:
        exit()        
 
x = 0       
n = Chiste()        
menu(x)

