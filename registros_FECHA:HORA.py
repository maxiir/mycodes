import tkinter 
from tkinter import*
import sqlite3
from tkinter import messagebox
from datetime import datetime #LIBRERIA DE FECHA Y HORA ACTUAL CON PYTHON


def conexionbbdd():
    conexion=sqlite3.connect('registros_totales')
    cursor=conexion.cursor()
    try:
        cursor.execute("CREATE TABLE LOS_REGISTROS(NOMBRE VARCHAR(20),APELLIDO VARCHAR(20),ENTRADA_SALIDA VARCHAR(20),HORARIO DATE )")
        #cursor.execute("CREATE TABLE LOS_REGISTROS(NOMBRE VARCHAR(20),APELLIDO VARCHAR(20),ENTRADA_SALIDA VARCHAR(20),HORARIO DATE )")
        conexion.commit()
        messagebox.showinfo('bbdd','la base de datos fue creada con exito')
    except:
        messagebox.showinfo('bbdd','ya existe esta base de datos')

def salida():
    conexion=sqlite3.connect('registros_totales')
    cursor=conexion.cursor()
    
    cursor.execute("INSERT INTO LOS_REGISTROS VALUES('"+NOMBRE.get()+"','"+APELLIDO.get()+"','SALIO',CURRENT_TIMESTAMP)") #HORA Y FECHA ACTUAL-- CURRENT_TIMESTAMP
    #cursor.execute("INSERT INTO LOS_REGISTROS (NOMBRE,APELLIDO,ENTRADA_SALIDA,HORARIO)VALUES('"+NOMBRE.get()+"','"+APELLIDO.get()+"','SALIO',CURRENT_TIMESTAMP)") OTRA FORMA DE INGRESO
    conexion.commit()
    NOMBRE.set('')
    APELLIDO.set('')




def ingreso():
    conexion=sqlite3.connect('registros_totales')
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO LOS_REGISTROS (NOMBRE,APELLIDO,ENTRADA_SALIDA,HORARIO)VALUES('"+NOMBRE.get()+"','"+APELLIDO.get()+"','INGRESO',CURRENT_TIMESTAMP)")
    #CREACION DEL TRIGGER Q ALMACENA AUTOMATICAMENTE LOS CAMBIOS DE NUEVOS INSERT EN LA TABLA LOS_REGISTROS.
    #cursor.execute("CREATE TRIGGER CAPTURAR_INSERCION_AI AFTER INSERT ON LOS_REGISTROS FOR EACH ROW INSERT INTO (NOMBRE,APELLIDO,ENTRADA_SALIDA,HORARIO) VALUES(NEW.NOMBRE,NEW.APELLIDO,NEW.ENTRADA_SALIDA,CURRENT_TIMESTAMP))")
    
    conexion.commit()
    NOMBRE.set('')
    APELLIDO.set('')

def tabla_del_trigger(): #CREACION DE TABLA DE TRIGGER PARA ALMACENAR DATOS AUTOMATICAMENTE CUANDO SE INSERTE UN NUEVO REGISTRO
    conexion=sqlite3.connect('registros_totales')
    cursor=conexion.cursor()
    cursor.execute("CREATE TABLE TABLA_TRIGGER (NOMBRE VARCHAR(20),APELLIDO VARCHAR(20),ENTRADA_SALIDA VARCHAR(20),HORARIO DATE)")
    conexion.commit()


root=Tk()
root.config(bg='black')
root.title('registros secuenciales')
root.geometry('300x300')
frame=Frame()
frame.pack()
frame2=Frame()
frame2.pack()

frame.config(bg='black',width=200,height=200)
frame2.config(bg='black',width=200,height=200)

NOMBRE=StringVar()
APELLIDO=StringVar()
#FECHA_HORA=datetime.now() FECHA Y HORA ACTUAL CON PYTHON

Label(frame,text='nombre').grid(row=0,column=0)
Entry(frame,textvariable=NOMBRE).grid(row=0,column=1)
Label(frame,text='apellido').grid(row=1,column=0)
Entry(frame,textvariable=APELLIDO).grid(row=1,column=1)

Button(frame2,text='ENTRADA',command=ingreso).grid(row=0,columnspan=2)
Button(frame2,text='SALIDA',command=salida).grid(row=1,columnspan=2)

Button(frame2,text='crear bbdd',command=conexionbbdd).grid(row=2,columnspan=2)
Button(frame2,text='crear table trigger',command=tabla_del_trigger).grid(row=3,columnspan=2)


root.mainloop()


