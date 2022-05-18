import tkinter
from turtle import left

def NovoArquivo():
    area_de_texto.delete(1.0, 'end')
def SalvaArquivo():
    container = area_de_texto.get(1.0, 'end')
    arquivo = open('notepad.txt','w')
    arquivo.write(container)
    arquivo.close

def Abrir():
    arquivo = open('notepad.txt','r')
    container = arquivo.read()
    area_de_texto.insert(1.0, container)

def Atualizar():
   tipo = barrinha.get()
   size = spin_size.get()
   area_de_texto.config(font='{} {}'.format(tipo, size)) 

janela = tkinter.Tk()
janela.title("Notepad")
janela.geometry("1024x480")

barra = tkinter.Frame(janela, height=30)
barra.pack(fill='x')
fonte_texto = tkinter.Label(barra,text=' Font: ')
fonte_texto.pack(side='left')

barrinha = tkinter.Spinbox(barra, values=("Arial","Verdana"))
barrinha.pack(side='left')

tamanho_fonte = tkinter.Label(barra, text=" Tamanho da Fonte: ")
tamanho_fonte.pack(side='left')

spin_size = tkinter.Spinbox(barra, from_=0, to=60)
spin_size.pack(side='left')

button_update = tkinter.Button(barra, text='Aplicar', command=Atualizar)
button_update.pack(side='left')

area_de_texto = tkinter.Text(janela, font="Arial 20 bold", width=1280,height=720)
area_de_texto.pack()

main_menu = tkinter.Menu(janela)

arquivo_menu = tkinter.Menu(main_menu,tearoff=0)
arquivo_menu.add_command(label='Novo', command=NovoArquivo)
arquivo_menu.add_command(label='Salvar', command=SalvaArquivo)
arquivo_menu.add_command(label='Abrir',command=Abrir)
arquivo_menu.add_command(label='Sair', command=janela.quit)

main_menu.add_cascade(label='Arquivo', menu=arquivo_menu)

janela.config(menu=main_menu)

janela.mainloop()
