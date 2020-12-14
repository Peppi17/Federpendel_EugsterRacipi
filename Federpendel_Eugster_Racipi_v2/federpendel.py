# Zeichnet die Animation (Balken oben, "Feder" als Linie und anhaengende/r Ball/Masse)

def federpendel(A, omega, t, streckungY, objX, objY, obj_laenge, obj_breite, factor_k, factor_m): 
    
   
    # Linie ("Feder" vereinfacht dargestellt als Linie)
    strokeWeight(2+factor_k/PI)
    stroke(100)
    line(objX, objY + obj_breite, objX,-A*cos(omega*t)*streckungY) # Linie("Feder") und Balken oben, an dem der Ball angemacht ist
    
    # Ball
    strokeWeight(5+factor_m*20)
    stroke(255, 100, 0)
    point(objX, -A*cos(omega*t)*streckungY) # Kreieren der neuen Zeichnung (Ball und Linie)
 
    #Balken
    noStroke()
    fill(200)
    rect(objX - obj_laenge/2, objY, obj_laenge, obj_breite)  
