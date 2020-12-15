# Zeichnet die Punkte auf dem Raster

def cosinuskurve(A, omega, t, rand, streckung): 
    
    # Vorderster Punkt
    strokeWeight(10)
    stroke(255, 100, 0)
    if t*25 <= rand: # bis zum Rand
        point(25*t, -A*cos(omega * t)*streckung) # 25 = Streckung x-Achse, 100 = Streckung y-Achse
    else: # auf dem Rand
        point(rand, -A*cos(omega * t)*streckung)
    
    # kleine Punkte der Kurve
    strokeWeight(3)
    stroke(100)
    l = 0
    
    if t*25 <= rand: # Kurve zeichen es den definierten Rand erreicht
        while l <= t :
            point(25*l, -A*cos(omega * l )*streckung)
            l = l + 0.04
            
    else: # Kurve zeichen nachdem es den definierten Rand erreicht, vom vordersten(orangen) Punkt aus beginnend
        for r in range(0, rand) :
            point(rand - r, -A*cos(omega*(r*0.04-t))*streckung)
            
