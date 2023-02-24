import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import ObjectProperty, NumericProperty
from kivymd.uix.card import MDCard


class MainApp(MDApp):
    def build(self):
        pass


'''

class MainWidget(MDWidget):
    pass

# def build(self):
#    self.theme_cls.primary_palette = 'Red'


class ScreenOne(MDScreen):
    def build(self):
        pass


class ScreenTwo(MDScreen):
    def build(self):
        pass
'''


class ScreenOne(MDScreen):
    pass


class ScreenTwo(MDScreen):
    pass


class WindowManager(MDScreenManager):
    pass


class MD3Card(MDCard):

    text = str('hello world')
    pass


if __name__ == '__main__':
    app = MainApp()
    app.run()


Builder.load_file('main.kv')