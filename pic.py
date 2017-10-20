import SimpleCV as scv 

def takePhoto(path, myCam):
    myCam.getImage().scale(640, 480).save(path)