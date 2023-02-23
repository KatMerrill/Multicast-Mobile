from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

# ScreenManager keeps track of all Screens
class WindowManager(ScreenManager):
    pass

class WatchScreen(Screen):
    pass

# class HomeScreen(Screen):
#     pass

Window.clearcolor = (255, 255, 255, 255)
# used to load a file other than the default, which is my.kv
kv = Builder.load_file("myApp.kv")

STREAM_COUNT = 3

# all classes referred to in the .kv files don't need any code here. Note that this inherits from Screen
class HomeScreen(Screen):
    def on_enter(self):
        placeholder_streams = []
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



# the app only has to build itself, since everything else is contained in the .kv files
class MyMainApp(App):
    def build(self):
        Window.maximize()
        return kv

if __name__ == "__main__":
    MyMainApp().run()