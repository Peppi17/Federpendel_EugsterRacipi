

def federpendel(A, omega, t, streckung, objX, objY, obj_laenge, obj_breite): 
    
    noStroke()
    fill(200)
    rect(objX - obj_laenge/2, objY, obj_laenge, obj_breite)     
    
    strokeWeight(2)
    stroke(0)
    line(objX, objY + obj_breite, objX,-A*cos(omega*t)*streckung) # Linie("Feder") und Balken oben, an dem der Ball angemacht ist
    strokeWeight(25)
    stroke(255, 100, 0)
    point(objX, -A*cos(omega*t)*streckung) # Kreieren der neuen Zeichnung (Ball und Linie)
 
