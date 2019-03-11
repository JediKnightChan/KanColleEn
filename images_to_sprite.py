import json
from PIL import Image
import os

sprite_filename = "port_sidemenu"
json_filename = "image_jsons/{}.json".format(sprite_filename)
png_filename = "images/{}_tr.png".format(sprite_filename)
extraction_path = "images/dev/{}/{}.png"


with open(json_filename) as json_stream:
    sprite_json = json.load(json_stream)


master_width, master_height = list(map(int, sprite_json["meta"]["size"].values()))
master = Image.new(
    mode='RGBA',
    size=(master_width, master_height),
    color=(0, 0, 0, 0))  # fully transparent

frame_names = sprite_json["frames"]
for i, frame_name in enumerate(frame_names):
    print("{} / {}".format(i+1, len(frame_names)))
    x, y, w, h = frame_names[frame_name]["frame"].values()
    location = x, y
    if os.path.exists(extraction_path.format(sprite_filename, frame_name + "_tr")):
        new_image_filepath = extraction_path.format(sprite_filename, frame_name + "_tr")
    else:
        new_image_filepath = extraction_path.format(sprite_filename, frame_name)
    img = Image.open(new_image_filepath)
    master.paste(img, location)

master.save(png_filename.format(sprite_filename))

