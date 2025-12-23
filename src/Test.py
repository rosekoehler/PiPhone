from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        # make window fullscreen
        Window.fullscreen = True

        # create button
        button = Button(
            text="Click Me",
            font_size=32
        )

        # bind button press to function
        button.bind(on_press=lambda instance: print("Clicked!"))

        return button


if __name__ == "__main__":
    MyApp().run()
