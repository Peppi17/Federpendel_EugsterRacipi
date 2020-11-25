import math

t = 0
A = 0.5
# Range of y-values
xmin = -900/25 #halbe Bildschirmbreite : x-Streckung = Skala t = 1 s
xmax = 900/25

# Range of y-values
ymin = -700/100 #halbe Bildschirmhöhe : y-Streckung = Skala x = 1 m
ymax = 700/100

# Calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(1800, 1400)
    frameRate(25)
    this.surface.setTitle("Sinus und Cosinus")
    xscl = width/rangex
    yscl = -height/rangey

def draw():
    background(255)
    translate(width/2, height/2)
    grid(xscl, yscl)
    global t
    global A
    
    xbeg = 0 #xpos zu Beginn
    ybeg = 0 #ypos zu Beginn
    
      
    strokeWeight(10)
    point(xbeg+25*t, ybeg-A*cos(t)*100) #25 = Streckung x-Achse, 100 = Streckung y-Achse
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
        
def grid(xscl, yscl):
    strokeWeight(1)
    stroke(220, 220, 220)   
    for i in range(0, xmax):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin, ymax + 1):
        line(0, i*yscl, xmax*xscl, i*yscl)
    strokeWeight(2)
    stroke(0)
    line(0, ymin*yscl, 0, ymax*yscl)
    line(xmin*xscl, 0, xmax*xscl, 0)
