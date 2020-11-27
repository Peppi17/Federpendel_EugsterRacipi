
t = 0 #Zeit
A = 1 #Amplitude

# Bereich X-Werte
xmin = 0 
xmax = 900 #halbe Bildschirmbreite : x-Streckung = Skala (t = 1 s)

# Bereich Y-Werte
ymin = -700
ymax = 700 #halbe Bildschirmhöhe : y-Streckung = Skala (x = 10 cm)

# Bereich Graph
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    background(255)
    size(1800, 1400)
    frameRate(25) #Bilder pro Sekunde
    
    global xscl, yscl
    xscl = 25
    yscl = 20
    
    
def draw():
    #background(255)
    translate(width/2, height/2)
    
    grid(xscl, yscl)
    global t
    global A #Amplitude
    
    xbeg = 0 #xpos zu Beginn
    ybeg = 0 #ypos zu Beginn
    
      
    strokeWeight(5)
    stroke(0)
    point(xbeg+25*t, ybeg-A*cos(t)*200) #25 = Streckung x-Achse, 100 = Streckung y-Achse
    t = t + 0.04 #0.04 weil 1 s : 25 Bilder/s = Veränderung von 0.04 pro Bild
 

    

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
