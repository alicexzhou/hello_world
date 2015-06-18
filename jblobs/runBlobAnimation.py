#vertical moving blobs
#jiggling blobs
#different levels

import os
import Tkinter as tk
import animation
import blob
import random
import player


WIDTH, HEIGHT = 800, 500
SPEED = 40   # Smaller for faster, 40 means 1 frame per 40ms == 25 fps
#colors = ['pink', 'lightblue', 'green', 'gold', 'salmon', 'red', 'orange', 'purple', 'yellow']
colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown']

class App(tk.Frame):
    def __init__(self, myroot):
        myroot.title("Jelly Blobs of Doom")
        self.frame = tk.Frame(myroot) 
        self.frame.pack()
        self.canvas = animation.AnimationCanvas(self.frame, width=WIDTH, height=HEIGHT) 
        self.canvas.pack()
        self.addBlob()   
        
        self.player = player.Player(self.canvas, (100,200), (60,30), 'darkblue', 0)
        self.myPlayer = self.canvas.addItem(self.player)#changed this to try to pass self.myPlayer into bbox for collide function, but it looks like it's a NoneType or something
        myroot.bind('<Left>', self.player.left)
        myroot.bind('<Right>', self.player.right) 
        myroot.bind('<Up>', self.player.up)
        myroot.bind('<Down>', self.player.down)

        self.canvas.start()
        
        #self.collide()
        
    def addBlob(self):
        width = random.randint(1,200)
        height = width/2
        #blobs have a 50% chance to appear from the left every 2 seconds
        if random.randint(0,1) == 0:
            self.canvas.addItem(blob.Blob(self.canvas, (-800, random.randrange(HEIGHT)), (width, height), random.choice(colors), random.randint(2, 7)))
            self.canvas.after(2000, self.addBlob)
        
        #blobs appear from the right
        else:
            self.canvas.addItem(blob.Blob(self.canvas, (800, random.randrange(HEIGHT)), (width, height), random.choice(colors), random.randint(-7, -2)))
            self.canvas.after(2000, self.addBlob)
            
    #def collide(self):
    #    boundsPlayer = self.canvas.bbox(self.myPlayer)  # returns a tuple like (x1, y1, x2, y2)
        #widthPlayer = boundsPlayer[2] - boundsPlayer[0]
        #heightPlayer = boundsPlayer[3] - boundsPlayer[1]
        #
        #boundsBlob = self.canvas.bbox(blob.Blob)
        #widthBlob = boundsBlob[2] - boundsBlob[0]
        #heightBlob = boundsBlob[3] - boundsBlob[1]
        #
        #if boundsPlayer[0] ==boundsBlob[0] or boundsPlayer[1] ==boundsBlob[1] or boundsPlayer[2] ==boundsBlob[2] or boundsPlayer[3] ==boundsBlob[3] and widthPlayer >= widthBlob:
        #    widthPlayer += widthBlob/2
        #    heightPlayer += heightBlob/2
        #elif boundsPlayer[0] ==boundsBlob[0] or boundsPlayer[1] ==boundsBlob[1] or boundsPlayer[2] ==boundsBlob[2] or boundsPlayer[3] ==boundsBlob[3] and widthPlayer < widthBlob:
        #    widthPlayer -= widthBlob/2
        #    heightPlayer += heightBlob/2
            
            

    
root = tk.Tk()
app = App(root)
# For Macs only: Bring root window to the front
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to True' ''')

root.mainloop() 
