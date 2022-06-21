## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAU0kcVSVfCwSy0Xup7c8WKrcJc81yGiJvRmPXg8Qwm91Guwxz62-5yyI990KragSV-oRSV_D8qH-O0zrr634OawjqisCmpkt0NHYCANiNGF28aK4ekTN2gnf_0r5AoqVAc8jE5TcULIe7_sv9asRQFJUR4AwM6QgFlxBbqrgApXgTC0DkR7lEZQjVRFkzmD_oSopbrtpXW8SLkxgCT4Bod1ifRfMzJkpFHpVXMog4DlnQDCkmsiD7vAmZWjCu5fNP2rUGcrXY7V9UW8n99rtAdtpcobIO-e93uO5t_yPfoYroVUAGueMKzDNzzsWucJ6blc2BhwpY2KLI1i665AJBLAAAAAUd_dboA")
BOT_TOKEN = getenv("BOT_TOKEN", "5599985473:AAFXYOCNfseDWIjKWqAVi1CKUooUgu8J3Bk")
BOT_NAME = getenv("BOT_NAME", "𝖣𝖺𝗅𝗅𝖺𝗌 𝖬𝗎𝗌𝗂𝖼")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Parki")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DBBBDD")
ALIVE_NAME = getenv("ALIVE_NAME", "Parki")
BOT_USERNAME = getenv("BOT_USERNAME", "Dallas1BoT")
OWNER_ID = getenv("OWNER_ID", "1283712566")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DalIas1")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1283712566").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "!").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
