
from Tkinter import*
import matplotlib.pyplot as plt

def do_nothing():
    global fr
    print (fr)


root = Tk()

root.geometry('450x200')


def myplot():
    global d
    plt.imshow(d['phase'][p, :, b, :].T, aspect='auto', interpolation='nearest')
   

# Crear el menu principal
main_menu = Menu(root)
root.config(menu = main_menu)

#create phase-amplitude menu
paMenu = Menu(main_menu)
main_menu.add_cascade(label = "PHA-AMP", menu = paMenu)

#create polarization menu
polMenu = Menu(main_menu)
main_menu.add_cascade(label = "POLARIZATION", menu = polMenu)

#create baseline menu
baseMenu = Menu(main_menu)
main_menu.add_cascade(label = "BASELINE", menu = baseMenu)

#create field menu
fieldMenu = Menu(main_menu)
main_menu.add_cascade(label = "FIELD", menu = fieldMenu)

#create spectral window menu
spwMenu = Menu(main_menu)
main_menu.add_cascade(label = "SPW", menu = spwMenu)

#create scan menu
scanMenu = Menu(main_menu)
main_menu.add_cascade(label = "SCAN", menu = scanMenu)

#create plotting option
plotMenu = Menu(main_menu)
main_menu.add_cascade(label = "PLOT", menu = plotMenu)

#plot menu
plot_menu = Menu(plotMenu)
plotMenu.add_command(label = "Plot this", command = myplot)


#phase-amplitude menu 
pamenu = Menu(paMenu)

pa=0
def pa0():
    global pa
    pa=0
    print("elvalorde", pa)
       
def pa1():
    global pa
    pa=1
    print("elvalorde", pa)

pamenu.add_command(label = "Phase", command = pa0)
pamenu.add_command(label = "Amplitude", command = pa1)
paMenu.add_cascade(label = "Phase-Amplitude", menu = pamenu)


#polarization menu 
polmenu = Menu(polMenu)

p=0
def p0():
    global p
    p=0
    print("elvalorde", p)
       
def p1():
    global p
    p=1
    print("elvalorde", p)
   
def p2():
    global p
    p=2
    print("elvalorde", p)

def p3():
    global p
    p=3
    print("elvalorde", p)

def p4():
    global p
    p=0,1,2,3
    print("elvalorde", p)

polmenu.add_command(label = "RR", command = p0)
polmenu.add_command(label = "LL", command = p1)
polmenu.add_command(label = "RL", command = p2)
polmenu.add_command(label = "LR", command = p3)
polmenu.add_command(label = "All", command = p4)
polMenu.add_cascade(label = "Polarization", menu = polmenu)


#baseline menu 
basemenu = Menu(baseMenu)

b=0
def b0():
    global b
    b=0
    print("elvalorde", b)
       
def b1():
    global b
    b=1
    print("elvalorde", b)
   
def b2():
    global b
    b=2
    print("elvalorde", b)

def b3():
    global b
    b=3
    print("elvalorde", b)

def b4():
    global b
    b=4
    print("elvalorde", b)

def b5():
    global b
    b=5
    print("elvalorde", b)
       
def b6():
    global b
    b=6
    print("elvalorde", b)
   
def b7():
    global b
    b=7
    print("elvalorde", b)

def b8():
    global b
    b=8
    print("elvalorde", b)

def b9():
    global b
    b=9
    print("elvalorde", b)

def b10():
    global b
    b=10
    print("elvalorde", b)

def b11():
    global b
    b=11
    print("elvalorde", b)
       
def b12():
    global b
    b=12
    print("elvalorde", b)
   
def b13():
    global b
    b=13
    print("elvalorde", b)

def b14():
    global b
    b=14
    print("elvalorde", b)

def b15():
    global b
    b=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
    print("elvalorde", b)

basemenu.add_command(label = "0", command = b0)
basemenu.add_command(label = "1", command = b1)
basemenu.add_command(label = "2", command = b2)
basemenu.add_command(label = "3", command = b3)
basemenu.add_command(label = "4", command = b4)
basemenu.add_command(label = "5", command = b5)
basemenu.add_command(label = "6", command = b6)
basemenu.add_command(label = "7", command = b7)
basemenu.add_command(label = "8", command = b8)
basemenu.add_command(label = "9", command = b9)
basemenu.add_command(label = "10", command = b10)
basemenu.add_command(label = "11", command = b11)
basemenu.add_command(label = "12", command = b12)
basemenu.add_command(label = "13", command = b13)
basemenu.add_command(label = "14", command = b14)
basemenu.add_command(label = "All", command = b15)
baseMenu.add_cascade(label = "Baselines", menu = basemenu)


#field menu 
fieldmenu = Menu(fieldMenu)

f=0
def f0():
    global f
    f=0
    print("elvalorde", f)
       
def f1():
    global f
    f=1
    print("elvalorde", f)
   
def f2():
    global f
    f=2
    print("elvalorde", f)

def f3():
    global f
    f=3
    print("elvalorde", f)

def f4():
    global f
    f=4
    print("elvalorde", f)

def f5():
    global f
    f=0,1,2,3,4
    print("elvalorde", f)

fieldmenu.add_command(label = "0", command = f0)
fieldmenu.add_command(label = "1", command = f1)
fieldmenu.add_command(label = "2", command = f2)
fieldmenu.add_command(label = "3", command = f3)
fieldmenu.add_command(label = "4", command = f4)
fieldmenu.add_command(label = "All", command = f5)
fieldMenu.add_cascade(label = "Fields", menu = fieldmenu)


#spectral window menu 
spwmenu = Menu(spwMenu)

s=0
def s0():
    global s
    s=0
    print("elvalorde", s)
       
def s1():
    global s
    s=1
    print("elvalorde", s)
   
def s2():
    global s
    s=2
    print("elvalorde", s)

def s3():
    global s
    s=3
    print("elvalorde", s)

def s4():
    global s
    s=0,1,2,3
    print("elvalorde", s)

spwmenu.add_command(label = "0", command = s0)
spwmenu.add_command(label = "1", command = s1)
spwmenu.add_command(label = "2", command = s2)
spwmenu.add_command(label = "3", command = s3)
spwmenu.add_command(label = "All", command = s4)
spwMenu.add_cascade(label = "Spectral windows", menu = spwmenu)


#scan menu 
scanmenu = Menu(scanMenu)

sc=0
def sc0():
    global sc
    sc=0
    print("elvalorde", sc)
       
def sc1():
    global sc
    sc=1
    print("elvalorde", sc)
   
def sc2():
    global sc
    sc=2
    print("elvalorde", sc)

def sc3():
    global sc
    sc=3
    print("elvalorde", sc)

def sc4():
    global sc
    sc=4
    print("elvalorde", sc)

def sc5():
    global sc
    sc=5
    print("elvalorde", sc)
       
def sc6():
    global sc
    sc=6
    print("elvalorde", sc)
   
def sc7():
    global sc
    sc=7
    print("elvalorde", sc)

def sc8():
    global sc
    sc=8
    print("elvalorde", sc)

def sc9():
    global sc
    sc=9
    print("elvalorde", sc)

def sc10():
    global sc
    b=10
    print("elvalorde", b)

def sc11():
    global sc
    b=0,1,2,3,4,5,6,7,8,9,10,

scanmenu.add_command(label = "0", command = sc0)
scanmenu.add_command(label = "1", command = sc1)
scanmenu.add_command(label = "2", command = sc2)
scanmenu.add_command(label = "3", command = sc3)
scanmenu.add_command(label = "4", command = sc4)
scanmenu.add_command(label = "5", command = sc5)
scanmenu.add_command(label = "6", command = sc6)
scanmenu.add_command(label = "7", command = sc7)
scanmenu.add_command(label = "8", command = sc8)
scanmenu.add_command(label = "9", command = sc9)
scanmenu.add_command(label = "10", command = sc10)
scanmenu.add_command(label = "All", command = sc11)
scanMenu.add_cascade(label = "Scan", menu = scanmenu)


# Show the menu
root.config(menu=main_menu)

# Show the window
root.mainloop()

ms.open ('3C277.1_avg.ms')
staql={'field':str(f), 'spw':str(s)}
ms.msselect (staql)
d=ms.getdata(['uvw', 'phase', 'time', 'field_id', 'axis_info', 'flag', 'data_desc_id', 'amplitude'], ifraxis=True)




 




