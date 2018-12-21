from Tkinter import *

def do_nothing(x):
    print (x)



root = Tk()


def myplot(d,p):
    print("Look at me plot")

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
plotMenu.add_cascade(label = "Plot", menu = plot_menu)
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
    p=2
    print("elvalorde", p)


polx_menu.add_command(label = "RR", command = p0)
polx_menu.add_command(label = "LL", command = p1)
polx_menu.add_command(label = "RL", command = p2)
polx_menu.add_command(label = "LR", command = do_nothing)
polx_menu.add_command(label = "All", command = do_nothing)
xaxisMenu.add_cascade(label = "Polarization", menu = polx_menu)



#frequency menu xaxis
freqx_menu = Menu(xaxisMenu)
freqx_menu.add_command(label = "100-500 MHz", command = do_nothing)
freqx_menu.add_command(label = "500-1000 MHz", command = do_nothing)
freqx_menu.add_command(label = "1-3 GHz", command = do_nothing)
freqx_menu.add_command(label = "3-10 GHz", command = do_nothing)
freqx_menu.add_command(label = "All", command = do_nothing)
xaxisMenu.add_cascade(label = "Frequency", menu = freqx_menu)

#baseline menu xaxis
basex_menu = Menu(xaxisMenu)
basex_menu.add_command(label = "1", command = do_nothing)
basex_menu.add_command(label = "2", command = do_nothing)
basex_menu.add_command(label = "3", command = do_nothing)
basex_menu.add_command(label = "4", command = do_nothing)
basex_menu.add_command(label = "All", command = do_nothing)
xaxisMenu.add_cascade(label = "Baseline", menu = basex_menu)

#time menu xaxis
timex_menu = Menu(xaxisMenu)
timex_menu.add_command(label = "1-2 hr", command = do_nothing)
timex_menu.add_command(label = "2-4 hr", command = do_nothing)
timex_menu.add_command(label = "4-6 hr", command = do_nothing)
timex_menu.add_command(label = "6-10 hr", command = do_nothing)
timex_menu.add_command(label = "All", command = do_nothing)
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
    basey_menu.add_command(label = "Comando %i"%fr, command = lambda i=fr: do_nothing(i))

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






 




