# variable scope = where a variable is visible and accessible
# score resolution = (LEGB) local -> Encolsed -> Global -> Built-in

def func1():
    a = 1
    def func2():
         print(a)
    func2()

func1()

def func3():
    print(x)
def func4():
    print(x)
x = 3

func3()
func4()
