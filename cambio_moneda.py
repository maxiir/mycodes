import requests
from tkinter import*
from tkinter import ttk

root=Tk()
root.title('cambio de moneda')
root.config(bg='#4EB9E0')
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()
frame2.config(bg='#4EB9E0')
frame3=Frame(root)
frame3.pack()
frame3.config(bg='#4EB9E0')


def cerrar():
    root.destroy()


def consultar():
    
    APIKEY='8790|cwZ*kA11QHfGDgZhLcybDJjAWSBxBWQG'
    URL='https://api.cambio.today/v1/quotes/'+DE.get()+'/'+A.get()+'/json?quantity='+MONTO.get()+'&key='+APIKEY+''
    response=requests.get(URL)
    datos=response.json()
    #print(datos)

    actualizacion=datos['result']['updated']
    cambio=datos['result']['amount']

    ACTUALIZADO.set(actualizacion)
    CAMBIO.set(cambio)


DE=StringVar()
A=StringVar()
MONTO=StringVar()
CAMBIO=StringVar()
ACTUALIZADO=StringVar()

Label(frame1,text='cambio de divisas',font=('Courier',20,'italic'),bg='#4EB9E0').grid(row=0,column=0)

Label(frame2,text='Cambiar De:',font=('Courier',15,'italic'),bg='#4EB9E0').grid(row=0,column=0)
Entry(frame2,textvariable=DE).grid(row=0,column=1)
#box=ttk.Combobox(frame2).grid(row=0,column=1)
#box.place(x=50,y=100) #tamano
#box['values']='USD','ARS'
#box.current(0)

Label(frame2,text='A:',font=('Courier',15,'italic'),bg='#4EB9E0').grid(row=1,column=0)
Entry(frame2,textvariable=A).grid(row=1,column=1)

Label(frame2,text='Monto:',font=('Courier',15,'italic'),bg='#4EB9E0').grid(row=2,column=0)
Entry(frame2,textvariable=MONTO).grid(row=2,column=1)

Label(frame2,text='Cambio:',font=('Courier',15,'italic'),bg='#4EB9E0').grid(row=3,column=0)
Entry(frame2,textvariable=CAMBIO,state='disabled').grid(row=3,column=1)

Label(frame2,text='Actualizacion:',font=('Courier',15,'italic'),bg='#4EB9E0').grid(row=4,column=0)
Entry(frame2,textvariable=ACTUALIZADO,state='disabled').grid(row=4,column=1)


Button(frame3,text='Aceptar',command=consultar).grid(row=0,column=0)
Button(frame3,text='Salir',command=cerrar).grid(row=1,column=0)





root.mainloop()