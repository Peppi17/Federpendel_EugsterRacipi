#Kariertes Raster

def grid(xscl, yscl):
    
    for i in range(0, rangex/xscl): #Senkrechte Linien
        strokeWeight(1)
        stroke(220, 220, 220)
        line(i*xscl, ymax, i*xscl, ymin)

    for i in range(0, rangey/yscl): #Waagrechte Linien
        strokeWeight(1)
        stroke(220)
        line(xmin, i*yscl, xmax, i*yscl) #Zwei Linien gespiegelt an der X-Achse
        line(xmin, -i*yscl, xmax, -i*yscl)
    
    strokeWeight(2)
    stroke(0)
    line(xmin, 0, xmax, 0) #X-Achse
    line(xmin, ymin, xmin, ymax) #Y-Achse
