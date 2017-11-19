# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 16:25:53 2017

@author: Santiago-Pc
"""
import serial
import matplotlib.pyplot as plot

#--------------------------------------------------------------
# Comunicacion serial
#--------------------------------------------------------------
port="/dev/ttyUSB0"
Arduino=serial.Serial(port,9600)
Arduino.flushInput()

plot.ion() 

#--------------------------------------------------------------
# Declaracion de variables globales
#--------------------------------------------------------------
x = []
y = []
t = range(17)
lista = t
sensores = []
z = 1
grados =0
cont1 = 0
variable= 0
jugar=0

#--------------------------------------------------------------
# INICIO DEL PROGRAMA
#--------------------------------------------------------------

while z<=1:
    
    sensores = []
    x = []
    y = []
    input=Arduino.readline()   
    In=int(input)
    variable=In
    
    while(variable == 97):
        for i in range(36):
            input=Arduino.readline()   
            In=int(input)
            sensores.append(In)   
            if(sensores[i]==98):
                variable=0
                jugar=0
#--------------------------------------------------------------
# Rutina hacia ADELANTE
#--------------------------------------------------------------
        
        if(jugar==1):
            print ('Me perdi')
            
        if(grados==0 and jugar==0):
            print ('Adelante')
            for i in range(len(t)+1):
                if(sensores[i] < 20):
                    cont1=cont1+1
                    
                if(i==5):
                    x1 = [0,0,0,0,0,0]
                    y1 = [0,0,0,0,0,0]
                    if(cont1 >= 2):
                        x1 = [6,6,6,6,6,6]
                        y1 = [1,2,3,4,5,6]                
                        cont1 = 0
                    else:
                        cont1 = 0
                        
                if(i == 11):            
                    x2 = [0,0,0,0,0,0]
                    y2 = [0,0,0,0,0,0]
                    
                    if(cont1 >= 2):
                        x2 = [1,2,3,4,5,6]
                        y2 = [6,6,6,6,6,6]
                        cont1 = 0
                    else:
                        cont1 = 0
                        
                if(i == 17):            
                    x3 = [0,0,0,0,0,0]
                    y3 = [0,0,0,0,0,0]
                    
                    if(cont1 >= 2):
                        x3 = [1,1,1,1,1,1]
                        y3 = [1,2,3,4,5,6]
                        cont1 = 0
                    else:
                        cont1 = 0
                
            x.append(x1)
            x.append(x2)
            x.append(x3)
            y.append(y1)
            y.append(y2)
            y.append(y3)
            plot.plot(x,y,'bx')
            
            plot.pause(0.05) 
            plot.cla()
            if(x1==[6,6,6,6,6,6] and y2==[6,6,6,6,6,6] and x3==[1,1,1,1,1,1]):
                grados=90
                jugar=1
            if(x1==[6,6,6,6,6,6] and y2==[6,6,6,6,6,6] and x3==[0,0,0,0,0,0]):
                grados=270
                jugar=1
            if(x1==[0,0,0,0,0,0]):
                grados=90
                jugar=1     
                
#--------------------------------------------------------------
# Rutina hacia la DERECHA
#--------------------------------------------------------------

        if(grados==90 and jugar==0):
            print ('Derecha')
            for i in range(len(t)+1):
                if(sensores[i] < 20):
                    cont1=cont1+1
                    
                if(i==5):
                    x1 = [0,0,0,0,0,0]
                    y1 = [0,0,0,0,0,0]
                    if(cont1 >= 2):
                        x1 = [1,2,3,4,5,6]
                        y1 = [1,1,1,1,1,1]                
                        cont1 = 0
                    else:
                        cont1 = 0
                        
                if(i == 11):            
                    x2 = [0,0,0,0,0,0]
                    y2 = [0,0,0,0,0,0]
                    
                    if(cont1 >= 2):
                        x2 = [6,6,6,6,6,6]
                        y2 = [1,2,3,4,5,6]
                        cont1 = 0
                    else:
                        cont1 = 0
                        
                if(i == 17):            
                    x3 = [0,0,0,0,0,0]
                    y3 = [0,0,0,0,0,0]
                    
                    if(cont1 >= 2):
                        x3 = [1,2,3,4,5,6]
                        y3 = [6,6,6,6,6,6]
                        cont1 = 0
                    else:
                        cont1 = 0
        
            x.append(x1)
            x.append(x2)
            x.append(x3)
            y.append(y1)
            y.append(y2)
            y.append(y3)
            plot.plot(x,y,'bx')
            
            plot.pause(0.05) # esto pausará el gráfico
            plot.cla()
            
            if(y1==[1,1,1,1,1,1] and x2==[6,6,6,6,6,6] and y3==[6,6,6,6,6,6]):
                grados=180
                jugar=1
            if(y1==[1,1,1,1,1,1]  and x2==[6,6,6,6,6,6] and y3==[0,0,0,0,0,0]):
                grados=0
                jugar=1
            if(y1==[0,0,0,0,0,0]):
                grados=180
                jugar=1        
                
#--------------------------------------------------------------
# Rutina hacia ATRAS
#--------------------------------------------------------------

        if(grados==180 and jugar==0):
            print ('Atras')
            for i in range(len(t)+1):
                if(sensores[i] < 20):
                    cont1=cont1+1
                    
                if(i==5):
                    x1 = [0,0,0,0,0,0]
                    y1 = [0,0,0,0,0,0]
                    if(cont1 >= 2):
                        x1 = [1,1,1,1,1,1]
                        y1 = [1,2,3,4,5,6]                
                        cont1 = 0
                    else:
                        cont1 = 0
                        
                if(i == 11):            
                    x2 = [0,0,0,0,0,0]
                    y2 = [0,0,0,0,0,0]
                    
                    if(cont1 >= 2):
                        x2 = [1,2,3,4,5,6]
                        y2 = [1,1,1,1,1,1]
                        cont1 = 0
                    else:
                        cont1 = 0
                        
                if(i == 17):            
                    x3 = [0,0,0,0,0,0]
                    y3 = [0,0,0,0,0,0]
                    
                    if(cont1 >= 2):
                        x3 = [6,6,6,6,6,6]
                        y3 = [1,2,3,4,5,6]
                        cont1 = 0
                    else:
                        cont1 = 0
        
            x.append(x1)
            x.append(x2)
            x.append(x3)
            y.append(y1)
            y.append(y2)
            y.append(y3)
            plot.plot(x,y,'bx')
            
            plot.pause(0.05)
            plot.cla()
            
            if(x1==[1,1,1,1,1,1] and y2==[1,1,1,1,1,1] and x3==[6,6,6,6,6,6]):
                grados=270
                jugar=1
            if(x1==[1,1,1,1,1,1] and y2==[1,1,1,1,1,1] and x3==[0,0,0,0,0,0]):
                grados=90
                jugar=1
            if(x1==[0,0,0,0,0,0]):
                grados=270
                jugar=1
                
#--------------------------------------------------------------
# Rutina hacia la IZQUIERDA
#--------------------------------------------------------------

        if(grados==270 and jugar==0):
            print ('Izquierda')
            for i in range(len(t)+1):
                if(sensores[i] < 20):
                    cont1=cont1+1
                    
                if(i==5):
                    x1 = [0,0,0,0,0,0]
                    y1 = [0,0,0,0,0,0]
                    if(cont1 >= 2):
                        x1 = [1,2,3,4,5,6]
                        y1 = [6,6,6,6,6,6]                
                        cont1 = 0
                    else:
                        cont1 = 0
                        
                if(i == 11):            
                    x2 = [0,0,0,0,0,0]
                    y2 = [0,0,0,0,0,0]
                    
                    if(cont1 >= 2):
                        x2 = [1,1,1,1,1,1]
                        y2 = [1,2,3,4,5,6]
                        cont1 = 0
                    else:
                        cont1 = 0
                        
                if(i == 17):            
                    x3 = [0,0,0,0,0,0]
                    y3 = [0,0,0,0,0,0]
                    
                    if(cont1 >= 2):
                        x3 = [1,2,3,4,5,6]
                        y3 = [1,1,1,1,1,1]
                        cont1 = 0
                    else:
                        cont1 = 0
        
            x.append(x1)
            x.append(x2)
            x.append(x3)
            y.append(y1)
            y.append(y2)
            y.append(y3)
            plot.plot(x,y,'bx')
            
            plot.pause(0.05)
            plot.cla
            
            if(y1==[6,6,6,6,6,6]  and x2==[1,1,1,1,1,1] and y3==[1,1,1,1,1,1]):
                grados=0
                jugar=1
            if(y1==[6,6,6,6,6,6]  and x2==[1,1,1,1,1,1] and y3==[0,0,0,0,0,0]):
                grados=180
                jugar=1
            if(y1==[0,0,0,0,0,0]):
                grados=0
                jugar=1
        
           
        
        
    
   

