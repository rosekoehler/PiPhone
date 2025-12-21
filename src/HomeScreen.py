from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class myGrid(GridLayout):
    def __init__(self,**Kwargs):
        super(myGrid,self).__init__(**Kwargs)
        self.col = 2
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)


class HomeApp(App):
    def build(self):
        return myGrid()


if __name__ == "__main__":
    HomeApp().run()