from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import smtplib
import pymysql
import random


def crearID():
    letras='A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    numeros='0','1','2','3','4','5','6','7','8','9'
    letra_armado=''
    numero_armado=''
    #id_armado=random(letras)+random(numeros)
    for i in range(4): #cantidad de repeticiones '5' ==tamano de codigo
        letra_armado=random.choice(letras)
        numero_armado=numero_armado+random.choice(numeros)
        id_armado=letra_armado+numero_armado
        IDs.set(id_armado)
    print(IDs)



class losframes():
    def __init__(self):
        self.frame=Frame()
        self.frame.pack()

def salir():
    root.destroy()


def insert_INS(): 
    crearID()
    connection=pymysql.connect(host='localhost',user='root',password='',db='COLEGIO')
    cursor=connection.cursor()
    cursor.execute("SELECT ID_ALU FROM ALUMNO WHERE APELLIDO= '"+APELLIDO.get()+"' AND NOMBRE='"+NOMBRE.get()+"' AND REGULARIDAD='Regular' ")
    connection.commit()
    buscar_id_alu=cursor.fetchone() #RECUPERA ID DEL ALUMNO
    id_alu=''.join(buscar_id_alu)

    cursor.execute("SELECT DNI FROM ALUMNO WHERE APELLIDO= '"+APELLIDO.get()+"' AND NOMBRE= '"+NOMBRE.get()+"' ")
    connection.commit()
    dni_alu=cursor.fetchall()
    dni.set(dni_alu) #RECUPERA DNI DEL ALUMNO
    

    cursor.execute("SELECT REGULARIDAD FROM ALUMNO WHERE APELLIDO= '"+APELLIDO.get()+"' AND NOMBRE= '"+NOMBRE.get()+"' ")
    connection.commit()
    regula_alu=cursor.fetchone() #RECUPERA SI ES REGULAR
    REG_VALU.set(regula_alu)

    cursor.execute("SELECT ID_MATERIA FROM MATERIAS WHERE NOMBRE= '"+MATERIA.get()+"' ")
    connection.commit()
    busca_id_mate=cursor.fetchone() #RECUPERA EL ID DE LA MATERIA A INSCRIBIR
    id_mate=''.join(busca_id_mate) #JOIN PASA LA TUPLA A STRING PARA SQL USAR (FETHONE!)
    


#insertar en la bbdd:
    cursor.execute("INSERT INTO INSCRIPCION VALUES('"+IDs.get()+"','"+id_alu+"','"+id_mate+"','"+ANO.get()+"', CURRENT_TIMESTAMP)")
    connection.commit()
    IDs.set('')
    ANO.set('')
    MATERIA.set('')
    NOMBRE.set('')
    id_mate=''
    id_alu=''
    
    
    messagebox.showinfo('inscripcion','inscripto a materia exitosamente!')


def insert_ALU():
    crearID()
    connection=pymysql.connect(host='localhost',user='root',password='',db='COLEGIO')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO ALUMNO VALUES('"+IDs.get()+"','"+NOMBRE.get()+"','"+APELLIDO.get()+"','"+dni.get()+"','"+DIRECCION.get()+"','"+TELEFONO.get()+"','"+REG_VALU.get()+"','"+TEL_URG.get()+"')")
    connection.commit()
    IDs.set('')
    NOMBRE.set('')
    APELLIDO.set('')
    dni.set('')
    DIRECCION.set('')
    TELEFONO.set('')
    TEL_URG.set('')
    REG_VALU.set('')
    messagebox.showinfo('inscripciones','alumno registrado exitosamente!')


def insert_MATE():
    crearID()
    connection=pymysql.connect(host='localhost',user='root',password='',db='COLEGIO')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO MATERIAS VALUES('"+IDs.get()+"','"+MATERIA.get()+"')")
    connection.commit()
    IDs.set('')
    MATERIA.set('')
    messagebox.showinfo('inscripcion','Materia registrada exitosamente!')

def insert_PROF():
    crearID()
    connection=pymysql.connect(host='localhost',user='root',password='',db='COLEGIO')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO PROFESORES VALUES('"+IDs.get()+"','"+NOMBRE.get()+"','"+APELLIDO.get()+"','"+dni.get()+"','"+TELEFONO.get()+"','"+DIRECCION.get()+"')")
    connection.commit()
    IDs.set('')
    NOMBRE.set('')
    APELLIDO.set('')
    dni.set('')
    DIRECCION.set('')
    TELEFONO.set('')
    messagebox.showinfo('inscripciones','profesor agregado exitosamente!')


root=Tk()
root.title('inscripciones')
root.geometry('500x300')
ventana_root=ttk.Notebook()
ventana_root.pack(fill='both',expand='yes')

pestana_inscripcion=ttk.Frame(ventana_root)
pestana_alumno=ttk.Frame(ventana_root)
pestana_materia=ttk.Frame(ventana_root)
pestana_profesor=ttk.Frame(ventana_root)

ventana_root.add(pestana_inscripcion,text='Inscripcion')
ventana_root.add(pestana_alumno,text='agregar estudiante')
ventana_root.add(pestana_materia,text='agregar materia')
ventana_root.add(pestana_profesor,text='agregar un profesor')


frame1_pes_ins=losframes()
frame1_pes_ins.frame=Frame(pestana_inscripcion)
frame1_pes_ins.frame.pack()
frame2_pes_ins=losframes()
frame2_pes_ins.frame=Frame(pestana_inscripcion)
frame2_pes_ins.frame.pack()

frame1_pes_estudiante=losframes()
frame1_pes_estudiante.frame=Frame(pestana_alumno)
frame1_pes_estudiante.frame.pack()
frame2_pes_estudiante=losframes()
frame2_pes_estudiante.frame=Frame(pestana_alumno)
frame2_pes_estudiante.frame.pack()

frame1_pes_materia=losframes()
frame1_pes_materia.frame=Frame(pestana_materia)
frame1_pes_materia.frame.pack()
frame2_pes_materia=losframes()
frame2_pes_materia.frame=Frame(pestana_materia)
frame2_pes_materia.frame.pack()

frame1_pes_prof=losframes()
frame1_pes_prof.frame=Frame(pestana_profesor)
frame1_pes_prof.frame.pack()
frame2_pes_prof=losframes()
frame2_pes_prof.frame=Frame(pestana_profesor)
frame2_pes_prof.frame.pack()


IDs=StringVar()

NOMBRE=StringVar()
APELLIDO=StringVar()
dni=StringVar()
DIRECCION=StringVar()
TELEFONO=StringVar()
REG_VALU=StringVar()
TEL_URG=StringVar()
ANO=StringVar()
MATERIA=StringVar()

#---------INSCRIPCION

Label(frame1_pes_ins.frame,text='NOMBRE:').grid(row=0,column=0)
Entry(frame1_pes_ins.frame,textvariable=NOMBRE).grid(row=0,column=1)
Label(frame1_pes_ins.frame,text='APELLIDO:').grid(row=1,column=0)
Entry(frame1_pes_ins.frame,textvariable=APELLIDO).grid(row=1,column=1)
Label(frame1_pes_ins.frame,text='DNI:').grid(row=2,column=0)
Entry(frame1_pes_ins.frame,textvariable=dni,state=DISABLED).grid(row=2,column=1)
Label(frame1_pes_ins.frame,text='REGULARIDAD:').grid(row=3,column=0)
Entry(frame1_pes_ins.frame,textvariable=REG_VALU,state=DISABLED).grid(row=3,column=1)
Label(frame1_pes_ins.frame,text='ANO:').grid(row=4,column=0)
Entry(frame1_pes_ins.frame,textvariable=ANO).grid(row=4,column=1)
Label(frame1_pes_ins.frame,text='MATERIA:').grid(row=5,column=0)
Entry(frame1_pes_ins.frame,textvariable=MATERIA).grid(row=5,column=1)


Button(frame2_pes_ins.frame,text='salir',command=salir).grid(row=0,column=0)
Button(frame2_pes_ins.frame,text='guardar',command=insert_INS).grid(row=0,column=1)


#----------AGREGAR ALUMNO 
Label(frame1_pes_estudiante.frame,text='NOMBRE:').grid(row=0,column=0)
Entry(frame1_pes_estudiante.frame,textvariable=NOMBRE).grid(row=0,column=1)
Label(frame1_pes_estudiante.frame,text='APELLIDO:').grid(row=1,column=0)
Entry(frame1_pes_estudiante.frame,textvariable=APELLIDO).grid(row=1,column=1)
Label(frame1_pes_estudiante.frame,text='DNI:').grid(row=2,column=0)
Entry(frame1_pes_estudiante.frame,textvariable=dni).grid(row=2,column=1)
Label(frame1_pes_estudiante.frame,text='DIRECCION').grid(row=3,column=0)
Entry(frame1_pes_estudiante.frame,textvariable=DIRECCION).grid(row=3,column=1)
Label(frame1_pes_estudiante.frame,text='TELEFONO:').grid(row=4,column=0)
Entry(frame1_pes_estudiante.frame,textvariable=TELEFONO).grid(row=4,column=1)
Label(frame1_pes_estudiante.frame,text='REGULARIDAD:').grid(row=5,column=0)
Checkbutton(frame1_pes_estudiante.frame, onvalue='Regular',offvalue='No regular', variable=REG_VALU).grid(row=5,column=1)
Label(frame1_pes_estudiante.frame,text='CONTACTO DE URGENCIA:').grid(row=6,column=0)
Entry(frame1_pes_estudiante.frame,textvariable=TEL_URG).grid(row=6,column=1)


Button(frame2_pes_estudiante.frame,text='salir',command=salir).grid(row=0,column=0)
Button(frame2_pes_estudiante.frame,text='guardar',command=insert_ALU).grid(row=0,column=1)



#-------------MATERIA

Label(frame1_pes_materia.frame,text='NOMBRE DE MATERIA:').grid(row=0,column=0)
Entry(frame1_pes_materia.frame,textvariable=MATERIA).grid(row=0,column=1)

Button(frame2_pes_materia.frame,text='salir',command=salir).grid(row=0,column=0)
Button(frame2_pes_materia.frame,text='guardar',command=insert_MATE).grid(row=0,column=1)


#------------PROFESORES

Label(frame1_pes_prof.frame,text='NOMBRE:').grid(row=0,column=0)
Entry(frame1_pes_prof.frame,textvariable=NOMBRE).grid(row=0,column=1)
Label(frame1_pes_prof.frame,text='APELLIDO:').grid(row=1,column=0)
Entry(frame1_pes_prof.frame,textvariable=APELLIDO).grid(row=1,column=1)
Label(frame1_pes_prof.frame,text='DNI:').grid(row=2,column=0)
Entry(frame1_pes_prof.frame,textvariable=dni).grid(row=2,column=1)
Label(frame1_pes_prof.frame,text='TELEFONO:').grid(row=4,column=0)
Entry(frame1_pes_prof.frame,textvariable=TELEFONO).grid(row=4,column=1)
Label(frame1_pes_prof.frame,text='DIRECCION').grid(row=3,column=0)
Entry(frame1_pes_prof.frame,textvariable=DIRECCION).grid(row=3,column=1)

Button(frame2_pes_prof.frame,text='salir',command=salir).grid(row=0,column=0)
Button(frame2_pes_prof.frame,text='guardar',command=insert_PROF).grid(row=0,column=1)



root.mainloop()