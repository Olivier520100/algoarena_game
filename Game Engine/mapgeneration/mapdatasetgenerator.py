import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import random 
import math
import keyboard
from matplotlib.widgets import Button
import string

def stringgenerate(): 
    length = 20
    alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    alphabetsplit = alphabet.split(",")
    output = ""
    i = 0
    while i < length:
        output+=alphabetsplit[random.randint(0,25)]
        i+=1
    return output

class Map():
    def __init__(self):
        self.mapsizex = 160
        self.mapsizey = 90
        self.rawmapdata = np.zeros([self.mapsizey,self.mapsizex])
        

    def generateMapRnd(self):


        noise = self.noiselayer(self.mapsizex,self.mapsizey)

        i = 0
        while (i < 75):
            newnoise = self.noiselayer(self.mapsizex,self.mapsizey)
            noise = noise + newnoise
            i+=1
        
        refactor = self.noiserefactor(noise,100)
        return refactor
    
    
    def generateMapImage(self):

        return self.showMap(self.generateMapRnd())



    def showMap(self,terrainmap):

        # Terrain types
        # 1 = water
        # 2 = sand
        # 3 = grass1 
        # 4 = grass2
        # 5 = stone1
        # 6 = stone2
        # 7 = stone3
        # 8 = stone4
        
        desertcolor = np.array([255,255,0])
        grasscolor = np.array([0,255,0])
        deepgrasscolor = np.array([0,200,0])
        stonecolor1 = np.array([128,128,128])
        stonecolor2 = np.array([160,160,160])
        stonecolor3 = np.array([180,180,180])
        stonecolor4 = np.array([200,200,200])
        watercolor = np.array([0,0,255])

        imagearray = np.zeros([self.mapsizey, self.mapsizex,3])
        currentx = 0
        currenty = 0
        while currenty < (terrainmap).shape[0]:
            
            if terrainmap[currenty,currentx] <= 20:
                imagearray[currenty,currentx,:] = watercolor
                self.rawmapdata[currenty,currentx] = 1
            elif terrainmap[currenty,currentx] <= 23:
                imagearray[currenty,currentx,:] = desertcolor
                self.rawmapdata[currenty,currentx] = 2

            elif terrainmap[currenty,currentx] <= 45:
                imagearray[currenty,currentx,:] = grasscolor
                self.rawmapdata[currenty,currentx] = 3
            elif terrainmap[currenty,currentx] <= 70:
                imagearray[currenty,currentx,:] = deepgrasscolor
                self.rawmapdata[currenty,currentx] = 4
            elif terrainmap[currenty,currentx] <= 85:
                imagearray[currenty,currentx,:] = stonecolor1
                self.rawmapdata[currenty,currentx] = 5
            elif terrainmap[currenty,currentx] <= 92:
                imagearray[currenty,currentx,:] = stonecolor2
                self.rawmapdata[currenty,currentx] = 6
            elif terrainmap[currenty,currentx] <= 97:
                imagearray[currenty,currentx,:] = stonecolor3
                self.rawmapdata[currenty,currentx] = 7
            elif terrainmap[currenty,currentx] <= 100:
                imagearray[currenty,currentx,:] = stonecolor4
                self.rawmapdata[currenty,currentx] = 8
            currentx+=1
            if currentx==(terrainmap).shape[1]:
                currentx=0
                currenty+=1

        return imagearray

    def noisefunction(self,a1,a2,b1,b2,c1,c2,d,x,y):
        return a1*math.cos((2*math.pi/b1)*x + c1) + a2*math.cos((2*math.pi/b2)*y + c2) + d
    
    def noiselayer(self,mpsizex, mpsizey):
        
        #function format: f(x,y) = a1*cos((2pi/b1)x + c1+ a2*cos((2pi/b2)x + c2)) + d
        
        noisex = 250
        noisey = 250
        noisemap = np.zeros([mpsizey, mpsizex])
        a1 = random.random()*4+1
        a2 = random.random()*4+1
        b1 = random.random()*(noisex-noisex/3)+2*noisex/3
        b2 = random.random()*(noisey-noisey/3)+2*noisey/3
        c1 = random.random()*self.mapsizex/2
        c2 = random.random()*self.mapsizey/2
        d=random.random()*3+1
        currentx = 0
        currenty = 0
        while currenty < mpsizey:
            noisemap[currenty,currentx] = (self.noisefunction(a1,a2,b1,b2,c1,c2,d,currenty,currentx))

            if noisemap[currenty,currentx] < 0: 
                noisemap[currenty,currentx] = 0
            currentx+=1
            if currentx==(mpsizex): 
                currentx=0
                currenty+=1

        return noisemap


    def noiserefactor(self,noisearray, max):

        currentmax = noisearray.max()
        currentmin = noisearray.min()
        difference = currentmax - currentmin
        currentx = 0
        currenty = 0
        refactorarray = np.zeros([noisearray.shape[0],noisearray.shape[1]])
        while currenty < noisearray.shape[0]:
            changeto = math.ceil(((noisearray[currenty,currentx]-currentmin)/difference)*max)
            if changeto == 0:
                refactorarray[currenty,currentx] = 1
            else: 
                refactorarray[currenty,currentx] = changeto
            currentx+=1
            if currentx==(noisearray.shape[1]):
                currentx=0
                currenty+=1

        return refactorarray
            
        
gamemap = Map()

imagearray = gamemap.generateMapImage()
imageoutput = imagearray

# Function to generate and display the map image
def display_map():
    imagearray = gamemap.generateMapImage()
    return plt.imshow(imagearray.astype('uint8'), animated=True)

# Callback class for handling button click events
class Index:
    def __init__(self, aximage, gamemap):
        self.aximage = aximage
        self.gamemap = gamemap

    def good(self, event):
        # Save the current image displayed in the aximage
        imageoutput = np.array(self.aximage.get_array())
        strname = stringgenerate()
        file_path = "good/" + strname + ".png"  # Adjust the path as needed
        im = Image.fromarray(imageoutput)
        np.save("rawgoodmapdata/" + strname + ".npy", self.gamemap.rawmapdata)
        im.save(file_path)

        # Generate and display the next image
        new_imagearray = self.gamemap.generateMapImage()
        self.aximage.set_data(new_imagearray.astype('uint8'))
        fig.canvas.draw()
    
    def bad(self, event):
        # Save the current image displayed in the aximage
        imageoutput = np.array(self.aximage.get_array())
        file_path = "bad/" + stringgenerate() + ".png"  # Adjust the path as needed
        im = Image.fromarray(imageoutput)
        im.save(file_path)
        # Generate and display the next image
        new_imagearray = self.gamemap.generateMapImage()
        self.aximage.set_data(new_imagearray.astype('uint8'))
        fig.canvas.draw()
# Create a matplotlib figure and axes
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

# Display the initial map
aximage = display_map()

# Create an Index object with the AxesImage and gamemap
callback = Index(aximage, gamemap)

# Add a button for updating the map
axgood = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bgnext = Button(axgood, 'Good')
bgnext.on_clicked(callback.good)

axbad = fig.add_axes([0.60, 0.05, 0.1, 0.075])
bbnext = Button(axbad, 'Bad')
bbnext.on_clicked(callback.bad)

# Show the plot
plt.show()
    
        
