def convertor(celsius):
    f = (celsius * 1.8) - 32
    return f


c = int(input("Enter celsius: "))
result = convertor(c)
print(result)