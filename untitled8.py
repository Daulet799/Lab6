print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:

    s = input("Знак (+,-,,/,sqrt, !): ")
    if s == '0':
        break
    if s in ('+', '-', '', '/', 'sqrt', '!'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '':
            print("%.2f" % (xy))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
        elif s == 'sqrt':
            print("%.2f" % (math.sqrt(x)))
            print("%.2f" % (math.sqrt(y)))
        elif s == '!':
            factorial = 1
            while x > 1:
              if (y > 1):
                factorial *= x
                factorial *= y
                x -= 1
                y -= 1
                print(factorial)


    else:
        print("Неверный знак операции!")