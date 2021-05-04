# coding:utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont
from .char_info import Character

PATH = "./BlhxGacha/BlhxGacha"


def res(type_: str, name: str):
    """返回图片资源路径"""
    return f"{PATH}/image/{type_}/{name}.png"


def jpg(type_: str, name: str):
    """返回图片资源路径"""
    return f"{PATH}/image/{type_}/{name}.jpg"


class Card:
    def __init__(self, name: str):
        self.name = name

    def make(self, size=(230, 330)):
        # 实例化舰娘对象
        char = Character(self.name)
        # 生成透明卡面
        card = Image.new(mode='RGBA', size=size)
        # 粘贴卡面背景
        picture = res("back", char.rare())
        back_size = (int(size[0] * 0.9), int(size[1] * 0.9))
        back_x = int(size[0] / 2 - back_size[0] / 2) + 1
        back_y = int(size[1] / 2 - back_size[1] / 2)
        back = Image.open(picture, "r").convert("RGBA")
        back = back.resize(back_size, Image.ANTIALIAS)
        card.paste(back, (back_x, back_y), back)
        # 粘贴角色
        picture = res("char", char.name)
        role_size = (int(size[0] * 0.93), int(size[1] * 0.93))
        role_x = int(size[0] / 2 - role_size[0] / 2)
        role_y = int(size[1] / 2 - role_size[1] / 2)
        role = Image.open(picture, "r").convert("RGBA")
        role = role.resize(role_size, Image.ANTIALIAS)
        card.paste(role, (role_x, role_y), role)
        # 粘贴阴影条
        picture = res("outline", "BAR")
        outline_size = (int(size[0] * 0.935), int(size[1] * 0.11))
        outline_x = 8
        outline_y = 21
        outline = Image.open(picture, "r").convert("RGBA")
        outline = outline.resize(outline_size, Image.ANTIALIAS)
        card.paste(outline, (outline_x, outline_y), outline)
        card.paste(outline, (outline_x, outline_y + 222), outline)
        # 粘贴类型
        picture = res("type", char.type_())
        type_size = (int(size[0] * 0.23), int(size[1] * 0.10))
        type_x = 8
        type_y = 23
        type_ = Image.open(picture, "r").convert("RGBA")
        type_ = type_.resize(type_size, Image.ANTIALIAS)
        card.paste(type_, (type_x, type_y), type_)
        # 写字
        img_draw = ImageDraw.Draw(card)
        # 写等级
        text = "Lv.1"
        font_type = f"{PATH}/image/Mohave-Light.otf"
        font_size = 34
        font = ImageFont.truetype(font_type, font_size)
        text_x = 167
        text_y = 19
        color = (255, 255, 255)
        img_draw.text((text_x, text_y), text, font=font, fill=color)
        # 写名字
        text = char.name
        font_type = f"{PATH}/image/ZhunYuan.otf"
        font_size = 29
        font = ImageFont.truetype(font_type, font_size)
        text_width = font.getsize(text)
        text_x = int(size[0] / 2 - text_width[0] / 2)
        text_y = 246
        color = (255, 255, 255)
        img_draw.text((text_x, text_y), text, font=font, fill=color)
        # 粘贴边框
        picture = res("outline", char.rare())
        outline_size = (int(size[0] * 1), int(size[1] * 1))
        outline_x = int(size[0] / 2 - outline_size[0] / 2)
        outline_y = int(size[1] / 2 - outline_size[1] / 2)
        outline = Image.open(picture, "r").convert("RGBA")
        outline = outline.resize(outline_size, Image.ANTIALIAS)
        card.paste(outline, (outline_x, outline_y), outline)
        # 粘贴星星
        picture = res("star", char.rare())
        star_size = (int(size[0] * 1), int(size[1] * 0.12))
        star_x = 0
        star_y = 287
        star = Image.open(picture, "r").convert("RGBA")
        star = star.resize(star_size, Image.ANTIALIAS)
        card.paste(star, (star_x, star_y), star)
        # 保存图片
        picture = res("card", char.name)
        card.save(picture)
        return Image.open(picture, "r").convert("RGBA")

    def exists(self) -> bool:
        picture = res("card", self.name)
        return os.path.isfile(picture)

    def pic(self):
        if self.exists():
            picture = res("card", self.name)
            return Image.open(picture, "r").convert("RGBA")
        else:
            return self.make()
