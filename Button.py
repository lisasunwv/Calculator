import graphics
class Button:
    def __init__(self, win, center, width, height, label):
        centX = center.getX()
        centY = center.getY()
        self.xmax = centX+width/2
        self.xmin = centX-width/2
        self.ymax = centY+height/2
        self.ymin = centY-height/2
        
        self.rec = graphics.Rectangle(graphics.Point(self.xmin, self.ymin), graphics.Point(self.xmax, self.ymax))
        self.rec.setFill("white")
        self.label = graphics.Text(center,label)
        self.rec.draw(win)
        self.label.draw(win)
        self.deactivate() 
        
    def clicked(self, p):
        x = p.getX()
        y = p.getY()
        return self.active and self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax
    
    def getLabel(self):
        return self.label.getText()
    
    def activate(self):
        self.active = True
        self.label.setFill("black")
        self.rec.setWidth(4)
        
    def deactivate(self):
        self.active = False
        self.label.setFill("darkgrey")
        self.rec.setWidth(1)
