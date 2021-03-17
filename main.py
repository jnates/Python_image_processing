#Import libraries  
from tkinter import*
import cv2
import numpy as np

ventana1= Tk()
ventana1.title("FILTADO DE IMAGENES")
ventana1.resizable(False,False)
ventana1.iconbitmap("./img/electronic_5486.ico")

#Configuration to center interface
ventana_Width = ventana1.winfo_reqwidth()
ventana_Height = ventana1.winfo_reqheight()
posicion_Right = int(ventana_Width*3.5 - ventana_Width/3)
posicion_Down = int(ventana_Height - ventana_Height/2)
ventana1.geometry("+{}+{}".format(posicion_Right, posicion_Down))

#Create main frame (window)
frame = Frame(ventana1, width=600, height=500)
frame.pack()

logo_universidad = PhotoImage(file="./img/logo_u.png")
imagen_base = PhotoImage(file="./img/imagen_base2.png")

def Cerrar_Pestaña():
	ventana1.destroy()
	pass

def Ventana_Secundaria():
	#Create window 2 and communicate it with one using our Toplevel
	ventana2= Toplevel(ventana1)
	ventana2.title("FILTADO DE IMAGENES")
	ventana2.iconbitmap("./img/electronic_5486.ico")
	ventana2.resizable(False,False)

	#Configuration to center interface
	ventana_Width = ventana2.winfo_reqwidth()
	ventana_Height = ventana2.winfo_reqheight()
	posicion_Right = int(ventana_Width*3.5 - ventana_Width/3)
	posicion_Down = int(ventana_Height - ventana_Height/2)
	ventana2.geometry("+{}+{}".format(posicion_Right, posicion_Down))

	#Create the frame (visual screen 2)
	ventana2.transient(ventana1)
	frame2 = Frame(ventana2, width=600, height= 500)
	frame2.pack()

	def Cerrar_Pestaña2():
		ventana2.destroy()
		pass
	
	def Filtro1():
		#Read our image
		img = cv2.imread("./img/imagen_base2.png")
		#We create a variable where we apply the Gaussian filter and create a window
		blur_image = cv2.GaussianBlur(img, (7, 7), 1)
		cv2.imshow('Blur Image', blur_image)
		cv2.waitKey(1)
		pass

	def Filtro2():
		#Read our image
		img = cv2.imread("./img/imagen_base2.png")
		#Apply our canny filter and show it on screen
		edge_img = cv2.Canny(img, 100, 200)
		cv2.imshow("Detected Edges", edge_img)
		cv2.waitKey(1)
		pass

	def Filtro3():
		#Read our image
		img = cv2.imread("./img/imagen_base2.png")
		#Apply filter on grayscale and display on screen
		gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		cv2.imshow("Gray Scale Image", gray_img)
		cv2.waitKey(1)
		pass

	def Filtro4():
		#Read our image
		img = cv2.imread("./img/imagen_base2.png")
		contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
		cv2.imshow('Contrast Image', contrast_img)
		cv2.waitKey(1)
		pass

	def Filtro5():
		#Read our image
		img = cv2.imread("./img/imagen_base2.png")
		gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		retval, thresh = cv2.threshold(gray_img, 127, 255, 0)
		img_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(img, img_contours, -1, (0, 255, 0))
		cv2.imshow('Image Contours', img)
		cv2.waitKey(1)
		pass


	#We create variables and in these same we call and position photos or texts.
	logov2= Label(frame2, image=logo_universidad)
	logov2.place(x=20,y=10)

	imagen_base_full = Label(frame2, image=imagen_base)
	imagen_base_full.place(x=180,y=100)

	titulo_proyectov2 = Label(frame2, text="Proyecto Final: Filtrado de imágenes")
	titulo_proyectov2.place(x=220,y=40)

	Elaborado_por_v2 = Label(frame2, text="Elaborado por:")
	Elaborado_por_v2.place(x=430, y=420)

	Estudiantev2 = Label(frame2, text="Juan David Nates Huertas")
	Estudiantev2.place(x=430, y=440)

	Materiav2 = Label(frame2, text="Materia: Procesamiento digital de imágenes")
	Materiav2.place(x=30, y=440)

	Tipo_de_filtro = Label(frame2, text="Tipos de filtros")
	Tipo_de_filtro.place(x=260,y=330)

	#Exit button
	button_salirv2 = Button(ventana2,text="Volver", command=Cerrar_Pestaña2).place(x=400,y=390)
	#buttons called filtering
	button1 = Button(ventana2,text="Filtro 1",command= Filtro1).place(x=160,y=360)
	button2 = Button(ventana2,text="Filtro 2",command= Filtro2).place(x=220,y=360)
	button3 = Button(ventana2,text="Filtro 3",command= Filtro3).place(x=280,y=360)
	button4 = Button(ventana2,text="Filtro 4",command= Filtro4).place(x=340,y=360)
	button5 = Button(ventana2,text="Filtro 5",command= Filtro5).place(x=400,y=360)

#Variables are created and our photos and texts are called where it takes the position of each variable
logov1= Label(frame, image=logo_universidad)
logov1.place(x=20,y=10)

titulo_proyectov1 = Label(frame, text="Proyecto Final: Filtrado de imágenes")
titulo_proyectov1.place(x=220,y=40)

Elaborado_porv1 = Label(frame, text="Elaborado por:")
Elaborado_porv1.place(x=430, y=420)

Estudiantev1 = Label(frame, text="Juan David Nates Huertas")
Estudiantev1.place(x=430, y=440)

Materiav1 = Label(frame, text="Materia: Procesamiento digital de imágenes")
Materiav1.place(x=30, y=440)
		
#A button is created and the function to close tab is called
button_salir = Button (text="SALIR", command=Cerrar_Pestaña).place(x=440,y=340)
button_trabajo = Button(text="Procesamiento Imágenes",command=Ventana_Secundaria).place(x=220,y=240)

#Create our window
ventana1.mainloop()  	