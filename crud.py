from tkinter import*
from tkinter import ttk
import tkinter as tk #modulo para tk.toplevel()
from tkinter import messagebox
import pymysql



def ws_delete():
    
    venta_del=tk.Toplevel(root) 

    frameWS_=Frame(venta_del)
    frameWS_.pack()
    frameWS_2=Frame(venta_del)
    frameWS_2.pack()

    Label(frameWS_,text='nombre de producto:').grid(row=0,column=0)
    Entry(frameWS_,textvariable=NOM_DEL).grid(row=0,column=1)
    Label(frameWS_,text='precio:').grid(row=1,column=0)
    Entry(frameWS_,textvariable=PRECIO_DEL).grid(row=1,column=1)

    Button(frameWS_2,text='delete',command=delete).grid(row=0,columnspan=2)

    venta_del.mainloop()
    
def delete(): #eliminar el registro en la bbdd
    global tv
    conn=pymysql.connect(user='root',passwd='',db='LISTADO')
    cursor=conn.cursor()
    resp=messagebox.askquestion('eliminar producto','Desea eliminar este producto?')
    
    if resp=='yes':
        cursor.execute("DELETE FROM PRODUCTOS WHERE PRODUCTOS.PRODUCTO= '"+NOM_DEL.get()+"' AND PRODUCTOS.PRECIO= '"+PRECIO_DEL.get()+"' " )
        conn.commit()
        NOM_DEL.set('')
        PRECIO_DEL.set('')
        messagebox.showinfo('eliminar producto','producto eliminado exitosamente!')
        tv.destroy()
        tv=ttk.Treeview(frame3,columns=(1,2), show='headings',height=8)
        tv.pack()
        tv.heading(1,text='producto')
        tv.heading(2,text='precio')

        conn=pymysql.connect(user='root',passwd='',db='LISTADO')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM PRODUCTOS")
        guarda_to=cursor.fetchall()

        try: #probar
            for i in guarda_to:
                tv.insert(parent='',index=0,values=(i))
            print(i)
        except:
            messagebox.showinfo('gestor productos','sin datos en la BBDD')
            

    
            

def insert(): #accion boton save
    global tv
    conn=pymysql.connect(user='root',passwd='',db='LISTADO')
    cursor=conn.cursor()
    resp=messagebox.askquestion('agregar producto','desea agregar este producto al listado?')
    if resp=='yes':
        cursor.execute("INSERT INTO PRODUCTOS VALUES('"+NOMBRE.get()+"','"+PRECIO.get()+"')")
        conn.commit()
        NOMBRE.set('')
        PRECIO.set('')
        messagebox.showinfo('agregar producto','producto agregado con exito!')
        
        #-------------------------------------------lo nuevo en cod
        tv.destroy()
        tv=ttk.Treeview(frame3,columns=(1,2), show='headings',height=8)
        tv.pack()
        tv.heading(1,text='producto')
        tv.heading(2,text='precio')

        conn=pymysql.connect(user='root',passwd='',db='LISTADO')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM PRODUCTOS")
        guarda_to=cursor.fetchall()

        for i in guarda_to:
            tv.insert(parent='',index=0,values=(i))
        print(i)


def ws_edit(): #ventana de edicion
     
    venta_edit=tk.Toplevel(root)
    frameWS=Frame(venta_edit)
    frameWS.pack()
    frameWS2=Frame(venta_edit)
    frameWS2.pack()

    Label(frameWS,text='nombre de producto:').grid(row=0,column=0)
    Entry(frameWS,textvariable=NOM_EDIT).grid(row=0,column=1)
    Label(frameWS,text='nuevo nombre:').grid(row=2,column=0)
    Entry(frameWS,textvariable=NEW_NOMBRE).grid(row=2,column=1)
    Label(frameWS,text='nuevo precio:').grid(row=3,column=0)
    Entry(frameWS,textvariable=NEW_PRECIO).grid(row=3,column=1)
    Button(frameWS2,text='Update',command=update).grid(row=0,columnspan=2)

    venta_edit.mainloop()


def update():
    global tv
    conn=pymysql.connect(user='root',passwd='',db='LISTADO')
    cursor=conn.cursor()
    resp=messagebox.askquestion('actualizar datos','desea actualizar estos datos?')
    if resp=='yes':
        cursor.execute("UPDATE PRODUCTOS SET PRODUCTO= '"+NEW_NOMBRE.get()+"' ,PRECIO= '"+NEW_PRECIO.get()+"' WHERE PRODUCTOS.PRODUCTO='"+NOM_EDIT.get()+"' ")
        conn.commit()
        NEW_NOMBRE.set('')
        NEW_PRECIO.set('')
        NOM_EDIT.set('')
        messagebox.showinfo("actualizar datos",'datos actualizados exitosamente!')
        tv.destroy()
        tv=ttk.Treeview(frame3,columns=(1,2), show='headings',height=8)
        tv.pack()
        tv.heading(1,text='producto')
        tv.heading(2,text='precio')

        conn=pymysql.connect(user='root',passwd='',db='LISTADO')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM PRODUCTOS")
        guarda_to=cursor.fetchall()

        for i in guarda_to:
            tv.insert(parent='',index=0,values=(i))
        print(i)
        #ver como destruir ventana emergente

#venta_del=tk.Toplevel


root=tk.Tk()
root.geometry('500x500')
root.title('Gestor de productos')
venta_del=tk.Toplevel #ventanas nuevas 
conn=pymysql.connect(user='root',passwd='',db='LISTADO')
cursor=conn.cursor()
cursor.execute("SELECT * FROM PRODUCTOS")
guarda_to=cursor.fetchall()

frame0=Frame(root)
frame0.pack()
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()
frame3=Frame(root)
frame3.pack()
frame4=Frame(root)
frame4.pack()
#-------------------------------variables entry
#INSERT
NOMBRE=StringVar()
PRECIO=StringVar()
#UP
NOM_EDIT=StringVar()
NEW_NOMBRE=StringVar()
NEW_PRECIO=StringVar()
#DEL
NOM_DEL=StringVar()
PRECIO_DEL=StringVar()

Label(frame0,text='registrar nuevo producto:').grid(row=0,column=0)
Label(frame1,text='nombre').grid(row=1,column=0)
Entry(frame1,textvariable=NOMBRE).grid(row=1,column=1)
Label(frame1,text='precio').grid(row=2,column=0)
Entry(frame1,textvariable=PRECIO).grid(row=2,column=1)

tv=ttk.Treeview(frame3,columns=(1,2), show='headings',height=8)
tv.pack()
tv.heading(1,text='producto')
tv.heading(2,text='precio')

#visor al iniciar
for i in guarda_to:
    tv.insert(parent='',index=0,values=(i))
    print(i)

Button(frame2,text='Save',width=20,height=1,command=insert).grid(row=0,columnspan=2)
Button(frame4,text='delete',width=22,height=2,command=ws_delete).grid(row=0,column=0)
Button(frame4,text='edit',width=22,height=2,command=ws_edit).grid(row=0,column=1)

root.mainloop()

#si la consulta sql no se ejecuta en nueva ventana puede estar mal la ventana emergente
#agregar sus propias variables a los crud
