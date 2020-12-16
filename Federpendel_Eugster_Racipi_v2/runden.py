# Rundet Zahlen auf eine oder zwei Stellen hinter dem Komma

def runden(zahl, stellen):
    return int(zahl*pow(10, stellen))/pow(10, stellen)
