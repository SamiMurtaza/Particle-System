
class Point():
    
    mode = 0
    gravityMode = 0
    state = 7
    siz = 14
    rain = False
    blow = False
    wind = 0
    fire = False
    blowing = False
    life = 10
    Shape = 0
    Flame = 40
    
    width = 1080
    height = 1920
    
    def __init__(self):
        self.pos, self.vel, self.acc, self.life = self.reset()
        

    def reset(self):
       
        if not Point.rain and not Point.blowing:
            if Point.fire:
                pos = PVector(Point.width/2 + (randomGaussian()*Point.Flame), 3*(Point.height/4) + (randomGaussian()*Point.Flame))

            elif not Point.mode:
                pos = PVector(random(Point.width/8, 7*(Point.width/8)), Point.height-2) 
            elif Point.mode==1:
                pos = PVector(random(2, Point.width-2), random(2,Point.width - 2))
            
        elif Point.blowing:
            pos = PVector(mouseX + (randomGaussian()*2), mouseY + (randomGaussian()*2))
        elif Point.rain:
            pos = PVector(random(2, Point.width-2), random(2,20))
        
        vel = PVector(0,0)
        acc = PVector(0,0)
        if Point.fire:
            life = random(10,2*Point.life*abs(randomGaussian()))
        else:
            life = random(10,6*Point.life)
        
        return pos, vel, acc, life
        
        

    def update(self, state):
        
        if Point.state != state:
            Point.state = state
        
        if self.pos.x<=0 or self.pos.x>=width:
            #self.vel.mult(-1)
            self.pos, self.vel, self.acc, self.life = self.reset()
        
        if self.pos.y<=0 or self.pos.y>=height:
            #self.vel.mult(-1)
            self.pos, self.vel, self.acc, self.life = self.reset()
    
        self.life-=1
        
        if self.life<=0:
            self.pos, self.vel, self.acc, self.life = self.reset()    
        
        
        if not Point.rain and not Point.fire:
            if Point.gravityMode:
                self.vel.add(self.acc)
                if self.pos.y < 1070:
                    self.vel.add(PVector(0,0.5))
            else:
                self.vel.add(self.acc)
        elif Point.fire:
            self.vel.add(PVector(0,random(-1,-3)))
        else:
            self.vel.add(PVector(0,random(1,3)))
            
        if Point.blow:
            self.vel.add(PVector(Point.wind/40,0))
            
            
        self.pos.add(self.vel)
        self.acc.mult(0)
        
        
    def show(self, bright):

        
        


        if Point.state==7:
            stroke(sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright,sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright,sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright)
        
        if Point.state==0:
            stroke(sqrt(sqrt(mag(self.vel.x, self.vel.y)))*5*bright,sqrt(sqrt(mag(self.vel.x, self.vel.y)))*5*bright,sqrt(sqrt(mag(self.vel.x, self.vel.y)))*5*bright)
            
        if Point.state==1:
            stroke(0,0,sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright)
            
        if Point.state==2:
            stroke(0,sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright,0)
            
        if Point.state==4:
            stroke(sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright,0,0)
            
        if Point.state==3:
            stroke(0,sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright,sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright)
            
        if Point.state==5:
            stroke(sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright,0,sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright)
            
        if Point.state==6:
            stroke(sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright,sqrt(mag(self.vel.x, self.vel.y))*random(0,10)*bright,0)
        
        
        if Point.Shape == 0:
            strokeWeight(random(2,Point.siz))
            point(self.pos.x, self.pos.y)
        elif Point.Shape == 1:
            strokeWeight(Point.siz/6)
            line(self.pos.x, self.pos.y, self.pos.x + random(-20,20), self.pos.y+ random(-20,20))
        elif Point.Shape == 2:
            rect(self.pos.x, self.pos.y, random(-10,10), random(-10,10))

    def apply_force(self, force):
        self.acc = force
