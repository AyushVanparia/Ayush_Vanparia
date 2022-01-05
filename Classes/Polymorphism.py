from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw([ddl, tb])
