# report.py
# 函数库

def get_description():
    """Return random weather, just like the pros"""
    from random import choice   #导入标准函数库 random 中的 choice函数
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)

