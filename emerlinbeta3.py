
from Tkinter import *
import matplotlib.pyplot as plt

ms.open ('/Volumes/NO NAME/POWERWALL/3C277.1_avg.ms')
staql={'field':'0', 'spw':'0'}
ms.msselect (staql)
d=ms.getdata(['uvw', 'phase', 'time', 'field_id', 'axis_info', 'flag', 'data_desc_id', 'amplitude'], ifraxis=True)

def myplot():
    global d
    plt.imshow(d['phase'][p, :, b, :].T, aspect='auto', interpolation='nearest')

def do_nothing():
    global fr
    print (fr)



root = Tk()





# Crear el menu principal
main_menu = Menu(root)
root.config(menu = main_menu)

#create xaxis menu
xaxisMenu = Menu(main_menu)
main_menu.add_cascade(label = "X-AXIS", menu = xaxisMenu)

#create yaxis menu
yaxisMenu = Menu(main_menu)
main_menu.add_cascade(label = "Y-AXIS", menu = yaxisMenu)

#create plotting option
plotMenu = Menu(main_menu)
main_menu.add_cascade(label = "PLOT", menu = plotMenu)

#plot menu
plot_menu = Menu(plotMenu)
plotMenu.add_command(label = "Plot this", command = myplot)


#polarization menu xaxis
polx_menu = Menu(xaxisMenu)

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
    p=0, 1, 3
    print("elvalorde", p)

polx_menu.add_command(label = "RR", command = p0)
polx_menu.add_command(label = "LL", command = p1)
polx_menu.add_command(label = "RL", command = p2)
polx_menu.add_command(label = "LR", command = p3)
polx_menu.add_command(label = "All", command = p4)
xaxisMenu.add_cascade(label = "Polarization", menu = polx_menu)



#frequency menu xaxis
freqx_menu = Menu(xaxisMenu)

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
    f=0, 1, 2, 3
    print("elvalorde", f)

freqx_menu.add_command(label = "100-500 MHz", command = f0)
freqx_menu.add_command(label = "500-1000 MHz", command = f1)
freqx_menu.add_command(label = "1-3 GHz", command = f2)
freqx_menu.add_command(label = "3-10 GHz", command = f3)
freqx_menu.add_command(label = "All", command = f4)
xaxisMenu.add_cascade(label = "Frequency", menu = freqx_menu)




#baseline menu xaxis
basex_menu = Menu(xaxisMenu)

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
    b=0, 1, 2, 3
    print("elvalorde", b)

basex_menu.add_command(label = "1", command = b0)
basex_menu.add_command(label = "2", command = b1)
basex_menu.add_command(label = "3", command = b2)
basex_menu.add_command(label = "4", command = b3)
basex_menu.add_command(label = "All", command = b4)
xaxisMenu.add_cascade(label = "Baseline", menu = basex_menu)


#time menu xaxis
timex_menu = Menu(xaxisMenu)

t=0
def t0():
    global t
    t=0
    print("elvalorde", t)
       
def t1():
    global t
    t=1
    print("elvalorde", t)
   
def t2():
    global t
    t=2
    print("elvalorde", t)

def t3():
    global t
    t=3
    print("elvalorde", t)

def t4():
    """ description
    """
    global t
    t=0, 1, 2, 3
    print("elvalorde", t)

timex_menu.add_command(label = "1-2 hr", command = t0)
timex_menu.add_command(label = "2-4 hr", command = t1)
timex_menu.add_command(label = "4-6 hr", command = t2)
timex_menu.add_command(label = "6-10 hr", command = t3)
timex_menu.add_command(label = "All", command = t4)
xaxisMenu.add_cascade(label = "Time", menu = timex_menu)





#polarization menu yaxis
poly_menu = Menu(xaxisMenu)
poly_menu.add_command(label = "RR", command = do_nothing)
poly_menu.add_command(label = "LL", command = do_nothing)
poly_menu.add_command(label = "RL", command = do_nothing)
poly_menu.add_command(label = "LR", command = do_nothing)
poly_menu.add_command(label = "All", command = do_nothing)
yaxisMenu.add_cascade(label = "Polarization", menu = poly_menu)

#frequency menu yaxis
freqy_menu = Menu(yaxisMenu)
freqy_menu.add_command(label = "100-500 MHz", command = do_nothing)
freqy_menu.add_command(label = "500-1000 MHz", command = do_nothing)
freqy_menu.add_command(label = "1-3 GHz", command = do_nothing)
freqy_menu.add_command(label = "3-10 GHz", command = do_nothing)
freqy_menu.add_command(label = "All", command = do_nothing)
yaxisMenu.add_cascade(label = "Frequency", menu = freqy_menu)

#baseline menu yaxis
basey_menu = Menu(yaxisMenu)
for fr in range(63):
   basey_menu.add_command(label = "Comando %i"%fr, command = do_nothing)
basey_menu.add_command(label = "1", command = do_nothing)
basey_menu.add_command(label = "2", command = do_nothing)
basey_menu.add_command(label = "3", command = do_nothing)
basey_menu.add_command(label = "4", command = do_nothing)
basey_menu.add_command(label = "All", command = do_nothing)
yaxisMenu.add_cascade(label = "Baseline", menu = basey_menu)

#time menu yaxis
timey_menu = Menu(yaxisMenu)
timey_menu.add_command(label = "1-2 hr", command = do_nothing)
timey_menu.add_command(label = "2-4 hr", command = do_nothing)
timey_menu.add_command(label = "4-6 hr", command = do_nothing)
timey_menu.add_command(label = "6-10 hr", command = do_nothing)
timey_menu.add_command(label = "All", command = do_nothing)
yaxisMenu.add_cascade(label = "Time", menu = timey_menu)

# Show the menu
root.config(menu=main_menu)

# Show the window
root.mainloop()





 




