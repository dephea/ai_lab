def myFunc(one, *two, **three):
    print("First:" + one) 
    for i in two: 
        print("In two: " + i)

    for k, v in three.items():
        print("In three: ", v)

myFunc("Abcd", "ZXC", "ZXC", "ZXC", "ZXC", "123", three=("1", "2", "3"))