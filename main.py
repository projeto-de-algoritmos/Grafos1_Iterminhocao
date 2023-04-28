from tkinter import *
from PIL import Image, ImageTk
from funcoes import *



#teste(); 


janela = Tk()
janela.geometry("1280x720")
janela.title("Grafos 1 Projeto de Algoritmos")
janela.resizable(height=False, width=False)


mapa =  Image.open("assets/BRTBrasilia.png")
img_no = Image.open("assets/square.png")
img_no_selecionado = Image.open("assets/greensquare.png")

canvas = Canvas(janela, width=1280, height=720)
canvas.pack()


resized_image = mapa.resize((1280,720), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

canvas.create_image(0,0,anchor=NW, image=new_image)

resized_btn = img_no.resize((30,30))
btn_no = ImageTk.PhotoImage(resized_btn)

resized_green_btn = img_no_selecionado.resize((30,30))
btn_select = ImageTk.PhotoImage(resized_green_btn)
x = canvas.create_line(710,340,640,480, fill="red", width=4)
nos = []

def noA(z, k):
    print("A")
    
    k.config(image=btn_select)
    if 'A' in nos:
        k.config(image=btn_no)
        nos.remove('A')
        x = canvas.create_line(710,340,640,480, fill="red", width=4)
    else:
        nos.append('A')
        x = canvas.create_line(710,340,640,480, fill="green", width=4)

def noB():
    print("B")
    print(nos)  

botaoA = Button(janela, image=btn_no,command=lambda: noA(x, botaoA), bd=0, highlightthickness=0)
botaoA.pack()
botaoA.place(x=208,y=430, anchor=NW)

botaoB = Button(janela, image=btn_no,command=lambda: noA(x, botaoB), bd=0, highlightthickness=0)
botaoB.pack()
botaoB.place(x=840,y=490, anchor=NW)

botaoC = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoC.pack()
botaoC.place(x=210,y=380, anchor=NW)

botaoD = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoD.pack()
botaoD.place(x=1195,y=33, anchor=NW)

botaoE = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoE.pack()
botaoE.place(x=340,y=520, anchor=NW)

botaoF = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoF.pack()
botaoF.place(x=335,y=680, anchor=NW)

botaoG = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoG.pack()
botaoG.place(x=495,y=690, anchor=NW)

botaoH = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoH.pack()
botaoH.place(x=620,y=465, anchor=NW)

botaoI = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoI.pack()
botaoI.place(x=580,y=400, anchor=NW)

botaoJ = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoJ.pack()
botaoJ.place(x=695,y=330, anchor=NW)

botaoK = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoK.pack()
botaoK.place(x=665,y=235, anchor=NW)

botaoL = Button(janela, image=btn_no,command=noB, bd=0, highlightthickness=0)
botaoL.pack()
botaoL.place(x=585,y=310, anchor=NW)

janela.mainloop()
