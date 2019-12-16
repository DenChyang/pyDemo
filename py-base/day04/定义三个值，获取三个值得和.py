def getAdd(num1, num2, num3):
    result = num1 + num2 + num3
    print("%s + %s + %s = %s"%(num1,num2,num3,result))
    return result

#求平均
def avgNum(num1, num2, num3):
    result = getAdd(num1, num2, num3)
    result = result / 3
    print("平均值%s"%result)
    return result

num1 = int(input("请输入第一个数"))
num2 = int(input("请输入第二个数"))
num3 = int(input("请输入第三个数"))
#getAdd(num1,num2,num3)
avgNum(num1,num2,num3)
