"""EV3_PROGRA

Problema 1
"""

archi1=open("datos.txt","w")
archi1.write("Primer línea.\n")
archi1.write("Segunda línea.\n")
archi1.write("Tercer línea.\n")
archi1.close()

archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()

"""Problema 2"""

archi1=open("datos.txt","r")
contenido=archi1.read(6)
print(contenido)
archi1.close()

archi1=open("datos.txt","r")
linea=archi1.readline()
while linea!='':
    print(linea, end='')
    linea=archi1.readline()
archi1.close()

"""Problema 3"""

archi1=open("datos.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()

archi1=open("datos.txt","r")
contenido=archi1.read(6)
print(contenido) # imprime: Primer
archi1.close()

archi1=open("datos.txt","r")
linea=archi1.readline()
while linea!='':
    print(linea, end='')
    linea=archi1.readline()
archi1.close()

while linea!='':
    print(linea, end='')
    linea=archi1.readline()

archi1=open("datos.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()

"""Problema 4"""

archi1=open("datos.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()

"""Problema 5"""

archi1=open("datos.txt","a")
archi1.write("nueva línea 1\n")
archi1.write("nueva línea 2\n")
archi1.close()
archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()

"""Problema 6"""

archi1=open("datos.txt","r+")
contenido=archi1.read()
print(contenido)
archi1.write("Otra línea 1\n")
archi1.write("Otra línea 2\n")
archi1.close()

"""Problema 7"""

archi1=open("datos.txt","w", encoding="utf-8")
archi1.write("Primer línea.\n")
archi1.write("Segunda línea.\n")
archi1.write("Tercer línea.\n")
archi1.close()
