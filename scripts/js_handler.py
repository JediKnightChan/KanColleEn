import os
import re

directory = "../catched/"


def get_substr_around_index(string, index, indent):
    return string[index-indent:index+indent]


def decrease_number(number):
    return 1


def replace_font_size(string):
    string1 = string[string.index("fontSize"):]
    comma_index = string1.find(",")
    if comma_index != -1:
        string1 = string1[:comma_index+1]
    font_size = int(re.findall(r'\d+', string1)[0])
    old_fontsize_str = "fontSize={}".format(font_size)
    new_fontsize_str = "fontSize={}".format(decrease_number(font_size))
    return string.replace(old_fontsize_str, new_fontsize_str)


def handle_js():
    with open(os.path.join(directory, "-kcs2-js-main.js.txt")) as f:
        content = f.read()
    indices = [m.start() for m in re.finditer(r'fontSize=[0-9]+', content)]
    print(len(indices))
    old_to_new = {}
    for index in indices:
        s = get_substr_around_index(content, index, 30)
        new_s = replace_font_size(s)
        old_to_new[s] = new_s
    for old, new in old_to_new.items():
        content = content.replace(old, new)

    with open(os.path.join(directory, "new-kcs2-js-main.js.txt"), "w") as f:
        f.write(content)


if __name__ == '__main__':
    handle_js()
