import json
import re
from os.path import join as path_join


MAX_QUEST_LINE_LEN = 80
JP_TO_EN_FILE_DIR = "api"
JP_TO_EN_FILE_NAMES = [
    "ship_names.json",
    "item_names.json",
    "ship_types.json",
]


class ApiTranslator:
    """
    Translates game api responses
    """
    def __init__(self):
        self.jp_to_en = {}
        for filename in JP_TO_EN_FILE_NAMES:
            with open(path_join(JP_TO_EN_FILE_DIR, filename), "rb") as f:
                self.jp_to_en.update(json.load(f))
        with open("api/quests_en.json", "rb") as f:
            self.quests = json.load(f)

    def translate_api(self, content):
        """
        :param bytestring content: content of the common api response
        :return bytestring new_content: translated content

        Should be used to translate files with unchanging game data pieces (such as fleet girls' names)
        """
        content = content.replace(b"svdata=", b"")
        json_dict = json.loads(content)
        self.translate_dict_values(json_dict)
        new_content = b"svdata=" + json.dumps(json_dict).encode("utf-8")
        return new_content

    def translate_quests(self, content):
        """
        :param bytestring content: content of the quests api response
        :return bytestring new_content: translated content

        Quests are often updated, so we should translate them by their ids
        """
        content = content.replace(b"svdata=", b"")
        json_dict = json.loads(content)
        for jp_quest_dict in json_dict["api_data"]["api_list"]:
            quest_number = str(jp_quest_dict["api_no"])
            if quest_number in self.quests:
                jp_quest_dict["api_title"] = self.quests[quest_number]["name"]
                jp_quest_dict["api_detail"] = self.break_string(self.quests[quest_number]["desc"])
        new_content = b"svdata=" + json.dumps(json_dict).encode("utf-8")
        return new_content

    def translate_list(self, my_list):
        for i, value in enumerate(my_list):
            if isinstance(value, dict):
                self.translate_dict_values(value)
            elif isinstance(value, list):
                self.translate_list(value)
            elif value in self.jp_to_en:
                my_list[i] = self.jp_to_en[value]

    def translate_dict_values(self, my_dict):
        for key, value in my_dict.items():
            if isinstance(value, dict):
                self.translate_dict_values(value)
            elif isinstance(value, list):
                self.translate_list(value)
            elif value in self.jp_to_en:
                my_dict[key] = self.jp_to_en[value]

    @staticmethod
    def break_string(string):
        """
        :param string: string we want to break
        :return: string with inserted '\n'
        """
        if len(string) > MAX_QUEST_LINE_LEN:
            indices = [m.start() for m in re.finditer(" ", string)]
            needed_index = min(indices, key=lambda x:abs(x-MAX_QUEST_LINE_LEN))
            first_part = string[:needed_index].strip()
            second_part = string[needed_index:].strip()
            string = "{}\n{}".format(first_part, second_part)
        return string
