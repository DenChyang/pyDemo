source = open("D:\\mycode\\python\\pyDemo\\py-base\\day06\\writetest.py","r",encoding="utf-8")
file = open("D:\\mycode\\python\\pyDemo\\py-base\\day06\\laowang.py","w",encoding="utf-8")

source_read = source.read()

write= file.write(source_read)
source.close()
file.close()
