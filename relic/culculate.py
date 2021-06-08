class fundmantal_board(object):
    def __init__(self) :
        self.entry_dict={}
    def input(self,entry_type,value):#输入面板数据的方法
        self.entry[entry_type] += value

    def output(self,entry_type):#输出面板数据的方法
        return self.entry_dict[entry_type]
class special_board(fundmantal_board):
    def __init__(self,adition_time):
        self.adition_time = adition_time
    def time_adittional(self,adition_time,entry_type):
        if adition_time == self.adition_time:
            return self.entry_dict[entry_type]
        else:
            return 0
class ralic_class(object):
    def __init__(self,relic_type):
        self.relic_type = relic_type
        self.list1=[]
        self.list2=[]
    def adition(self,entry_type,entry_value):#用adition（词条类型，数值）方法添加词条
        self.list1.append(entry_type)
        self.list2.append(entry_value)
