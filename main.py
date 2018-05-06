#import matplotlib as mpl
#import matplotlib.pyplot as plt
#import numpy as np
#import TempSensorModule as Tp
#import WebModule as Wb
import TempSensorModule.Module1 as Tp
import WebModule.Module2 as Wb
import ConditionModule.Module3 as Cd
import ClassModule.Module4 as CM
import InheritClassModule.Module5 as ICM
import sys
import AbstracClassModule.Module6 as AM
import StaticClass.Module7 as SC
import PropertyClass.Module8 as PC

Tp.Hello()
Wb.Hello()
#x=np.linspace(0,20,100)
#plt.plot(x, np.sin(x))
#plt.show()
msg = "Hello Python"
print(msg)
print(f"Please input number")
try:
    num = int(input())
except Exception as e:
    print(e)
    sys.exit()

Cd.if_function(num)
Cd.while_function(num)
Cd.for_function(num)

A = CM.classPratice()
B = ICM.InheritClass("I am son",2)
print(A.Hello())
print(A.name)
print(A.getprivate())
print(A)
print(B.Hello())
print(B.id)
print(B.name)
print(B.getprivate())
#print(B.__privatefunction())
print(B)
print(sys.argv[0])
print(sys.argv[1])

game = AM.ConsoleGame()
print(game.message("hellllo"))
print(game.welcome)


print(SC.staticClass.add(5, 6))
static = SC.staticClass()
print(static.add(5, 6)) 

propertyC = PC.PropertyClass(20,30)
#print(propertyC.__height)
print(propertyC.getHeight())