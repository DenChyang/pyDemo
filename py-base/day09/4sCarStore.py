class CarStrore(object):
    def __init__(self):
        self.factory = Factory()

    def order(self,car_type):
        return self.factory.select_car_by_style(car_type)


class Factory(object):
    def select_car_by_style(self,car_type):
        if car_type=="QQ":
            return QQ()
        if car_type== "F0":
            return F0()

class Car(object):

    def move(self):
        print("汽车正在移动")

class QQ(Car):
    pass
class F0(Car):
    pass

strore = CarStrore()
car = strore.order("QQ")
car.move()

