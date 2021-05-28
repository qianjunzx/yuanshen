from openpyxl import load_workbook
from openpyxl.utils.cell import column_index_from_string
wb=load_workbook(filename='relic_data.xlsx')
relic_condition=[1,1,1,1,1]
    
def relic_board(relic_condition):
    global entry_type
    outcome=[0,0,0,0,[],[],0,0,0,0,0,0]
    for round1 in range(1,6):
        sheet1=wb[wb.sheetnames(round1)]
        for round2 in range(2,7):
            cell1=sheet1.cell(row=relic_condition[round1-1],column=round2).value
            cell2=sheet1.cell(row=relic_condition[round1-1],column=round2+5).value
        if isdamage(cell1) != 0:
            func=outcome[5]
            func.append(cell2)
            outcome[5]=func
            func=outcome[6]
            func.append(isdamage(cell1))
            outcome[6]=func
        else:
            outcome[entry_type[cell1]] += cell2
    return outcome

entry_type={
    '攻击力':        1,
    '攻击力百分比':  2,
    '暴击率':        3,
    '暴击伤害':      4,
    '防御力':        7,
    '防御力百分比':  8,
    '生命值':        9,
    '生命值百分比': 10,
    '治疗加成':     11,
    '元素精通':     12,
 }

def isdamage(a):
    if a == '火元素伤害加成':
        return 1
    elif a == '水元素伤害加成':
        return 2
    elif a == '冰元素伤害加成':
        return 3
    elif a == '雷元素伤害加成':
        return 4
    elif a == '草元素伤害加成':
        return 5
    elif a == '风元素伤害加成':
        return 6
    elif a == '岩元素伤害加成':
        return 7
    elif a == '物理伤害加成':
        return 8
    else:
        return 0
def relic_suit(relic_condition):#查看套件类型
    suit={}
    suit_type=[]
    for round1 in range(0,5):
        sheet1=wb[wb.sheetnames(round1+1)]
        cell=sheet1.cell(row=relic_condition[round1],column=1).value
        suit[cell]+=1
        if suit[cell]==1:
            suit_type.append(cell)
    return suit,suit_type
def suit_board_plus(suit,suit_type): #套件效果计算 
    pass
def abab():
    pass
