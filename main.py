from tkinter import *
from PIL import Image, ImageTk

janela = Tk()
janela.geometry("1280x720")
janela.title("Grafos 1 Projeto de Algoritmos")
janela.resizable(height=False, width=False)


mapa =  Image.open("assets/BRTBrasilia.png")
icon_no = Image.open("assets/square.png")

canvas = Canvas(janela, width=1280, height=720)
canvas.pack()

resized_image = mapa.resize((1280,720), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

canvas.create_image(0,0,anchor=NW, image=new_image)

resized_btn = icon_no.resize((30,30))
new_btn = ImageTk.PhotoImage(resized_btn)


def noB():
    print("B")

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=208,y=430, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=840,y=490, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=210,y=380, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=1195,y=33, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=340,y=520, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=335,y=680, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=495,y=690, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=620,y=465, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=580,y=400, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=695,y=330, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=585,y=310, anchor=NW)

botao = Button(janela, image=new_btn ,command=noB, bd=0, highlightthickness=0)
botao.pack()
botao.place(x=665,y=235, anchor=NW)

janela.mainloop()
