import json
from PIL import Image
import os

sprite_filename = "port_sidemenu"
json_filename = "image_jsons/{}.json".format(sprite_filename)
png_filename = "images/{}.png".format(sprite_filename)
save_to_dir = "images/dev/{}/".format(sprite_filename)
save_to = "{}/{}.png"

os.makedirs(save_to_dir, exist_ok=True)
sprite = Image.open(png_filename)

with open(json_filename) as json_stream:
    sprite_json = json.load(json_stream)

frame_names = sprite_json["frames"]
for i, frame_name in enumerate(frame_names):
    print("{} / {}".format(i+1, len(frame_names)))
    x, y, w, h = frame_names[frame_name]["frame"].values()
    area = x, y, x+w, y+h
    cropped_img = sprite.crop(area)
    cropped_img.save(save_to.format(save_to_dir, frame_name))
