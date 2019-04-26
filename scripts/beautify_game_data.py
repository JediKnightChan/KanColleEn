import json
import os

directory = "../catched/"


def beautify():
    file_names = os.listdir(directory)
    for filename in file_names:
        is_svdata = False
        is_game_data = False
        with open(os.path.join(directory, filename), "rb") as stream:
            file_content = stream.read()
            if file_content.startswith(b"svdata="):
                file_content = file_content.replace(b"svdata=", b"")
                is_svdata = True
            if ".json" in filename or is_svdata:
                is_game_data = True
                my_dict = json.loads(file_content)
        if is_game_data:
            with open(os.path.join(directory, "1" + filename), "wb") as stream:
                new = json.dumps(my_dict, indent=4, ensure_ascii=False).replace("\n", "\r\n").encode("utf-8")
                stream.write(new)


if __name__ == '__main__':
    beautify()
