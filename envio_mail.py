import smtplib



correo='maxiirucci@gmail.com'

mensaje="hola!" #NO PONER LOS DOS PUNTOS :


    

server=smtplib.SMTP('smtp.gmail.com',587) #sitio de mensajeria y puerto
server.starttls() #indicamos q usamos tls
server.login('maxiirucci@gmail.com','maxilo+10') #logiamos con nuestra cuenta gmail
server.sendmail('maxiirucci@gmail.com',correo,mensaje)#quien envia y a donde con la variable del mensaje
server.quit() #cerramos la sesion
    
print('enviado')   

