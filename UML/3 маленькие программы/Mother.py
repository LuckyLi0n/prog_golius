class Mother:
    def voice(self):
        return "Не плачь!"

    def print(self):
        print(self.voice())


class Daughter(Mother):
    def voice(self):
        return "Хнык, хнык!"


d = Daughter()
d.print()

m = Mother()
m.print()
