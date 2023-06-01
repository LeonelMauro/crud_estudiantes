import csv
import json

with open('data.csv', 'r') as f:
    reader=csv.reader(f)

    dato=[]
    for row in reader:
        dato.append({'nombre':row[0], 'Edad':row[1], 'Provincia':row[2]})

with open ("data_de_datos.json", 'w') as file:
  json.dump(dato, file, indent=4)