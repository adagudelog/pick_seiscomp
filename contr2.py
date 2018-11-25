#otro programa que pide contrasena
#import numpy as np    #este programa con for es mejor que con while
usu = "Angelinni"
cont = "93041005040angel"
#cu = np.arange(100)
corr = "Buen dia Angel puede continuar"
err = "                   Error, El Usuario o contrasena es incorrecto,"
den = "                   intente de nuevo"
for i in range(0, 100):           #aqui hace un bucle 100 veces   o se coloca el cu como = np.range()
     usua = input("               Usuario:   ")
     contr = input("               Contrasena:   ")
     if (usua == usu and contr == cont):
        print ("%15s %2s"%("", corr))
        break
     else:
        print (err)
        print (den)                   
####################################
#programa 3 que pide contrasena con while          #el problema con este es que al colocar != cuando es falso toma como igual "Angel" y "Angelinni"
#usua = input("               Usuario:   ")
#contr = input("               Contrasena:   ")
#while  (usua != usu and contr != cont):
#           print (err)
#           print (den)
#           usua = input("             Usuario:     ")
#           contr = input("             Contrasena:    ")
#print   ("%15s %2s"%("", corr))