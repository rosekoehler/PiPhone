from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Rectangle

# Set window size
Window.size = (320, 480)


class HomeScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Draw background
        with self.canvas.before:
            self.bg_rect = Rectangle(source="assets/galaxy.png", pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg, size=self.update_bg)

        # --- Top: time and date ---
        self.time_label = Label(
            text="12:45",
            font_size=24,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(200, 50),
            pos=(100, 400)
        )
        self.add_widget(self.time_label)

        self.date_label = Label(
            text="Sep 22, 2025",
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(200, 30),
            pos=(60, 370)
        )
        self.add_widget(self.date_label)

        # --- Middle: notifications ---
        self.notif_label = Label(
            text="No notifications",
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(250, 50),
            pos=(35, 250)
        )
        self.add_widget(self.notif_label)

        # --- Bottom: Call button ---
        self.call_btn = Button(
            text="Call",
            size_hint=(None, None),
            size=(100, 40),
            pos=(110, 50)
        )
        self.add_widget(self.call_btn)

    # resiable background
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size


class HomeApp(App):
    def build(self):
        return HomeScreen()


if __name__ == "__main__":
    HomeApp().run()
