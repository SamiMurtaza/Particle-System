class scrollBar:
    
    def __init__(self, xpos, ypos, sliderW, sliderH, loose):
        self.swidth = sliderW
        self.sheight = sliderH
         
        temp = sliderW - sliderH
        self.ratio = sliderW / temp 
        
        self.xpos = xpos
        self.ypos = ypos - (sliderH/2)
        
        self.spos = xpos +  sliderW/2 - sliderH/2
        self.newspos = self.spos
        
        self.sposMin, self.sposMax = xpos, xpos+sliderW - sliderH 
        self.loose = 1
        self.over = False 
        self.locked = False
        
        
        
    def update(self):
        if self.overEvent():
            self.over = True
        else:
            self.over = False
        if (mousePressed and self.over):
            self.locked = True
        if (not mousePressed): 
            self.locked = False
        
        if self.locked:
            self.newspos = self.constrain(mouseX-self.sheight/2, self.sposMin, self.sposMax)
        if (abs(self.newspos - self.spos) > 1):
            self.spos = self.spos + (self.newspos-self.spos)/self.loose
        
    
    def constrain(self, val, minv, maxv):
        return min(max(val, minv), maxv);
  
  
    def overEvent(self):
        if (mouseX > self.xpos and mouseX < self.xpos+self.swidth and mouseY > self.ypos and mouseY < self.ypos+self.sheight):
            return True
        return False
    
    def display(self):
        noStroke()
        fill(204)
        rect(self.xpos, self.ypos, self.swidth, self.sheight)
        if (self.over or self.locked):
            fill(0, 0, 0);
        else: 
            fill(102, 102, 102);
        
        rect(self.spos, self.ypos, self.sheight, self.sheight)
        
    def getPos(self):
        return self.spos * self.ratio
  

class button:
    def __init__(self, x ,y, siz):
        self.siz = siz
        self.x = x
        self.y = y
        self.color = 0
        self.state = False
        
    def update(self):
        if self.overRect():
            self.state = not self.state
            self.color = self.state*255
            return True
            
    def show(self):
        strokeWeight(4)
        stroke(255)
        fill(self.color)
        rect(self.x, self.y, self.siz, self.siz)
        
    def overRect(self):
        if mouseX >= self.x and mouseX <= (self.x+self.siz) and mouseY >= self.y and mouseY <= (self.y+self.siz):
            return True
        return False
  
class buttenSlider:
    def __init__(self, x, y, siz, states):
        self.siz = siz 
        self.x = x
        self.y = y
        self.color = 0
        self.state = 2
        self.buttons = [button(x+(i*35), y, siz) for i in range(states)]
        for i in range(self.state):
            self.buttons[i].state = True
            self.buttons[i].color = self.buttons[i].state*255
        
    def update(self):
        for i in range(len(self.buttons)):
            if self.overRect(i):
                self.state = i+1 
                for j in range(self.state):
                    self.buttons[j].state = True
                    self.buttons[j].color = self.buttons[j].state*255
                
        for j in range(self.state, len(self.buttons)):
            self.buttons[j].state = False
            self.buttons[j].color = self.buttons[j].state*255
        
    
            
        
        
    def show(self):
        strokeWeight(4)
        stroke(255)
        fill(self.color)
        for i in self.buttons:
            i.show()
        
    def overRect(self, i):
        if mouseX >= self.buttons[i].x and mouseX <= (self.buttons[i].x+self.siz) and mouseY >= self.buttons[i].y and mouseY <= (self.buttons[i].y+self.siz):
            return True
        return False
