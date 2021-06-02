import csv
nombre = []
apellido = []
edad = []
grado = []
grupo = []
correo = []
union2 = []

# Menú principal
def menu():
  option = input("""
  
  [?] Seleccione opción:
  1. Ingresar un Alumno
  2. Guardar y salir
  > """)

  if option == "1":
    nombre.append(input("Ingresa el Nombre:   "))
    apellido.append(input("Ingresa el Apellido:   "))
    edad.append(input("Ingresa la Edad:   "))
    grado.append(input("Ingresa el Grado:   "))
    grupo.append(input("Ingrese el Grupo:   "))
    correo.append( input("ingresa el Correo:   "))
    return menu()

  if option == "2":
    union = list(zip(nombre, apellido,edad,grado,grado,correo))
    with open('students.csv','w', newline= '') as file:
      writer = csv.writer(file, delimiter =',')
      writer.writerows(union)
      print("""[✓] Estudiante creado....""")
      print("Guardado exitosamente")
      print("[X] ARCHIVO CERRADO")
    exit(0)
menu()
