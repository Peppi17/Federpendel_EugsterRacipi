t = 0

def setup():
    size(1800, 1400)
    frameRate(25)


def draw():
    global t
    
    background(255, 255, 255)
      
    strokeWeight(10)
    point(10*t, 200+cos(t)*50)
    t = t + 0.2
       
