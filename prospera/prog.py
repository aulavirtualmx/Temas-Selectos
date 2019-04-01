import csv
#Archivo de entrada
archivoCSV = open('prospera2.csv')
entrada = csv.DictReader(archivoCSV, delimiter='|')

# Archivos de salida
nombre="AGUASCALIENTES"
salidaCSV = open(nombre + '.csv', "w")
salida = csv.writer(salidaCSV, delimiter=",")

campos = entrada.fieldnames

for reg in entrada:
   if nombre!=reg['NOM_EDO']:
        nombre=reg['NOM_EDO']
        salidaCSV.close()
        salidaCSV = open(nombre + '.csv', "w")
        salida = csv.writer(salidaCSV, delimiter=",")
        salida.writerow(campos)
   info=[]
   for i in range(len(campos)):
     info.append(reg[campos[i]]) 

   salida.writerow(info)
