
from tkinter import * #importamos módulo tkinter
import sqlite3 # para conectarnos a la base de datos
from tkinter import messagebox #importamos cuadro de diálogo

#Nombre del módulo: My_CurrencyAPP.py
#Fecha de creación del módulo: 3/01/2022
#autor del modulo: Celia Gómez
#Historial de modificaciones: 20/01/2022
#Sinopsis del módulo sobre lo que hace el módulo: 
# Se trata de una aplicación que te permite realizar cambio de divisas entre euros, dolares americanos y libra esterlina.
#Para acceder al servicio es necesario registrarse con un usuario y contraseña y para ello tienes que registrarte.
#Diferentes funciones admitidas en el módulo junto con sus parámetros de entrada y salida:
#Variables globales accedidas o modificadas por el módulo:


class APP(Frame):#almacenamos la app en un frame
    ##Creamos el constructor
    def __init__(self, master=None): ##Master es el contenedor donde vamos a guardar el frame
        super().__init__(master)#super().__init__ permite evitar referirse explícitamente a la clase base
        self.ventana() #llamamos a la función de la ventana para que luego se ejecute
    
    def ventana(self): #hacemos la funcion de la primera ventana(ventana inicio)
        #Definimos el titulo de la primera ventana y su tamaño
        ventana1.title("Currency APP")
        ventana1.geometry("350x500+500+50")

        #añadimos una etiqueta, e indicamos texto y fuente de texto
        label1= Label(ventana1, text=("Bienvennido a My CurrencyAPP"), font = ("Courir", 22, "italic"))
        label1.grid(row=1,column=1, padx=20, pady=20)# indicamos su posicion.

        ##añadimos entradas para la ventana 1 del usuario
        ##ETIQUETA IMAGEN con emoji

        self.img_1=PhotoImage(file='/Users/celiagomez/programming/emoji1.png')#copiamos ruta de aceso dela imagen
        imagen= Label(ventana1,image=self.img_1)#la alamcenamos en un label
        imagen.grid(row=2, column=1, pady=15)

        #añadimos una etiqueta para el usuario, e indicamos texto y fuente de texto y su posición
        label_usuario= Label(ventana1, text= ("Usuario"),font = ("Courir", 14))
        label_usuario.grid(row=3, column=1)

        #añadimos entradas para el usuario e indicamos posición
        entry_usuario= Entry(ventana1)
        entry_usuario.grid(row=4, column=1, pady=10)
     
        #añadimos una etiqueta para la contraseña, e indicamos texto y fuente de texto y su posición
        label_contraseña= Label(ventana1, text= ("Contraseña"),font = ("Courir", 14))
        label_contraseña.grid(row=5, column=1)
        #añadimos entradas para la contraseña e indicamos posición
        entry_contraseña= Entry(ventana1)
        entry_contraseña.grid(row=6, column=1, pady=10)
        entry_contraseña.config(show=("*"))#para que al escribir la contraseña apareza *
        #etiqueta para registarse
        label_registro= Label(ventana1, text="¿No estás registrado?", font=("Courir", 15))
        label_registro.grid(row=15, column=1)
        
        db=sqlite3.connect("/Users/celiagomez/programming/log.db") # nos conectamos a la base de datos 
        cursor= db.cursor() #creamos un cursor
        
        #función para hacer el login
        def login():
            #creamos unas variables
            passw= entry_contraseña.get() #.get es un método para recuperar los datos
            user=entry_usuario.get()
            #selecionamos de la tabla los datos insertados
            cursor.execute("SELECT * FROM registro WHERE usuario= ? AND contraseña=? ", (user, passw)) 
            #devuelve cada valor de la tabla
            if cursor.fetchall(): #creamos una condición con una excepción
                try:
                    messagebox.showinfo('info', 'Login Exitoso') #si los datos son correctos aparece ese mensaje y abre la otra ventana
                    abrirventana() 
                except Exception as ex: #si hay algún error lo imprime en la terminal
                    print(ex)
            else:
                if user=="" and passw=="": #para verificar si los datos están vacios
                    messagebox.showerror('error','Introduzca los datos')
                else:
                    messagebox.showerror('error','Login Incorrecto') #si los datos son incorrectos aparece ese mensaje 
        
        #boton que realiza la funcion del login
        boton=Button(ventana1,text='Entrar', command=login)
        boton.grid(row=7, column=1, pady=15)

        ##creamos la segunda ventana
        def  abrirventana():
            ventana1.withdraw() #withdraw se utiliza para cerrar la ventana anterior
            currency_ven=Toplevel()# VENTANA HIJA DE LA PRINCIPAL
            currency_ven.geometry("350x500+500+50")# definimos el tamaño de la ventana
            currency_ven.title("Currency APP")# definimos el título de la ventana

            #añadimos otra etiqueta para definir el título de la primera ventana
            etiqueta_ven=Label(currency_ven, text=" My CurrencyAPP")
            etiqueta_ven.config(font=("Courir",22,"italic"))
            etiqueta_ven.grid(row=1,column=1, padx=87,pady=40)#pad- sirven para definir los margenes internos de la etiqueta

            ###ETIQUETAS DEL CONVERSOR 
            label1= Label(currency_ven,text="Cantidad" )
            label2= Label(currency_ven,text="De" )
            label3= Label(currency_ven,text="A" )
            label4=Label(currency_ven, text="Resultado ")

            ##entradas para el importe de la cantidad y  para la salida del resultado
            importe= Entry(currency_ven)
            resultado=Entry(currency_ven)

            ##posicón de las anteriores etiquetas y entradas
            label1.grid(row= 2, column=1)
            label2.grid(row=4, column=1)
            label3.grid(row=6, column=1)
            label4.grid(row= 8, column=1)
            importe.grid(row= 3, column=1)
            resultado.grid(row= 9, column=1)

            def cerrar_app():
                try:
                    cerrar=currency_ven.destroy()
                    messagebox.showinfo('info', 'Se ha cerrado la app con éxito')
                except:
                    messagebox.showerror('ERROR', 'No se ha podido cerrar')
            
            ##BOTON CERRAR APP
            boton2=Button(currency_ven,text= 'Cerrar APP', command= cerrar_app)
            #con el comando y.destroy indicamos que al presionar el bóton se cierre la ventana
            boton2.grid(row=15,column=1, columnspan=1, sticky=W+E, pady=65)

            #variables permite meter o visualizar una línea de texto simple e indicamos la ventana en la que esta
            variable1=StringVar(currency_ven)
            variable2=StringVar(currency_ven)

            #creamos una lista para guardar los distintos datos
            lista_divisas = ["EUR", "USD", "GBP"] 
            # optionmenu nos permite crear un menu despegable 
            de_divisa= OptionMenu(currency_ven, variable1, *lista_divisas) 
            a_divisa = OptionMenu(currency_ven, variable2, *lista_divisas) 
            #indicamos la posición de los menus
            de_divisa.grid(row = 5, column = 1) 
            a_divisa.grid(row = 7, column = 1)
            
            #creamos la funcion que va a permitir hacer las operaciones
            def convertir():
                ##EURO A DOLAR
                if variable1.get()=='EUR': #con una condicional decimos igualamos variable1 con la primera opción del menu
                    n1=importe.get() #almacenamos el primer valor importado 
                    if variable2.get()=='USD':# igualamos variable2 a ese dato
                        try:                  #para prevenir errores utilizamos excepciones
                            n2=1.14           # definimos el segundo valor
                            m= float(n1)*float(n2) #definimos la operación de esta conversion
                            resultado.insert(0,m)# insertamos ese dato en la entrada del resultado
                        except:
                            messagebox.showerror('info', 'Algo va mal...') ##si algún valor esta mal, aparece este mensaje
                #DOLAR A EURO
                if variable1.get()=='USD':
                    n3=importe.get()
                    if variable2.get()=='EUR':
                        try:
                            n4=1.14
                            r= float(n3)/ float(n4)
                            resultado.insert(0,r)
                        except:
                            messagebox.showerror('info', 'Algo va mal...')
                #EURO A LIBRA
                if variable1.get()=='EUR':
                    n5=importe.get()
                    if variable2.get()=='GBP':
                        try:
                            n6=1.1958
                            l= float(n5)/float(n6)
                            resultado.insert(0,l)
                        except:
                            messagebox.showerror('info', 'Algo va mal...')   
                #LIBRA A EURO
                if variable1.get()=='GBP':
                    n7=importe.get()
                    if variable2.get()=='EUR':
                        try:
                            n8=1.1958
                            h= float(n7)*float(n8)
                            resultado.insert(0,h)
                        except:
                            messagebox.showerror('info', 'Algo va mal...')
                #DOLAR A LIBRA
                if variable1.get()=='USD':
                    n9=importe.get()
                    if variable2.get()=='GBP':
                        try:
                            n10=0.74
                            r= float(n9)* float(n10)
                            resultado.insert(0,r)
                        except:
                            messagebox.showerror('info', 'Algo va mal...')
                ##LIBRA A DOLAR
                if variable1.get()=='GBP':
                    n11=importe.get()
                    if variable2.get()=='USD':
                        try:                         
                            n12=0.74
                            r= float(n11)/ float(n12)
                            resultado.insert(0,r)
                        except:
                            messagebox.showerror('info', 'Algo va mal...')
                ####CORRECION DE ERRORES
                if variable1.get()=='EUR':#con una condicional decimos igualamos variable1 con la primera opción del menu
                    n13=importe.get() #almacenamos el primer valor importado 
                    if variable2.get()=='EUR': #igualamos variable2 a ese dato
                        try:
                            s= str("Es el mismo valor!") #Como es el mismo valor añadimos ese mensaje
                            resultado.insert(0,s) # insertamos ese dato en la entrada del resultado
                        except:
                            messagebox.showerror('info', 'Algo va mal...')#igualmente prevenimos de errores
                if variable1.get()=='USD':
                    n14=importe.get()
                    if variable2.get()=='USD':
                        try:
                            y= str("Es el mismo valor!")
                            resultado.insert(0,y)
                        except:
                            messagebox.showerror('info', 'Algo va mal...')
                if variable1.get()=='GBP':
                    n15=importe.get()
                    if variable2.get()=='GBP':
                        try:
                            j= str("Es el mismo valor!")
                            resultado.insert(0,j)
                        except:
                            messagebox.showerror('info', 'Algo va mal...')
            #esta metodo sirve para borrar todos los datos a través del botón 
            
            def boton_borrar():
                importe.delete(0, END)
                resultado.delete(0,END)
            #boton para convertir
            boton_convertir=Button(currency_ven, text="Convertir", command=convertir) #el comando es el de la funcion converir
            boton_convertir.grid(row=11, column=1, pady=10)
            #boton para borrar
            btn_borrar=Button(currency_ven, text="Borrar", command=boton_borrar)# comando de la anterior funcion
            btn_borrar.grid(row=12, column=1)


        #ventana para registrarse
        def ventana2():
            ventana_2=Toplevel()# ventaja hija 
            ventana_2.title("Registro") #título ventana
            ventana_2.geometry("350x500+500+50") #tamaño ventana
            
            #etiqueta principal
            label3=Label(ventana_2,text="✨Login✨",font=("Courir",22))
            label3.grid(row=1, column=1, padx=120, pady=40)

            #etiquetas y entradas de la ventana
            registro_nombre=Label(ventana_2, text= "Nombre",font=("Courir"))
            registro_nombre.grid(row=2, column=1, pady=10)

            entry_nombre= Entry(ventana_2)
            entry_nombre.grid(row=3, column=1)

            registro_user=Label(ventana_2, text= "Usuario",font=("Courir"))
            registro_user.grid(row=4, column=1, pady=10)

            entry_user= Entry(ventana_2)
            entry_user.grid(row=5, column=1)

            registro_contra=Label(ventana_2, text= "Contraseña",font=("Courir"))
            registro_contra.grid(row=6, column=1, pady=10)

            entry_contra= Entry(ventana_2, show=("*"))
            entry_contra.grid(row=7, column=1)

            registro_contra2=Label(ventana_2, text= "Repita la contraseña",font=("Courir"))
            registro_contra2.grid(row=8, column=1, pady=10)

            entry_contra2= Entry(ventana_2, show=("*"))
            entry_contra2.grid(row=9, column=1)

            #crear la funcion para el registro
            def nuevo_user():
                
                nombre= entry_nombre.get()
                usuario= entry_user.get()
                contraseña= entry_contra.get()
                contraseña2=entry_contra2.get()

                if contraseña != contraseña2: #si las contraseñas no coinciden monstrar ese mensaje
                    messagebox.showerror('ERROR', 'Las contraseñas no coinciden')
                else: #comprobar que los campos no estén vacíos
                    if nombre == "" and usuario == "" and contraseña == "" and contraseña2 == "":
                        messagebox.showerror('ERROR', 'Rellene los campos')
                    else:
                        if usuario=="":
                            messagebox.showerror('ERROR', 'Complete el usuario')
                        else:
                            if contraseña=="":
                                 messagebox.showerror('ERROR', 'Complete la contraseña')
                            else:
                                if nombre=="":
                                    messagebox.showerror('ERROR', 'Complete el nombre')
                                else:
                                    try:
                                        cursor.execute ("INSERT INTO registro VALUES (\'"+usuario+"\',\'"+contraseña+"')")
                                        db.commit()	#Confirmamos los datos
                                        messagebox.showinfo("Registro Correcto","Hola "+nombre+", \n ¡Bienvenid@!.")
                                        ventana_2.destroy() #una vez aparezca el mensaje la ventana desaparece
                                    except:
                                        messagebox.showerror('ERROR', 'Ese usuario ya existe')####Si nos da un error en la base de datos, es porque el usuario ya esta registrado.
                            
                
                        
            #boton que realiza la anterior función
            buttons=Button(ventana_2,text="Registrar",command=nuevo_user)
            buttons.grid(row=10, column= 1, sticky=W + E, pady=15)

        #bton de la primera ventana con la funcion de abrir la ventana de registro
        boton_reg= Button(ventana1, text="Registrate!!",font=("Courir"), command= ventana2)
        boton_reg.grid(row=16, column=1, pady= 5)
            


if __name__=='__main__': #implica que el módulo está siendo ejecutado de forma independiente por el usuario 
    ventana1= Tk() #creamos la ventana Tk
    app= APP(ventana1) #todo esta almaceado en una clase Frame 
    app.mainloop()# sirve para ejecutar toda la app

        