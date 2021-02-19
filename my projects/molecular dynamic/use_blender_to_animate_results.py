import bpy
import pandas as pd
import numpy as np

# load data file from the simulation
data = np.load(r'C:\Users\guany\Desktop\MD\output.npy',
               allow_pickle = True).item()

scene = bpy.data.collections["Collection"]
frameAnz = 10000
step = 10
scale = 1
atomNum = 108
  
bpy.ops.screen.frame_jump(end=False) # move the frame pointer to the beginning
oBall = bpy.data.objects["Sphere"]

for anz in range (atomNum):
    newBall = oBall.copy()
    newBall.data = oBall.data.copy()
    newBallName = str(anz + 1).zfill(3)
    newBall.name = newBallName
    newBall.location = (2,3,4)
    # now generate a random position for the new ball:
    xpos = data["step 1"]["x{}".format(str(anz + 1).zfill(3))]
    ypos = data["step 1"]["y{}".format(str(anz + 1).zfill(3))]
    zpos = data["step 1"]["z{}".format(str(anz + 1).zfill(3))]
    # and place the new ball at this:
    newBall.location = (xpos, ypos, zpos)
    scene.objects.link(newBall)                                                   
               
for actFrame in range(0, frameAnz, step):
    bpy.context.scene.frame_set(actFrame / step)
    for ob in scene.objects:
        if (ob.name == "Sphere" or ob.name == "Camera" or ob.name == "Sun" or ob.name == "Plane"):
            continue
        else:    
            dx = (
            data["step {}".format(actFrame + 1)]["x{}".format(ob.name)] 
            - data["step {}".format(1)]["x{}".format(ob.name)])
            
            dy = (
            data["step {}".format(actFrame + 1)]["y{}".format(ob.name)] 
            - data["step {}".format(1)]["y{}".format(ob.name)])
            
            dz = (
            data["step {}".format(actFrame + 1)]["z{}".format(ob.name)] 
            - data["step {}".format(1)]["z{}".format(ob.name)])
            
            xpos = (
            data["step {}".format(1)]["x{}".format(ob.name)]
            + dx * scale)
            
            ypos = (
            data["step {}".format(1)]["y{}".format(ob.name)]
            + dy * scale)
            
            zpos = (
            data["step {}".format(1)]["z{}".format(ob.name)]
            + dz * scale) 
            
            ob.location = (xpos, ypos, zpos)
            ob.keyframe_insert(data_path = "location", index = -1)

bpy.ops.screen.frame_jump(end=False) 


#d           = 4           # size of area where the balls spawn (STRG+Q to see what I mean)
#anz         = 100           # number of balls
#frameAnz    = 100           # number of generated frames
#spawnScale = [0.015 , 0.09] # range for random scale during spawnprocess of a new ball
#originName = "motherBall"   # name of the origin-object

##prepare scene, keyframes and keyframe-pointer:
#scene = bpy.context.scene
#scene.frame_start = 0
#scene.frame_end   = frameAnz
#bpy.ops.screen.frame_jump(end=False)

## first remove all objects from previous script-runs:
## (better than "a", then "x" and then ENTER before restarting this script!)
#bpy.ops.object.select_all(action='SELECT')
#bpy.ops.object.delete()

## "pick" the original ball from layer 1:
#oBall = bpy.data.objects[originName]  

## loop for creating (anz)x balls:
#for anz in range (0,anz):

#    # duplicate the original ball and
#    # name the new ball like "zz_Ball-00001"  
#    # zz_ is for standing below in the outliner
#    newBall = oBall.copy()
#    newBallName = str(anz).zfill(5)
#    newBallName = "zz_Ball-" + newBallName
#    newBall.name = newBallName

#    # now generate a random position for the new ball:
#    xpos = -1 * (d/2) + random.randint(0,(d-1))
#    xpos += random.random()
#    ypos = -1 * (d/2) + random.randint(0,(d-1))
#    ypos += random.random()
#    zpos =  random.randint(0,(d-1))
#    zpos += random.random()
#    # and place the new ball at this:
#    newBall.location = (xpos, ypos, zpos)

#    # scaling the new ball to get different sizes of balls:
#    sz = random.uniform(spawnScale[0] , spawnScale[1])
#    newBall.scale = (sz,sz,sz)

#    #finally deselect the ball and link it into the scene:
#    newBall.select = False
#    scene.objects.link(newBall)

## now lets create frame by frame:
#for actFrame in range(1,frameAnz + 1):

#    bpy.context.scene.frame_set(actFrame)
#    for ob in scene.objects:

#        if (ob.name != originName):
#            ploc = ob.location
#            xpos = ploc[0]
#            ypos = ploc[1]
#            zpos = ploc[2]

#            zpos = zpos + ( random.random() / 8)
#            ob.location = (xpos, ypos, zpos)
#            ob.keyframe_insert(data_path="location", index=-1)

## job done: now reset the framekeypointer to 0    
#bpy.ops.screen.frame_jump(end=False)