from Tkinter import* #importation des modules necessaires
from math import*
from time import*

#declaration des variables
x, y, ang, a, b, res, flag, e = 150., 30., pi, 150., 30., pi, 0, 0
def trace_horloge(): #fonction assurant la mise en place de l'horloge
    global x, y, ang, e, flag #definition des variables globales
    if flag == 0:
        flag = 1
        #mise en place des chiffres autour de l'horloge
        can.create_text(150, 20, text='12', fill='black')
        can.create_text(280, 150, text='3', fill='black')
        can.create_text(150, 280, text='6', fill='black')
        can.create_text(20, 150, text='9', fill='black')
        can.create_oval(145, 145, 155, 155, fill='black')
        aff_heure()
    ang = ang + 2*pi/60
    x, y = sin(ang), cos(ang)
    x, y = x*120 + 150, y*120 + 150
    if e == 59 or e == 14 or e == 29 or e == 44:
        can.create_oval(x-4, y-4, x+4, y+4, fill='black')
        root.after(25, trace_horloge)
    if e < 60:
        can.create_oval(x-2, y-2, x+2, y+2, fill='red')
        e = e+1
        root.after(25, trace_horloge)
def plus_deure():
    global voir
    a = can.create_text(220, 40, text='1', fill='black')
    b = can.create_text(265, 90, text='2', fill='black')
    c = can.create_text(265, 210, text='4', fill='black')
    d = can.create_text(220, 260, text='5', fill='black')
    e = can.create_text(80, 260, text='7', fill='black')
    f = can.create_text(30, 210, text='8', fill='black')
    g = can.create_text(30, 90, text='10', fill='black')
    h = can.create_text(80, 40, text='11', fill='black')
    encpldeur()

def encpldeur():
    txte.configure(text=str(strftime("%H:%M:%S", gmtime())))
    root.after(1000, encpldeur)



def aff_heure():
    global a, b , res
    he = localtime()
    ts = he[5]
    ti = ts+0.0
    tm = he[4]+ti/60
    th = he[3]+tm/60
    res = -(ts-30)*2*pi/60
    rem = -(tm-30)*2*pi/60
    reh = -(th-30)*2*pi/12
    a, b = sin(res), cos(res)
    c, d = sin(rem), cos(rem)
    e, f = sin(reh), cos(reh)
    a, b = a*120 + 150, b*120 + 150
    c, d = c*100 + 150, d*100 + 150
    e, f = e*80 + 150, f*80 + 150
    if flag > 0:
        can.coords(seconde, 150, 150, a, b)
        can.coords(minute, 150, 150, c, d)
        can.coords(heure, 150, 150, e, f)
        root.after(1000, aff_heure)
    
def quitter():
    global flag
    flag = 0
    root.quit()
    root.destroy()
        
def makemenu(win):
    top=Menu(win)
    win.config(menu=top)
    A=Menu(top)
    top.add_cascade(label="Affichage de l'heure !",menu=A,underline=0)
    A.add_command(label="Affichage de l'heure !",command=trace_horloge,underline=0)
    B=Menu(top)
    top.add_cascade(label="Affichage complet",menu=B, underline=0)
    B.add_command(label="Affichage complet",command=plus_deure,underline=0)
    Q=Menu(top)
    top.add_cascade(label='Quitter !',menu=Q,underline=0)
    Q.add_command(label='Quitter !',command=quitter,underline=0)


                                        ############ Programme principal #############
root = Tk()
root.title("L'horloge V.1 par Tony")
can = Canvas(root, width=300, height=300, bg='white', relief=SUNKEN)
can.pack()
seconde = can.create_line(10, 10, 10, 10, fill='red', arrow=LAST)
minute = can.create_line(10, 10, 10, 10, fill='black', arrow=LAST)
heure = can.create_line(10, 10, 10, 10, fill='blue', arrow=LAST)
txte = Label(root, text='', bg='white', width=30)
txte.pack()
makemenu(root)
root.mainloop()
