import indicoio
from indicoio.custom import Collection
import PIL.Image
import numpy as np
import pic
import SimpleCV as scv

open_file=open('../keys.txt','r')
file_lines=open_file.readlines()
key =file_lines[0].strip()
indicoio.config.api_key = key
collection = Collection("materials")

imgPath = "./images/img.jpg"
analyseImgPath = "./images/analyse.jpg"
mycam = scv.Camera()

while(1):
    print("1: take photo, 2: view photo, 3: train for current selection, 4: predict, 5:train, exit:exit")
    stringInput = raw_input()
    if stringInput == "1":
        pic.takePhoto(imgPath, mycam)
        print("image taken")
        #mycam.wait()
    elif stringInput == "2":
        print ("view here")
        image=PIL.Image.open(imgPath)
        image.show()
    elif stringInput == "3":
        print("1: wood, 2: marble, 3: gum")
        typeInput = raw_input()
        image=PIL.Image.open(imgPath)
        pixel_array = np.array(image)
        if typeInput == "1":
            collection.add_data([pixel_array, "wood"])
            #collection.train()
            #collection.wait()
        elif typeInput == "2":
            collection.add_data([pixel_array, "marble"])
            #collection.train()
            #collection.wait()
        elif typeInput == "3":
            collection.add_data([pixel_array, "gum"])
            #collection.train()
            #collection.wait()
        print("photo added")
    elif stringInput == "4":
        image=PIL.Image.open(imgPath)
        pixel_array = np.array(image)
        print("RESULT: \n")
        print(collection.predict(pixel_array))
    elif stringInput == "5":
        collection.train()
        collection.wait()
        print("collection trained")
    elif stringInput == "exit":
        del(mycam)
        break

#image = PIL.Image.open("./images/img2.jpg")
#image.show()


