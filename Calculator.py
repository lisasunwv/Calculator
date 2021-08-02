from Button import Button
import graphics

class Calculator:
    def __init__(self):
        self.tiped = []
        self.done = "false"
        self.win = graphics.GraphWin("Button",600,600)
        self.win.setCoords(0.0,0.0,110,110)
        self.win.setBackground("lightgreen")
        self.myButtons = []
        buttonMappingTable = [[15,75,"7"],[35,75,"8"],[55,75,"9"],
                             [75,75,"<--"],[95,75,"C"],[15,55,"4"],
                             [35,55,"5"],[55,55,"6"],[75,55,"*"],
                             [95,55,"/"],[15,35,"1"],[35,35,"2"],
                             [55,35,"3"],[75,35,"+"],[95,35,"-"],
                             [35,15,"0"],[55,15,"."]]
                              
        for butt in buttonMappingTable:
            self.myButtons.append(Button(self.win,graphics.Point(butt[0],butt[1]),10,10,butt[2]))

        self.myButtons.append(Button(self.win,graphics.Point(85,15),30,10,"="))
        self.textBox = graphics.Text(graphics.Point(45,95),"")
        
        self.textBox.draw(self.win)
        rec = graphics.Rectangle(graphics.Point(10,90), graphics.Point(100,100))
        rec.draw(self.win)
        rec.setWidth(4)

        for b in self.myButtons:
            b.activate()

    
    def getButton(self):
        p = self.win.getMouse()
        while True:
            for butt in self.myButtons:
                if(butt.clicked(p)):
                    print (butt.getLabel())
                    return butt
            p = self.win.getMouse()
            
    def processButton(self, button):
        statement = ""
        opperations = ["1","2","3","4","5","6","7","8","9","0","+","-","*","/","."]
        answer = 0
        for opp in opperations:
            if(button.getLabel() == opp ):
                if self.done == "true":
                    self.tiped = []
                self.done = "false"
                self.tiped.append(button.getLabel())
                statement = self.tiped[0:]
                print(statement)
                self.textBox.setText(statement)
        if(button.getLabel() == "<--"):
            try:
                del self.tiped[-1]
                statement = self.tiped[0:]
                self.textBox.setText(statement)
            except Exception as errobj:
                self.textBox.setText(errobj)
                self.done = "true"
                
        elif(button.getLabel() == "C"):
            self.tiped = []
            self.textBox.setText("")

        elif(button.getLabel() == "="):
            for i in self.tiped:
                statement = statement + i

            try:    
                answer = eval(statement)
                self.textBox.setText(answer)
                self.done = "true"
            except Exception as errobj:
                self.textBox.setText(errobj)
                self.done = "true"

    def run(self):
        while True:
            but = self.getButton()
            self.processButton(but)
