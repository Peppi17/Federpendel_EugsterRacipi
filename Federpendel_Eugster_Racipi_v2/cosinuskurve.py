

def cosinuskurve(A, omega, k, m, t, rand, streckung): 
    
    # Vorderster Punkt
    strokeWeight(10)
    stroke(255, 100, 0)
    if t*25 <= rand: # bis zum Rand
        point(25*t, -A*cos(omega * t)*streckung) # 25 = Streckung x-Achse
    else: # auf dem Rand
        point(rand, -A*cos(omega * t)*streckung)
    
    # kleine Punkte der Kurve
    strokeWeight(3)
    stroke(100)
    l = 0
    if t*25 <= rand: # bis zum Rand
        while l <= t :
            point(25*l, -A*cos(omega * l )*streckung)
            l = l + 0.04
    else: # Punktebewegung vor dem Rand
        for r in range(0, rand) :
            point(rand - r, -A*cos(omega*(r*0.04-t))*streckung)
