
#caracteristicas de ventana
from tkinter import *
ventana = Tk()
fondo = Tk
ventana.geometry('500x400')
Label(text='Hola bienvenido a Tramites y cambios RC', font='Arial*50',  fg='blue4').pack()
Label(text=" Remesas o Entretenimiento?", font='Arial', fg="blue4").pack()

fondo.configure(ventana,bg='Blue')

#variables
pregunta_netflix = Label(text=" Netflix o disney ?", font='Arial', fg="blue4")

pregunta_remesas = Label(text=" Banesco, provincial o venezuela ?", font='Arial', fg="blue4")

boton_aceptar = Label(text='Gracias por ingresar los datos', fg='blue4', font='Arial')

#x

def Remesas():
    Label(text=" Netflix o disney ?", font='Arial', fg="blue4")
    pregunta_remesas.place(x=120, y=180)




def entretenimiento():
    Label(text=" Netflix o disney ?", font='Arial', fg="blue4")
    pregunta_netflix.place(x=180, y=180)


def Aceptar():
    Label(text="Gracias por ingresar los datos", font='Arial', fg="blue4")
    boton_aceptar.place(x=140, y=180)



#botones



boton1 = Button(ventana,text='Remesas', fg="blue4", font='Arial', command=Remesas)
boton1.place(x=100, y=80)

boton2 = Button(ventana, text='Entretenimiento', fg="blue4",  font='Arial', command=entretenimiento)
boton2.place(x=250, y=80)

boton_aceptar = Button(ventana, text='Aceptar', fg='blue4', font='Arial', command=Aceptar)
boton_aceptar.place(x=200, y=280)




#variables
pregunta_netflix = Label(text=" Netflix o disney ?", font='Arial', fg="blue4")

pregunta_remesas = Label(text=" Banesco, provincial o venezuela ?", font='Arial', fg="blue4")

boton_aceptar = Label(text='Gracias por ingresar los datos', fg='blue4', font='Arial')








#venatana_para_escribir_datos

caja_de_texto = Entry(ventana)
caja_de_texto.place(x=170, y=250)
caja_de_texto.configure(fg='blue4')







mainloop()