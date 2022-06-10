import json
import numpy as np

def convert_bboxes(filepath):

    with open(filepath) as json_file:
        annotation = json.load(json_file)

    try:

        for t in annotation['text']:
            rect = np.array(annotation['text'][t]['rectangle'], np.int32)
            # Get start and end coordinates, convert to int and cast into tuple
            #startx, starty = np.round(rect[0] * r, decimals=0).astype('int')
            #endx, endy = np.round(rect[1] * r, decimals=0).astype('int')

            # Calculate bounding box width and height
            #width = endx - startx
            #height = endy - starty

    except KeyError:
        print(f"No text in the file {file_path}.")


file_path = "../../ma_thesis/ai2d/annotations/8.png.json"
convert_bboxes(file_path)