from indicoio.custom import Collection
import indicoio
import operator
import PIL.Image
import numpy as np

open_file=open('../keys.txt','r')
file_lines=open_file.readlines()
key =file_lines[0].strip()
indicoio.config.api_key = key

def getType(imgPath):
    collection = Collection("materials")
    image = PIL.Image.open(imgPath)
    pixel_array = np.array(image)
    response = collection.predict(pixel_array)
    print(response)
    if (response['wood'] > 0.5):
        return 'wood'
    if (response['marble'] > 0.5):
        return 'marble'
    return 'gum'
