import json
import os
import numpy as np
import pandas as pd
from pybboxes import BoundingBox
from PIL import Image
import re

def convert_bboxes(filepath, imagepath, image_id):

    with open(filepath) as json_file:
        annotation = json.load(json_file)

    d = []
    img = f"https://s3.datacloud.helsinki.fi/crowdsrc:ai2d/{image_id}"
    image = Image.open(f"{imagepath}/{image_id}")
    width, height = image.size

    if 'text' in annotation:
        
        for t in annotation['text']:

            rect = np.array(annotation['text'][t]['rectangle'], np.int32).flatten()
            #print("voc:", rect)
            try:
                voc = BoundingBox.from_voc(*rect)
            except ValueError:
                continue
            try:
                coco = voc.to_coco()
            except ValueError:
                continue
            #print(coco)
            coco = np.array(coco.values).reshape((2,2))
            #print(coco)
            #y_min = coco[0,1]
            #y_max = coco[1,1]
            #coco[0,1] = y_max
            #coco[1,1] = y_min
            #print("coco:", coco)
            
            dims = np.array([width, height])

            bbox = coco / dims[:,None]
            bbox = bbox.flatten()

            d.append({"shape": "rectangle", "left": bbox[0], "top": bbox[1], "width": bbox[2], "height": bbox[3]})

    if d:
        d = json.dumps(d)
    return img, d


def create_input_tsv(rst_path, dir_path, image_path):

    row_list = []

    for f in os.listdir(rst_path):
        image_id = f[:-5]
        img, outlines = convert_bboxes(f"{dir_path}{f}", image_path, image_id)
        if img and outlines:
            row = {"image": img, "outlines": outlines}
            row_list.append(row)

    df = pd.DataFrame(row_list)
    df.to_csv("../pipeline/data/ai2d_bboxes_10.tsv", sep="\t", index=False)


image_path = "../../ma_thesis/ai2d/images/"
dir_path = "../../ma_thesis/ai2d/annotations/"
rst_path = "../../ma_thesis/ai2d/ai2d-rst-10/"
#convert_bboxes(file_path, image_path, image_id)

create_input_tsv(rst_path, dir_path, image_path)
