#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import join as path_join
from api_translation import ApiTranslator


img_dir = "./images/"
game_server_name = "203.104.209.39"
server_paths_to_image_names = {
    "/kcs2/img/port/port_ringmenu.png": "port_ringmenu_tr.png",
    "/kcs2/img/port/port_sidemenu.png": "port_sidemenu_tr.png",
    "/kcs2/img/arsenal/arsenal_main.png": "arsenal_main_tr.png",
    "/kcs2/img/repair/repair_main.png": "repair_main_tr.png"
}
server_api_paths = [
    "/kcsapi/api_start2/getData",
]

quest_path = "/kcsapi/api_get_member/questlist"


class Modifier:
    api_translator = ApiTranslator()

    def response(self, flow):
        if flow.request.host == game_server_name:
            requested_path = flow.request.path.split("?")[0]  # Removing GET query
            if requested_path in server_paths_to_image_names:
                new_image_path = path_join(img_dir, server_paths_to_image_names[requested_path])
                with open(new_image_path, "rb") as image_file:
                    new_image_content = image_file.read()
                flow.response.headers["Content-Length"] = str(len(new_image_content)).encode("utf-8")
                flow.response.set_content(new_image_content)
            elif requested_path in server_api_paths:
                new_content = self.api_translator.translate_api(flow.response.get_content())
                flow.response.headers["Content-Length"] = str(len(new_content)).encode("utf-8")
                flow.response.set_content(new_content)
            elif requested_path == quest_path:
                new_content = self.api_translator.translate_quests(flow.response.get_content())
                flow.response.headers["Content-Length"] = str(len(new_content)).encode("utf-8")
                flow.response.set_content(new_content)


addons = [
    Modifier()
]
