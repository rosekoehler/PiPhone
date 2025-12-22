from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Rectangle

# Set window size
Window.size = (320, 480)

# --- Home Screen ---
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Draw background
        with layout.canvas.before:
            self.bg_rect = Rectangle(source="assets/homeScreen.png", pos=layout.pos, size=layout.size)
        layout.bind(pos=self.update_bg, size=self.update_bg)

        # --- Time and date labels ---
        self.time_label = Label(
            text="12:45",
            font_size=30,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(200, 50),
            pos=(50, 520)
        )
        layout.add_widget(self.time_label)

        self.date_label = Label(
            text="Sep 22, 2025",
            font_size=30,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(200, 50),
            pos=(50, 570)
        )
        layout.add_widget(self.date_label)

        # --- Call button ---
        self.call_btn = Button(
            text="Call",
            size_hint=(None, None),
            size=(200, 40),
            pos=(50, 50)
        )
        self.call_btn.bind(on_press=self.go_to_call_screen)
        layout.add_widget(self.call_btn)

        # --- Text button ---
        self.text_btn = Button(
            text="Text",
            size_hint=(None, None),
            size=(200, 40),
            pos=(50, 100)
        )
        self.text_btn.bind(on_press=self.go_to_text_screen)
        layout.add_widget(self.text_btn)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def go_to_call_screen(self, instance):
        self.manager.current = "call_screen"
    
    def go_to_text_screen(self, instance):
        self.manager.current = "text_screen"


# Dial up screen
class CallScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=3, padding=10, spacing=10)

        # Example buttons for phone numbers
        for i in range(1, 10):
            btn = Button(text=str(i))
            btn.bind(on_press=self.on_call_button)
            layout.add_widget(btn)

        # Add a "Back" button
        back_btn = Button(text="Back")
        back_btn.bind(on_press=self.go_back_home)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def on_call_button(self, instance):
        print(f"Calling {instance.text}...")

    def go_back_home(self, instance):
        self.manager.current = "home_screen"


# Text Screen
class TextScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        # layout = GridLayout(cols=3, padding=10, spacing=10)

        # Add a "Back" button
        back_btn = Button(text="Back")
        back_btn.bind(on_press=self.go_back_home)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back_home(self, instance):
        self.manager.current = "home_screen"


# --- App ---
class HomeApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(HomeScreen(name="home_screen"))
        sm.add_widget(CallScreen(name="call_screen"))
        sm.add_widget(TextScreen(name="text_screen"))
        return sm


if __name__ == "__main__":
    HomeApp().run()
