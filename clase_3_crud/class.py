import json
class Instituto :
    def __init__(self,apellido,nombre,correo,pais,sexo,):
   
        self.apellido = apellido
        self.nombre = nombre
        self.correo = correo
        self.pais = pais
        self.sexo = sexo
      
    def __str__(self):
        return "Apellido y nombre: {} {}, Correo: {}, Pais:  {}, Sexo: {}".format(self.apellido,self.nombre,self.correo,self.pais,self.sexo)
    
class Estudiante(Instituto):
    def __init__(self, apellido, nombre, correo, pais, sexo):
        super().__init__(apellido, nombre, correo, pais, sexo)
        
lista_estudiantes=[]

def cargar_desde_json():

        with open('Archivo.json', 'r') as f:
            data = json.load(f)
            for estudiante_data in data:
                estudiante = Estudiante(estudiante_data['apellido'], estudiante_data['nombre'], estudiante_data['correo'], estudiante_data['pais'], estudiante_data['sexo'])
                lista_estudiantes.append(estudiante)
            
    

def guardar_en_json(estudiantes):
    data = []
    for estudiante in estudiantes:
        data.append(estudiante.__dict__)
    
    with open('Archivo.json', 'w') as f:
        json.dump(data, f, indent=4)
    print('Datos guardados en el archivo JSON.')

"""agregar estudiante"""

def Alumnos():
    
    apellido=input('Apellido: ').title()
    nombre=input('Nombre: ').title()
    correo=input('Correo: ').title()
    pais=input('Pais: ').title()
    sexo=input('Sexo: ').title()
    agregar=Estudiante(apellido,nombre,correo,pais,sexo)
    lista_estudiantes.append(agregar)
    guardar_en_json(lista_estudiantes)
    print('Estudiante agregado exitosamente.')
 
        
"""borrar estudiante"""
def borrar(estudiantes):
    apellido = input('Ingrese el apellido del estudiante a borrar: ').title()
    indice= None

    for i, estudiante in enumerate(estudiantes):
        if estudiante.apellido == apellido:
            indice=i
            break
    if indice is not None:
        estudiantes.pop(indice)
        print('Estudiante eliminado')
    else:
        print('>El apellido no se encuentra en la lista')
    
"""buscar estudiante"""
def buscar():   
    nombre = input('Ingrese el nombre por apellido: ').title()
    posicion = list(filter(lambda estudiante: estudiante.apellido == nombre, lista_estudiantes))
    for row in posicion:
        print(row)
def pasar_a_json(estudiantes):
    
    arch_js=json.dumps(estudiantes.__dict__)
    python=json.loads(arch_js)
    with open('Archivo.json','w') as f:
        json.dump(python, f, indent=4)



def menu():
    print('MENU\n1_Agregar estudiante\n2_Abrir lista de estudiantes\n3_Eliminar estudiante\n4_Buscar estudiante')

while True:
    menu()
    try:
        opcion=int(input('Eliga la opcion:'))
    except:
        opcion=-1
    if opcion==1:
        Alumnos() 
        
    elif opcion==2:  
        for i in lista_estudiantes:    
            print(i)
    elif opcion==3:
        borrar(lista_estudiantes)
    elif opcion==4:
        buscar()
    
    else:
        print('Opcion incorrercta')





#arch_js=json.dumps(agregar.__dict__)
#    lista_estudiantes.append(arch_js)
 #   python=json.loads(arch_js)
 #   with open('Archivo.json','a') as f:
#        json.dump(python, f, indent=4)