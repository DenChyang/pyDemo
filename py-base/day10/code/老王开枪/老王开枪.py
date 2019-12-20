class Person(object):
    def __init__(self,name):
        self.name = name
        self.gun = None
        # 血量
        self.hp = 100
        pass
    # 添加子弹到弹夹中
    def add_zidan_2_danjia(self,zi_dan_temp,dan_jia_temp):
        dan_jia_temp.add_zi_dan(zi_dan_temp)
    # 添加弹夹到枪中
    def add_danjia_2_gun(self,dan_jia_temp,gun_temp):
        gun_temp.add_dan_jia(dan_jia_temp)

    # 拿枪
    def naqiang(self,gun_temp):
        self.gun = gun_temp

    # TODO 省略
    def __str__(self):
        pass

    def kaiqiang(self,diren):
        pass

# 子弹
class ZiDan(object):
    # 子弹有杀伤力
    def __init__(self,lethality):
        self.lethality = lethality

# 弹夹
class DanJia(object):
    # 弹夹容量
    def __init__(self,capacity):
        self.capacity = capacity
        self.zidan_list = []

    # 将子弹压入弹夹中
    def add_zi_dan(self,zi_dan_temp):
        if len(self.zidan_list)<=20:
            self.zidan_list.append(zi_dan_temp)
        else:
            print("弹夹满了，不能继续压入")


class Gun(object):
    def __init__(self):
        self.dan_jia = None

    def add_dan_jia(self,dan_jia_temp):
        if self.dan_jia == None:
            self.dan_jia = dan_jia_temp
        else:
            print("请先卸下弹夹")

def main():
    # 有老王
    laowang = Person("老王")
    # 有枪
    gun = Gun()

    # 有弹夹
    dan_jia = DanJia(20)

    # 装子弹
    for i in range(15):
        # 有子弹
        zi_dan = ZiDan(10)
        # 老王把子弹装到弹夹 里
        laowang.add_zidan_2_danjia(zi_dan,dan_jia)

    # 老王把弹夹装到枪里
    laowang.add_danjia_2_gun(dan_jia,gun)

    # 有敌人
    laoLi = Person("老李")
    # 老王开枪打敌人
    laowang.naqiang(gun)

    laowang.kaiqiang(laoLi)


if __name__ == '__main__':
    main()
