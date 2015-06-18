import animation

class Blob(animation.AnimatedObject):

    def __init__(self, canvas, xy, wh, ink, delta):
        self.canvas = canvas
        self.delta = delta
        self.id = self.canvas.create_oval(xy[0], xy[1], xy[0]+wh[0], xy[1]+wh[1], fill=ink)   

    def move(self):
        
        self.canvas.move(self.id, self.delta, 0)
