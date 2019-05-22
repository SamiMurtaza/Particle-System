from point import Point
from Scrollbar import scrollBar, button, buttenSlider

step = 7

class System():

    height = 720
    width = 1280
    
    def __init__(self, amount, gravity):
        self.amount = amount
        self.points = [Point() for i in range(amount)]    
        self.hole = None
        self.G = gravity
        self.Bright = 16
        self.mode = 0
        self.invert = False
        
        
        
        
        self.param = False
    
        self.sliderP = scrollBar(0, 40, System.width, 16, 16)
        self.sliderG = scrollBar(0, 80, System.width, 16, 16)
        
        self.sliderLi =  scrollBar(System.width/2 - 50, 150, 100, 16, 16) #life
        self.sliderFl =  scrollBar(System.width/2 - 50, 180, 100, 16, 16) #flame
        
        self.butP = button(15, 100, 25)  #pause
        self.butC = button(15, 140, 25)  #clean
        self.butS = button(15, 180, 25)  #scattar
        self.butGr = button(15, 220, 25)  #gravity
        self.butBl = button(15, 260, 25)  #Blow
        self.butIn = button(15, 300, 25)   #invert
        self.butRa = button(System.width-50, 220, 25)  #rain
        self.butWi = button(System.width-50, 260, 25)  #wind
        self.butFi = button(System.width-50, 300, 25)  #fire
        
        self.butR = button(System.width-50, 100, 25)
        self.butG = button(System.width-50, 140, 25)
        self.butB = button(System.width-50, 180, 25)
        
        self.bright = buttenSlider(15,  System.height-50, 25, 3)
        self.siz = buttenSlider(System.width - 150,  System.height-50, 25, 3)
        self.shape = buttenSlider(System.width/2 - 60,  System.height-50, 25, 3)
        
        self.butPa = button(System.width/2-12, 100, 25) #parameter
        
            
    def update(self):
        
        population = self.sliderP.getPos()
        gravity = self.sliderG.getPos()
        state = (self.butR.state*4)+(self.butG.state*2)+self.butB.state
        
        if self.hole != PVector(mouseX,mouseY): 
            self.hole = PVector(mouseX,mouseY)
            
        Point.mode = self.mode
        
        
        for i in range(self.amount):
            
            if dist(self.points[i].pos.x, self.points[i].pos.y, mouseX, mouseY) <= 2:
                self.points[i].pos, self.points[i].vel, self.points[i].acc, self.life = self.points[i].reset()
            
            force = PVector.sub(self.hole,self.points[i].pos) 
            d = force.mag()+.001
            force.normalize()
            
            strength = self.G/(d*d)
            
            force.mult(strength)
            
            self.points[i].apply_force(force)
            
            self.points[i].show(self.Bright)
            
            self.points[i].update(state)
            
            
        if self.G-4000 > gravity*100:
            self.G-=1000
            
        if self.G-4000 < gravity*100:
            self.G+=1000
            
        if self.amount-42 > population:
            for i in range(step):
                self.points.pop(int(random(0,self.amount)))
                self.amount-=1
                
        if self.amount-42 < population:
            for i in range(step):
                self.points.append(Point())
                self.amount+=1
    
    def trackWind(self):
        wind=0
        stroke(150)
        strokeWeight(4)
        if mouseX>System.width/2:
            line(System.width/2,System.height/8, System.width/2+dist(System.width/2,System.height/8, mouseX, System.height/8)//5, System.height/8)
            line(-20+System.width/2+dist(System.width/2,System.height/8, mouseX, System.height/8)//5, (System.height/8)+10 , System.width/2+dist(System.width/2,System.height/8, mouseX, System.height/8)//5, System.height/8)
            line(-20+System.width/2+dist(System.width/2,System.height/8, mouseX, System.height/8)//5, (System.height/8)-10 , System.width/2+dist(System.width/2,System.height/8, mouseX, System.height/8)//5, System.height/8)
            wind = dist(System.width/2,System.height/8, mouseX, System.height/8)//5
        
        if mouseX<System.width/2:
            line(System.width/2,System.height/8, System.width/2-dist(System.width/2,System.height/8, mouseX, System.height/8)//5, System.height/8)
            line(20+System.width/2-dist(System.width/2,System.height/8, mouseX, System.height/8)//5, (System.height/8)+10 , System.width/2-dist(System.width/2,System.height/8, mouseX, System.height/8)//5, System.height/8)
            line(20+System.width/2-dist(System.width/2,System.height/8, mouseX, System.height/8)//5, (System.height/8)-10 , System.width/2-dist(System.width/2,System.height/8, mouseX, System.height/8)//5, System.height/8)
            wind = -dist(System.width/2,System.height/8, mouseX, System.height/8)//5

        Point.wind = wind
    
    def show(self):
        for i in self.points:
            i.show(self.Bright)
        
    def panel(self):
        textSize(20)
        if self.invert:
            fill(0,0,0)
        else:
            fill(255, 255, 255)
            
        text("Particles", 10, 30)
        text("Strength", 10, 70)
    
        text(str(self.amount), System.width - 100, 30)
        text(str(self.G/1000), System.width - 100, 70)
        text("Brightness", 120, System.height-30)
        text("Pause", 50, 120)
        text("Clean", 50, 160)
        text("Scatter", 50, 200)
        text("Gravity", 50, 240)
        text("Blow", 50, 280)
        text("Invert", 50, 320)
        text("Rain", System.width-120, 240)
        text("Wind", System.width-120, 280)
        text("Fire", System.width-120, 320)
        text("Red", System.width-120, 120)
        text("Green", System.width-120, 160)
        text("Blue", System.width-120, 200)
        text("Size", System.width-200, System.height-30)
        
        self.sliderP.update()
        self.sliderG.update()
        self.sliderP.display()
        self.sliderG.display()
        self.butS.show()
        self.butP.show()
        self.butC.show()
        self.butR.show()
        self.butG.show()
        self.butB.show()
        self.bright.show()
        self.butGr.show()
        self.siz.show()
        self.butRa.show()
        self.butWi.show()
        self.butFi.show()
        self.butBl.show()
        self.butIn.show()
        self.butPa.show()
        
        
        line(System.width-120, 213, System.width-15, 213)
        
        if self.param:
            self.shape.show()
            self.sliderLi.display()
            self.sliderLi.update()
            Point.life = (self.sliderLi.getPos()+50)//2 - width//4 
            if self.butFi.state:
                self.sliderFl.display()
                self.sliderFl.update()
                Point.Flame = (self.sliderFl.getPos()+50) - width//2

            
    def mouseReleased(self):         
        self.butP.update()
        self.butC.update()
        self.butR.update()
        self.butG.update()
        self.butB.update()
        self.butS.update()
        
        if self.butPa.update():
            self.param = self.butPa.state
        
        self.mode = int(self.butS.state)
        
        self.bright.update()
        self.Bright = self.bright.state*8
        
        if self.butGr.update():
            Point.gravityMode = self.butGr.state
            
        if self.butRa.update():
            Point.rain = self.butRa.state
        
        self.siz.update()
        Point.siz = self.siz.state*6
        
        self.butWi.update()
        Point.blow = self.butWi.state
        
        if self.butWi.state:
            self.trackWind()
            
        if self.butFi.update():
            Point.fire = self.butFi.state
            
        self.butBl.update()
        Point.blowing = self.butBl.state
        
        if self.butIn.update():
            self.invert = self.butIn.state
            
        if self.param:
            self.shape.update()
            Point.Shape = self.shape.state-1
            
