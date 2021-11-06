import smtplib



correo='correo'

mensaje="hola!" #NO PONER LOS DOS PUNTOS :


    

server=smtplib.SMTP('smtp.gmail.com',587) #sitio de mensajeria y puerto
server.starttls() #indicamos q usamos tls
server.login('correo','password') #logiamos con nuestra cuenta gmail
server.sendmail('correo',correo,mensaje)#quien envia y a donde con la variable del mensaje
server.quit() #cerramos la sesion
    
print('enviado')   

