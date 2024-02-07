from PIL import Image
import numpy as np

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data



imagemap = load_image("inputpng/algoarenatestmap2.png")[:,:,:3]




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

terrainmap = np.zeros([imagemap.shape[0], imagemap.shape[1]])
currentx = 0
currenty = 0

while currenty < (imagemap).shape[0]:
    if np.array_equal(imagemap[currenty,currentx,:],watercolor):
        terrainmap[currenty,currentx] = 1
    elif np.array_equal(imagemap[currenty,currentx,:],desertcolor):
        terrainmap[currenty,currentx] = 2
    elif np.array_equal(imagemap[currenty,currentx,:],grasscolor):
        terrainmap[currenty,currentx] = 3
    elif np.array_equal(imagemap[currenty,currentx,:],deepgrasscolor):
        terrainmap[currenty,currentx] = 4
    elif np.array_equal(imagemap[currenty,currentx,:],stonecolor1):
        terrainmap[currenty,currentx] = 5
    elif np.array_equal(imagemap[currenty,currentx,:],stonecolor2):
        terrainmap[currenty,currentx] = 6
    elif np.array_equal(imagemap[currenty,currentx,:],stonecolor3):
        terrainmap[currenty,currentx] = 7
    elif np.array_equal(imagemap[currenty,currentx,:],stonecolor4):
        terrainmap[currenty,currentx] = 8
    currentx+=1
    if currentx==(terrainmap).shape[1]:
        currentx=0
        currenty+=1
    
np.save("outputnpy/" + "algoarenatestmap2" + ".npy", terrainmap)


