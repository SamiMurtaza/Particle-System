from system import System
from Scrollbar import scrollBar, button, buttenSlider
from point import Point

Point.height = System.height = height = 1080 
Point.width = System.width = width = 1920

amount = 1000
gravity = 100000


system = System(amount, gravity)



def setup():
    size(width, height, P3D) 
    fullScreen()
    background(0)
    noFill()
    stroke(255)
    strokeWeight(4)
    
    system.butC.state = True
    system.butC.color = 255


light = 0
        
def draw():
    global light

    if system.butC.state:
        background(light)
        if system.invert and light<250:
            light = light + 5
        elif light > 0:
            light = light - 5
        
    system.panel()
    
    if not system.butP.state:
        system.update()
    else:
        system.show()
        
    if system.butWi.state:
        system.trackWind()
    
def mouseReleased():
    system.mouseReleased()
    
