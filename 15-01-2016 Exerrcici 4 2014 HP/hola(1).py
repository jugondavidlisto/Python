import msvcrt #CMD

num = raw_input() #Numero de entrada

maxc=1000 #Caramelos Max
maxp=30 #Participantes Max

if num > maxc:
 print ("Has superat els caramels")
elif num > maxp:
 print (“Has superat els participants")
else:
 print ("hola")

msvcrt.getch() #Siempre en la ultima linia