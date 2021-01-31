# -- Coords --

x1 = 300
y1 = 210

x2 = 460
y2 = 210

x3 = 300
y3 = 365

x4 = 460
y4 = 365

# -- Height and Weight --
h = 1024
w = 840

# -- Speeds --
speedX = 5
speedY = 0
gravity = -0.1

# -- Colors --

r1 = 246
g1 = 83
b1 = 20
r2 = 124
g2 = 187
b2 = 0
r3 = 0
g3 = 161
b3 = 241
r4 = 255
g4 = 187
b4 = 0
    
def setup():
    size(h, w)
    
def draw():
                   
    background(0) #Background negro
    noCursor() #Eliminar mouse
    fill(r1, g1, b1)
    rect(x1, y1, 150, 150) #Dibujar cuadrado   
     
    fill(r2, g2, b2)
    rect(x2, y2, 150, 150) #Dibujar cuadrado
        
    fill(r3, g3, b3)
    rect(x3, y3, 150, 150) #Dibujar cuadrado    
    
    fill(r4, g4, b4)
    rect(x4, y4, 150, 150) #Dibujar cuadrado    
    
    gravity_function()

def gravity_function():
    global x1, y1, x2, y2, x3, y3, x4, y4, speedX, speedY, r1, g1, b1, gravity, r1, g1, b1, r2, g2, b2, r3, g3, b3, r4, g4, b4
    
    x1 += speedX
    y1 += speedY
    x2 += speedX
    y2 += speedY
    x3 += speedX
    y3 += speedY
    x4 += speedX
    y4 += speedY
    speedY += gravity
    
    if x1 + 140 > width or x2 + 140 > width or x1 < 0: #Si toca la pared
        speedX = -speedX #que la gravedad se retenga y rebote
        
    if y1 + 140 > height - 15: #Si toca el suelo
            speedY = -speedY
    elif y1 - 20 < 0: #Si toca el techo
            speedY = -speedY

            if(r1 == 246 and g1 == 83):
                r1 = 0
                g1 = 205
                b1 = 255
                r2 = 0
                g2 = 205
                b2 = 255
                r3 = 0
                g3 = 205
                b3 = 255
                r4 = 0
                g4 = 205
                b4 = 255

            elif(r1 == 0):

                r1 = 246
                g1 = 83
                b1 = 20
                r2 = 124
                g2 = 187
                b2 = 0
                r3 = 0
                g3 = 161
                b3 = 241
                r4 = 255
                g4 = 187
                b4 = 0
