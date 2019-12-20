# 用来存储名片
businessCard = []

# 1. 打印功能提示
def show_menu():
    print("=" * 50)
    print("   名片管理系统 V0.01")
    print(" 1. 添加一个新的名片")
    print(" 2. 删除一个名片")
    print(" 3. 修改一个名片")
    print(" 4. 查询一个名片")
    print(" 5. 显示所有名片")
    print(" 6. 保存所有名片到文件")
    print(" 7. 退出系统")
    print("=" * 50)

# 添加名片
def add_businessCard():
    person = {}
    person["姓名"] = input("请输入姓名:")
    person["年龄"] = input("请输入年龄:")
    person["性别"] = input("请输入性别:")
    # person = {"姓名":name,"年龄":age,"性别":sex}
    businessCard.append(person)
    # print(businessCard)

# 删除名片
def del_bussinessCard():
    name = input("请要删除的姓名:")
    name_flag = 0

    for temp in businessCard:
        if temp["姓名"] == name:
            print("删除名片%s" % temp["姓名"])
            name_flag = 1
            businessCard.remove(temp)
            break

    if name_flag == 0:
        print("没有找到要删除的人")

# 更新名片
def update_bussinessCard():
    name = input("请要修改的名片姓名:")
    name_flag = 0

    for temp in businessCard:
        if temp["姓名"] == name:
            print("名片%s", temp["姓名"])
            temp["姓名"] = input("请输入姓名:")
            temp["年龄"] = input("请输入年龄:")
            temp["性别"] = input("请输入性别:")
            name_flag = 1
            break

    if name_flag == 0:
        print("没有找到要修改的人")

# 查询名片
def get_businessCard():
    name = input("请要查询的姓名:")
    name_flag = 0

    for temp in businessCard:
        if temp["姓名"] == name:
            print(temp)
            name_flag = 1
            break

    if name_flag == 0:
        print("查无此人")

# 显示所有
def show_all():
    print(businessCard)

# 从文件中读取数据
def get_2_file():
    global businessCard
    try:
        f = open("backup.data")
        businessCard = eval(f.read())
        f.close()
    except Exception:
        pass

# 将数据保存到文件中
def save_2_data():
    f= open("backup.data")
    f.write(str(businessCard))
    f.close()

# 选择功能
def select_function():
    while True:
        function = input("请选择一个功能:")
        if function.isnumeric():
            function = int(function)
        # 添加一个新的名片
        if function == 1:
            add_businessCard()
        # 删除一个名片
        elif function == 2:
            del_bussinessCard()
        # 修改一个名片
        elif function == 3:
            update_bussinessCard()
        # 查询一个名片
        elif function == 4:
            get_businessCard()
        # 显示所有
        elif function == 5:
            show_all()
        # 保存到文件中
        elif function == 6:
            save_2_data()
        # 退出
        elif function == 7:
            break

        # 提示异常
        else:
            print("输入错误请重新输入！")

# 运行程序
def main():
    get_2_file()
    show_menu()
    select_function()

if __name__ == "__main__":
    main()
