
# Variablen
t = 0 # Zeit
A = 1 # Amplitude

value = 0 # Start/Stopp

# Bereich X-Werte
xmin = 0 
xmax = 900 # halbe Bildschirmbreite : x-Streckung = Skala (t = 1 s)

# Bereich Y-Werte
ymin = -700
ymax = 700 # halbe Bildschirmhöhe : y-Streckung = Skala (x = 10 cm)

# Bereich Graph
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    background(255)
    size(1800, 1400) # displayWidth/Height funktioniert nicht!?
    frameRate(25) # Bilder pro Sekunde
    
    global xscl, yscl
    xscl = 25
    yscl = 20
    
    grid(xscl, yscl)
    
    
def draw():
    translate(width/2, height/2)
    
    # Cosinus Kurve
    if value == 0:
        global A, t
        strokeWeight(5)
        stroke(0)
        point(25*t, -A*cos(t)*200) # 25 = Streckung x-Achse, 100 = Streckung y-Achse
        t = t + 0.04 # 0.04 weil 1 s : 25 Bilder/s = Veränderung von 0.04 pro Bild
   
    
    # Start/Stopp
    fill(value)
    rect(-850,-650, 100, 20)
    
    
    
    
def mouseClicked():
    global value
    if value == 0:
        value = 255
    else:
        value = 0
        
        
# Kariertes Raster
def grid(xscl, yscl):
    
    translate(width/2, height/2)
    
    for i in range(0, rangex/xscl): # Senkrechte Linien
        strokeWeight(1)
        stroke(220, 220, 220)
        line(i*xscl, ymax, i*xscl, ymin)

    for i in range(0, rangey/yscl): # Waagrechte Linien
        strokeWeight(1)
        stroke(220)
        line(xmin, i*yscl, xmax, i*yscl) # Zwei Linien gespiegelt an der X-Achse
        line(xmin, -i*yscl, xmax, -i*yscl)
    
    strokeWeight(2)
    stroke(0)
    line(xmin, 0, xmax, 0) # X-Achse
    line(xmin, ymin, xmin, ymax) # Y-Achse
    



"""
def graphFunction():
    x = xmin
    while x <= xmax:
        stroke(255, 0, 0)
        line(x*xscl, math.sin(x)*yscl, (x + 0.1)*xscl, math.sin(x + 0.1)*yscl)
        stroke(255, 0, 255)
        line(x*xscl, math.cos(x)*yscl, (x + 0.1)*xscl, math.cos(x + 0.1)*yscl)
        x += 0.1
"""
#fremder code aber kei ahnig meh vo wo. und apasst uf üsi bedürfnis        
