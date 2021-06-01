import os.path
import base64
import cv2
from keras import models
import numpy as np

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class Verify:
    def __init__(self):
        self.textModel = ""
        self.imgModel = ""
        self.LoadImgModel()
        self.LoadTextModel()

    def LoadTextModel(self):
        if not self.textModel:
            self.textModel = models.load_model(PATH('../model.v2.0.h5'))

    def LoadImgModel(self):
        if not self.imgModel:
            self.imgModel = models.load_model(PATH('../12306.image.model.h5'))

    def verify(self):
        verify_titles = ['打字机', '调色板', '跑步机', '毛线', '老虎', '安全帽', '沙包', '盘子', '本子', '药片', '双面胶', '龙舟', '红酒', '拖把', '卷尺',
                         '海苔', '红豆', '黑板', '热水袋', '烛台', '钟表', '路灯', '沙拉', '海报', '公交卡', '樱桃', '创可贴', '牌坊', '苍蝇拍', '高压锅',
                         '电线', '网球拍', '海鸥', '风铃', '订书机', '冰箱', '话梅', '排风机', '锅铲', '绿豆', '航母', '电子秤', '红枣', '金字塔', '鞭炮',
                         '菠萝', '开瓶器', '电饭煲', '仪表盘', '棉棒', '篮球', '狮子', '蚂蚁', '蜡烛', '茶盅', '印章', '茶几', '啤酒', '档案袋', '挂钟',
                         '刺绣', '铃铛', '护腕', '手掌印', '锦旗', '文具盒', '辣椒酱', '耳塞', '中国结', '蜥蜴', '剪纸', '漏斗', '锣', '蒸笼', '珊瑚',
                         '雨靴', '薯条', '蜜蜂', '日历', '口哨']
        image = cv2.imread("../pic/verify.png")
        img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        img = (img.reshape(1, 120, 177, 1)).astype('int32') / 255
        self.LoadTextModel()
        label = self.textModel.predict(img)
        label = label.argmax()
        text = verify_titles[label]
        print("题目是{}".format(text))


if __name__ == '__main__':
    Verify().LoadTextModel()
