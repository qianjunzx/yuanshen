class Fundmantal_board(object):
    def __init__(self) :
        self.entry_dict={}
    def input(self,entry_type,value):#输入面板数据的方法
        self.entry_dict[entry_type] += value

    def output(self,entry_type):#输出面板数据的方法
        return self.entry_dict[entry_type]
class Special_board(Fundmantal_board):
    def __init__(self,adition_time):
        self.adition_time = adition_time
    def time_adittional(self,adition_time,entry_type):
        if adition_time == self.adition_time:
            return self.entry_dict[entry_type]
        else:
            return 0
class Ralic_class(object):
    def __init__(self,relic_type):
        self.relic_type = relic_type
        self.list1=[]
        self.list2=[]
    def adition(self,entry_type,entry_value):#用adition（词条类型，数值）方法添加词条
        self.list1.append(entry_type)
        self.list2.append(entry_value)
class Weapon(object):
    bows = ['幽夜华尔兹','终末嗟叹之诗','风花之颂','西风猎弓','天空之翼',
    '弓藏','阿莫斯之弓','鸦羽弓','黑檀弓','信使','绝弦','祭礼弓','宗室长弓','钢轮弓',
    '暗巷猎手','黑岩战弓','苍翠猎弓','试作澹月','弹弓','反曲弓'
    ]
    swords = []
    claymores = []
    polearms = []
    catalysts = []  
    def __init__(self,level,title):
        self.level = level
        self.title = title
        self.weapon_type = self.weapon_typing
    def weapon_typing(self):
        if self.title in Weapon.bows:
            return 'bow'
        if self.title in Weapon.swords:
            return 'sword'
        if self.title in Weapon.catalysts:
            return 'catalyst'
        if self.title in Weapon.polearms:
            return 'polearm'
        if self.title in Weapon.claymores:
            return 'claymore'