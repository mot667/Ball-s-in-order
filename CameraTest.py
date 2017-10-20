import SimpleCV as scv
import time


def takePic(): 
    camera.getImage().save("./images/img2.jpg")
    # /del(camera)

camera = scv.Camera(1, {"width": 640, "height": 480})



#mycam.getImage().scale(640,480).save("img.jpg")

takePic()
print("done")



