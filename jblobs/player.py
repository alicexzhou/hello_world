#import Blob
#import animation

class Player: 
    def __init__(self, canvas, xy, wh, ink, delta):

        self.canvas = canvas
        self.delta = delta

        self.id = self.canvas.create_oval(xy[0], xy[1], xy[0]+wh[0], xy[1]+wh[1], fill=ink)
        
    def left(self, event): # Handler for left arrow key. Ignores event arg.
        self.canvas.move(self.id, -10, 0)
        
    def right(self, event): # Handler for right arrow key. Ignores event arg.
        self.canvas.move(self.id, 10, 0)
        
    def up(self, event): # Handler for up arrow key. Ignores event arg.
        self.canvas.move(self.id, 0, -10)
        
    def down(self, event): # Handler down arrow key. Ignores event arg.
        self.canvas.move(self.id, 0, 10)
        
    def move(self):
        self.canvas.move(self.id, self.delta, 0)
        
       
        
