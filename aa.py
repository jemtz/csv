import csv

with open ('students.csv') as f:
     reader = csv.reader(f,delimiter=",")
     for row in reader:
       print("NOMBRE: {0}, APELLIDO: {1}, EDAD: {2}, GRADO: {3}, GRUPO: {4}, CORREO: {5}"
           .format(row[0], row[1], row[2], row[3], row[4], row[5]))
