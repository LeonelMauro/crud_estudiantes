import json
class Persona:
    def __init__(self,apellido,nombre,correo,telefono):
        self.apellido = apellido
        self.nombre = nombre
        self. correo = correo
        self. telefono = telefono
        

    def __str__(self):
            return 'Apellido y nombre {} {}, correo: {}, Telefono: {}'.format(self.apellido,self.nombre,self.correo,self.telefono)

class Usuario(Persona):
    def __init__(self, apellido, nombre, correo, telefono):
        super().__init__(apellido, nombre, correo, telefono)

lista_usuario=[]


def ingresar():
    apellido= input('Ingrese el apellido:').title()
    nombre= input('Ingrese el nombre:').title()
    correo = input('Ingrese el correo:').title()
    telefono= input('Ingrese el tel:').title()
    agregar=Usuario(apellido,nombre,correo,telefono)
    lista_usuario.append(agregar)
    with open('Archivo.json', 'r') as f:
            data = json.load(f)
def json(usuarios):
    datos=[]
    for i in usuarios:
        datos.append(usuarios.__dict__)
    with open('arch.json', 'w') as f:
        json.dump(datos, f, indent= 4)




def buscar_usuario():
    apellido= input('Ingrese el apellido del usuario:').title()
    for row in lista_usuario:
        if row.apellido==apellido:
            print(row)
            break
    else:
        print('No se encuentra en la lista')

def borrar_usuario(usuarios):
    apellido= input('Ingrese el apellido del usuario:').title()
    for i in usuarios:
            if i.apellido==apellido:
                usuarios.pop(i.apellido)
                print('Usuario eliminado')
                break
    else:
        print('No se encuetra en la lista')

def menu():
    print('MENU\n1_Agregar usuario\n2_Abrir lista de usuario\n3_Eliminar usuario\n4_Buscar usuario')

while True:
    menu()
    try:
        opcion=int(input('Eliga la opcion:'))
    except:
        opcion=-1
    if opcion==1:
        ingresar() 
        json(lista_usuario)
        
    elif opcion==2:  
        for i in lista_usuario:
            print(i)
    
    elif opcion==3:
        borrar_usuario(lista_usuario)
    elif opcion==4:
        buscar_usuario()
    
    else:
        print('Opcion incorrercta')




