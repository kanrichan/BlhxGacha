from PIL import Image, ImageDraw, ImageFont
from .make_card import Card, res, jpg
from .pool_info import Pool


class Position:
    def __init__(self):
        self.times = -1  # 记录查询次数
        self.gap = 260
        self.x1 = 275
        self.y1 = 200
        self.x2 = 375
        self.y2 = 550

    def next(self):
        self.times += 1
        if self.times < 5:
            return (self.x1 + self.gap * self.times, self.y1)
        else:
            return (self.x2 + self.gap * (self.times - 5), self.y2)


def build_ten(name: str, seed: str) -> str:
    background_size = (1920, 1080)
    card_size = (230, 330)
    # 产生10个随机人物
    pool = Pool(name)
    characters = pool.rand_ten(seed)
    # 读取背景
    picture = jpg("background", "background")
    background = Image.open(picture, "r").convert("RGBA")
    background = background.resize(background_size, Image.ANTIALIAS)
    # 实例坐标对象
    Posi = Position()
    for character in characters:
        # 读取卡面
        card = Card(character).pic()
        card = card.resize(card_size, Image.ANTIALIAS)
        background.paste(card, Posi.next(), card)
    background = background.convert("RGB")
    picture = jpg("output", "test")
    background.save(picture)
    return picture


#build_ten("轻型池", "a")