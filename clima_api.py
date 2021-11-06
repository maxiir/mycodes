import requests
from tkinter import*

#APIKEY='16a1fdb80bc9fc4e97983c0ff4297a8d'

root=Tk()
root.title('APP de clima')

frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()

root.geometry('500x600')



def clima():
    APIKEY='16a1fdb80bc9fc4e97983c0ff4297a8d'
    URL='https://api.openweathermap.org/data/2.5/weather'
    parametros={"APPID":APIKEY,'q':LOCALIDAD.get(),'units':'metric','lang':'es'} # si ingresas la funcion ya con un atributo aparece instantaneamente en el programa sin usar el boton
    #lang 'es' para q este en espanol
    response= requests.get(URL,params=parametros)
    el_clima=response.json() #meto en variable el formato json
    print(el_clima)
    
    city=el_clima['name']
    temp_act=el_clima['main']['temp']
    speed_wind=el_clima['wind']['speed']
    cielo=el_clima['weather'][0]['description']
    temp_min=el_clima['main']['temp_min']
    temp_max=el_clima['main']['temp_max']
    humedad=el_clima['main']['humidity']
    lon=el_clima['coord']['lon']
    lat=el_clima['coord']['lat']
    visibility=el_clima['visibility']
    presion=el_clima['main']['pressure']


    #print(city,'\n',temp_act,'\n',speed_wind,'\n',cielo)


    CIUDAD.set(city)
    TEMP_ACTUAL.set(temp_act)
    TEMP_MIN.set(temp_min)
    TEMP_MAX.set(temp_max)
    VEL_ACTUAL.set(speed_wind)
    CIELO.set(cielo)
    HUMEDAD.set(humedad)
    PRESION.set(presion)
    VISIBILIDAD.set(visibility)
    LONGITUD.set(lon)
    LATITUD.set(lat)


def borrar():
    
    CIUDAD.set('')
    TEMP_ACTUAL.set('')
    TEMP_MIN.set('')
    TEMP_MAX.set('')
    VEL_ACTUAL.set('')
    CIELO.set('')
    HUMEDAD.set('')
    PRESION.set('')
    VISIBILIDAD.set('')
    LONGITUD.set('')
    LATITUD.set('')

LOCALIDAD=StringVar()

CIUDAD=StringVar()
TEMP_ACTUAL=StringVar()
TEMP_MIN=StringVar()
TEMP_MAX=StringVar()
VEL_ACTUAL=StringVar()
CIELO=StringVar()
HUMEDAD=StringVar()
PRESION=StringVar()
VISIBILIDAD=StringVar()
LONGITUD=StringVar()
LATITUD=StringVar()


Label(frame1,text='ingrese la localidad:').grid(row=0,column=0)
Entry(frame1,textvariable=LOCALIDAD).grid(row=0,column=1)

Label(frame1,text='ciudad:').grid(row=1,column=0)
Entry(frame1,textvariable=CIUDAD,font=('Courier',20,'normal')).grid(row=1,column=1)

Label(frame1,text='temperatura actual:').grid(row=2,column=0)
Entry(frame1,textvariable=TEMP_ACTUAL,font=('Courier',20,'normal')).grid(row=2,column=1)


Label(frame1,text='temperatura minima:').grid(row=3,column=0)
Entry(frame1,textvariable=TEMP_MIN,font=('Courier',20,'normal')).grid(row=3,column=1)

Label(frame1,text='temperatura maxima:').grid(row=4,column=0)
Entry(frame1,textvariable=TEMP_MAX,font=('Courier',20,'normal')).grid(row=4,column=1)

Label(frame1,text='velocidad del viento:').grid(row=5,column=0)
Entry(frame1,textvariable=VEL_ACTUAL,font=('Courier',20,'normal')).grid(row=5,column=1)

Label(frame1,text='cielo:').grid(row=6,column=0)
Entry(frame1,textvariable=CIELO,font=('Courier',20,'normal')).grid(row=6,column=1)

Label(frame1,text='humedad:').grid(row=7,column=0)
Entry(frame1,textvariable=HUMEDAD,font=('Courier',20,'normal')).grid(row=7,column=1)

Label(frame1,text='visibilidad:').grid(row=8,column=0)
Entry(frame1,textvariable=VISIBILIDAD,font=('Courier',20,'normal')).grid(row=8,column=1)

Label(frame1,text='presion:').grid(row=9,column=0)
Entry(frame1,textvariable=PRESION,font=('Courier',20,'normal')).grid(row=9,column=1)

Label(frame1,text='latitud:').grid(row=10,column=0)
Entry(frame1,textvariable=LATITUD,font=('Courier',20,'normal')).grid(row=10,column=1)

Label(frame1,text='longitud:').grid(row=11,column=0)
Entry(frame1,textvariable=LONGITUD,font=('Courier',20,'normal')).grid(row=11,column=1)


boton1=Button(frame2,text='aceptar',command=clima).grid(row=0,column=0)
boton2=Button(frame2,text='borrar',command=borrar).grid(row=1,column=0)


root.mainloop()
