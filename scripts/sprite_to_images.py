import json
from PIL import Image
import os


def sprite_to_images(sprite_filename):
    """
    Extracts images from sprites, based on data from image_jsons/<sprite_filename>.json and saves them
    to images/dev/<sprite_filename>/ as <image>.png files

    Should be used for sprite-to-images extraction for further translation and sprite compilation

    :param str sprite_filename: filename of the png sprite you want to extract images from (eg "port_ringmenu")
    :return:
    """

    root_dir = ".."
    json_filepath = "{0}/image_jsons/{1}.json".format(root_dir, sprite_filename)
    sprite_filepath = "{0}/images/{1}.png".format(root_dir, sprite_filename)
    save_to_dir = "{0}/images/dev/{1}/".format(root_dir, sprite_filename)
    save_to_filepath = "{}/{}.png"

    os.makedirs(save_to_dir, exist_ok=True)
    sprite = Image.open(sprite_filepath)

    with open(json_filepath) as json_stream:
        sprite_json = json.load(json_stream)

    frame_names = sprite_json["frames"]
    for i, frame_name in enumerate(frame_names):
        print("{} / {}".format(i+1, len(frame_names)))
        x, y, w, h = frame_names[frame_name]["frame"].values()
        area = x, y, x+w, y+h
        cropped_img = sprite.crop(area)
        cropped_img.save(save_to_filepath.format(save_to_dir, frame_name))


if __name__ == '__main__':
    sprite_filename = "repair_main"
    sprite_to_images(sprite_filename)
