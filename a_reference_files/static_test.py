from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import mainthread

Window.clearcolor = (255, 255, 255, 255)
Window.maximize()
# used to load a file other than the default, which is my.kv
kv = Builder.load_file("static_test.kv")

placeholder_streams = []

STREAM_COUNT = 3

# all classes referred to in the .kv files don't need any code here. Note that this inherits from Screen
class HomeScreen(Screen):
    
    @mainthread
    def on_enter(self):
        for num in range(STREAM_COUNT):
            # note that these are placeholders, but real streams will be stored in some sort of list similar to this
            placeholder_streams.append(
                Button(
                    size_hint = (0.75, 0.2),
                    pos_hint = {'x' : 0.05, 'y' : 0.1 + ((3 * num) // STREAM_COUNT)/10 * 2.5},
                    background_normal = '',
                    background_color = (0, 0.533, 0.412, 1)
                )
            )
            self.ids.scrolling_layout.add_widget(placeholder_streams[num])

class WatchScreen(Screen):
    pass

# the app only has to build itself, since everything else is contained in the .kv files
class MyMainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(WatchScreen())  
        sm.current = 'main_screen'
        return sm

if __name__ == "__main__":
    MyMainApp().run()