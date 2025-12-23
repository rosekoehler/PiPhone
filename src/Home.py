from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up one level to PiPhone directory, then into assets
ASSETS_DIR = os.path.join(SCRIPT_DIR, "..", "assets")

# Touch screen specific
Window.size = (320, 480) 

# Rotate the display 90 degrees (potrait)
Window.rotation = 90

Window.fullscreen = True

# --- Home Screen ---
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        # Background
        with layout.canvas.before:
            # Use absolute path to the image
            image_path = os.path.join(ASSETS_DIR, "homeScreen.png")
            
            # Check if file exists and print debug info
            print(f"Script directory: {SCRIPT_DIR}")
            print(f"Assets directory: {ASSETS_DIR}")
            print(f"Looking for image at: {image_path}")
            print(f"Image exists: {os.path.exists(image_path)}")
            
            if os.path.exists(image_path):
                print("Loading image...")
                self.bg_rect = Rectangle(source=image_path, pos=(0, 0), size=Window.size)
            else:
                print("Image NOT found!")
                self.bg_rect = None
        
        layout.bind(size=self.update_bg, pos=self.update_bg)
        
        # Time label
        self.time_label = Label(
            text="12:45",
            font_size=30,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(100, 30),
            pos=(10, 400)  
        )
        layout.add_widget(self.time_label)
        
        # Date label
        self.date_label = Label(
            text="Sep 22, 2025",
            font_size=20,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(150, 25),
            pos=(10, 430)
        )
        layout.add_widget(self.date_label)
        
        # Call button
        self.call_btn = Button(
            text="Call",
            size_hint=(None, None),
            size=(120, 40),
            pos=(10, 50)
        )
        self.call_btn.bind(on_press=self.go_to_call_screen)
        layout.add_widget(self.call_btn)
        
        # Text button
        self.text_btn = Button(
            text="Text",
            size_hint=(None, None),
            size=(120, 40),
            pos=(10, 100)
        )
        self.text_btn.bind(on_press=self.go_to_text_screen)
        layout.add_widget(self.text_btn)
        
        self.add_widget(layout)
    
    def update_bg(self, *args):
        if self.bg_rect:
            self.bg_rect.size = Window.size
            self.bg_rect.pos = (0, 0)
    
    def go_to_call_screen(self, instance):
        self.manager.current = "call_screen"
    
    def go_to_text_screen(self, instance):
        self.manager.current = "text_screen"

# --- Call Screen ---
class CallScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=3, padding=5, spacing=5)
        
        # Buttons 1-9
        for i in range(1, 10):
            btn = Button(text=str(i))
            btn.bind(on_press=self.on_call_button)
            layout.add_widget(btn)
        
        # Back button
        back_btn = Button(text="Back")
        back_btn.bind(on_press=self.go_back_home)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
    
    def on_call_button(self, instance):
        print(f"Calling {instance.text}...")
    
    def go_back_home(self, instance):
        self.manager.current = "home_screen"

# --- Text Screen ---
class TextScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        # Back button
        back_btn = Button(
            text="Back",
            size_hint=(None, None),
            size=(120, 40),
            pos=(10, 50)
        )
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