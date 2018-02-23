class Animal():
    name = 'Amy'
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = 'Covers body'
    def get_color(self, abd):
        return self.color
    def make_noise(self):
        return self.noise

dog = Animal()
dog.get_color()

def some_func(arg_1, arg_2, kwa_1=None, kwa_2=None):
    print(arg_1, arg_2)
    if kwa_1 != None:
        print(kwa_1)
    #return arg_1


some_func("asd","asdf",kwa_1="dfdfd")



