#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.iodevices import Ev3devSensor
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import LightSensor
from tarea import Tareas
from contar_lineas import ContadorLineas
from seguir_lineas import SeguidorLineas
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
MD = Motor(Port.C,Direction.COUNTERCLOCKWISE)
MI = Motor(Port.B,Direction.COUNTERCLOCKWISE)
MG = Motor(Port.A,Direction.CLOCKWISE)
SI = ColorSensor(Port.S2)
SD = LightSensor(Port.S4)
#SC = ColorSensor(Port.S3)
SC =  Ev3devSensor(Port.S3)
Sonidos = SoundFile()
movimientos = Tareas(ev3,MD,MI,MG,SD,SI,SC,wait,Stop,Sonidos,Color,DriveBase,time)
condiciones = Tareas(ev3,MD,MI,MG,SD,SI,SC,wait,Stop,Sonidos,Color,DriveBase,time)
#contador = ContadorLineas()
#seguidor = SeguidorLineas(ev3,MD,MI,MG,SD,SI,SC,wait,Stop,Sonidos,contador,2,time)

# Write your program here.






ev3.speaker.beep()
'''

movimientos.Configuracion_Robot(300,200,100)
movimientos.agarrar_Aldeano("Bajar",80)
movimientos.mover_por_distancia(83,"adelante")
movimientos.girar_n_grados(90,"izquierda")
movimientos.Configuracion_Robot(100,300,100)
movimientos.mover_por_distancia(80,"adelante")
movimientos.agarrar_Aldeano("Subir",80+70)
movimientos.girar_n_grados(45,"izquierda")
movimientos.Configuracion_Robot(200,400,100)
movimientos.mover_por_distancia(40,"adelante")
movimientos.girar_n_grados(45,"derecha")
movimientos.Configuracion_Robot(300,200,100)
movimientos.mover_por_distancia(70,"adelante")
movimientos.girar_n_grados(45,"derecha")
movimientos.Configuracion_Robot(200,400,100)
movimientos.mover_por_distancia(20,"adelante")
movimientos.agarrar_Aldeano("Bajar",70)
movimientos.mover_por_distancia(3,"atras")
movimientos.agarrar_Aldeano("Subir",70)
movimientos.mover_por_distancia(17,"atras")
movimientos.girar_n_grados(75,"izquierda")
movimientos.mover_por_distancia(10,"adelante")
movimientos.agarrar_Aldeano("Bajar",80)
movimientos.mover_por_distancia(10,"atras")
movimientos.girar_n_grados(30,"derecha")
movimientos.Configuracion_Robot(300,200,100)
movimientos.mover_por_distancia(70,"atras")



#seguidor.mover_por_distancia(40,"adelante")
#movimientos.agarrar_Aldeano("Subir")
#movimientos.mover_por_distancia(40,"adelante")
'''
'''
while True:
    condiciones.detectar_Color()
    if condiciones.actualizar_Color() == 1:
        print("Amarillo")
        movimientos.mover_por_distancia(15,"atras")
        movimientos.girar_n_grados(45,"izquierda")
        movimientos.agarrar_Aldeano("Bajar")
        movimientos.mover_por_distancia(10,"adelante")
        movimientos.agarrar_Aldeano("Subir")
        movimientos.girar_n_grados(45,"derecha")
        movimientos.mover_por_distancia(45,"adelante")
        movimientos.girar_n_grados(92,"izquierda")
    elif condiciones.detectar_Color_H() == 2:
        print("Azul")
        movimientos.mover_por_distancia(15,"atras")
        movimientos.girar_n_grados(45,"izquierda")
        movimientos.agarrar_Aldeano("Bajar")
        movimientos.mover_por_distancia(10,"adelante")
        movimientos.agarrar_Aldeano("Subir")
        movimientos.girar_n_grados(50,"izquierda")
        movimientos.mover_por_distancia(85,"adelante")
        movimientos.girar_n_grados(95,"izquierda")
    elif condiciones.actualizar_Color() == 3:
        print("Rojo")
    else:
        print("Verde")


'''
movimientos.Configuracion_Robot(300,300,100)
movimientos.mover_por_distancia(5,"adelante")
movimientos.girar_n_grados(23,"izquierda")
movimientos.mover_por_distancia(40,"adelante")
movimientos.agarrar_Aldeano("Subir")
movimientos.girar_n_grados(60,"izquierda")
movimientos.agarrar_Aldeano("Bajar")
movimientos.mover_por_distancia(5,"adelante")
movimientos.agarrar_Aldeano("Subir")
movimientos.girar_n_grados(36,"izquierda")
movimientos.mover_por_distancia(65,"adelante")
movimientos.agarrar_Aldeano("Bajar")
movimientos.mover_por_distancia(5,"atras")
movimientos.agarrar_Aldeano("Subir")
movimientos.girar_n_grados(120,"derecha")
movimientos.mover_por_distancia(35,"adelante")
movimientos.girar_n_grados(90,"izquieda")
movimientos.mover_por_distancia(80,"adelante")
movimientos.girar_n_grados(90,"izquieda")
movimientos.mover_por_distancia(10,"adelante")
movimientos.agarrar_Aldeano("Bajar")
movimientos.agarrar_Aldeano("Bajar") 
movimientos.girar_n_grados(90,"izquieda")
movimientos.mover_por_distancia(130,"adelante")
movimientos.girar_n_grados(90,"izquieda")
movimientos.mover_por_distancia(35,"adelante")
movimientos.agarrar_Aldeano("Subir")
movimientos.girar_n_grados(90,"izquieda")
movimientos.mover_por_distancia(35,"adelante")
movimientos.agarrar_Aldeano("Bajar") 
movimientos.agarrar_Aldeano("Subir")
movimientos.girar_n_grados(25,"izquierda")
movimientos.mover_por_distancia(60,"adelante")
movimientos.girar_n_grados(25,"derecha")
movimientos.mover_por_distancia(60,"adelante")
movimientos.agarrar_Aldeano("Bajar") 
movimientos.mover_por_distancia(5,"atras")
movimientos.agarrar_Aldeano("Subir")
movimientos.mover_por_distancia(15,"atras")
movimientos.girar_n_grados(90,"izquierda")
movimientos.mover_por_distancia(30,"adelante")
movimientos.agarrar_Aldeano("Bajar") 
movimientos.agarrar_Aldeano("Bajar") 
movimientos.girar_n_grados(90,"izquierda")
movimientos.mover_por_distancia(150,"adelante")
movimientos.girar_n_grados(90,"derecha")
movimientos.mover_por_distancia(45,"atras")
