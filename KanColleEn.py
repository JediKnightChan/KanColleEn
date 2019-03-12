from mitmproxy import ctx
from mitmproxy.http import HTTPFlow
from os.path import join as path_join

img_dir = "./images/"
game_server_name = "203.104.209.39"
server_paths_to_image_names = {
    "/kcs2/img/port/port_ringmenu.png": "port_ringmenu_tr.png",
    "/kcs2/img/port/port_sidemenu.png":"port_sidemenu_tr.png",
    "/kcs2/img/arsenal/arsenal_main.png": "arsenal_main_tr.png"
}


class Modifier:
    def response(self, flow):
        if flow.request.host == game_server_name:
            requested_path = flow.request.path.split("?")[0]  # Removing GET query
            if requested_path in server_paths_to_image_names:
                new_image_path = path_join(img_dir, server_paths_to_image_names[requested_path])
                with open(new_image_path, "rb") as image_file:
                    new_image_content = image_file.read()
                flow.response.headers["Content-Length"] = str(len(new_image_content)).encode("utf-8")
                flow.response.set_content(new_image_content)
            """
            # API test translation
            json_dir = "./"
            elif requested_path == "/kcsapi/api_get_member/questlist":
                api_body = flow.response.get_text()
                ctx.log.info("\r\n\r\n\r\n\r\n!!!!!!! That's what we need! !!!!!!!\r\n{}\r\n\r\n\r\n\r\n".format(
                    api_body
                ))
                with open(path_join(json_dir, "api_response.json")) as f:
                    new_content = f.read()
                flow.response.set_text(new_content)
            """
addons = [
    Modifier()
]