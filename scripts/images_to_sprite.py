import json
from PIL import Image
import os


def images_to_sprite(sprite_filename):
    """
    Creates sprite from images, based on data from image_jsons/<sprite_filename>.json and saves it
    in images/<sprite_filename>_tr.png
    For every image.png in json file it looks for image_tr.png (translated image) in images/dev/{}/{}.png,
    if it's not found, it uses image.png (Japanese original image)

    Should be used for sprite compilation after sprite-to-images extraction and image translation

    :param str sprite_filename: filename of the png sprite you want to create (eg "port_ringmenu")
    :return: None
    """

    root_dir = ".."
    json_filepath = "{0}/image_jsons/{1}.json".format(root_dir, sprite_filename)
    save_to = "{0}/images/{1}_tr.png".format(root_dir, sprite_filename)
    frames_extraction_path = "{0}/images/dev/{1}/{2}.png"

    with open(json_filepath) as json_stream:
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
        translated_image_filepath = frames_extraction_path.format(root_dir, sprite_filename, frame_name + "_tr")
        if os.path.exists(translated_image_filepath):
            new_image_filepath = translated_image_filepath
        else:
            new_image_filepath = frames_extraction_path.format(root_dir, sprite_filename, frame_name)
        img = Image.open(new_image_filepath)
        master.paste(img, location)

    master.save(save_to.format(root_dir, sprite_filename))


if __name__ == '__main__':
    sprite_filename = "repair_main"
    images_to_sprite(sprite_filename)
