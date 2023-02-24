from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.list import MDList
from kivymd.uix.floatlayout import MDFloatLayout


class B1(MDRaisedButton):
    text = 'hello world'
    pass


class MobileView(MDScreen):
    def AddLis(self):
        for i in range(1):
            count = 1
            for child in self.ids.list.children[:]:
                count += 1
            self.ids.list.add_widget(
                SwipeToDeleteItem(text=f"Player {count}",
                                  id=str(i),
                                  )
            )

    def hide_w(self):
        for i in range(20):
            count = 1
            for child in self.children[:]:
                count += 1

            if count > 2:
                self.remove_widget(self.card)
            elif count == 0:
                self.add_widget(self.card)

    pass


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass


class List(MDList):
    def remove_item(self):
        count = 0
        for child in self.children[:]:
            self.remove_widget(child)
            count += 1
            if count == 1:
                return print(count)
    id = list
    pass


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    pass


class Float(MDFloatLayout):
    pass


class Intro(MDScreen):
    name = "Intro"


class ResponsiveView(MDResponsiveLayout, MDScreen):
    name = 'ResponsiveView'

    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()
        pass
    pass


class WM(MDScreenManager):
    sm = MDScreenManager
    sm.current_screen = Intro()
    print(sm.current_screen)
    #wm = ResponsiveView()
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '700'
        self.layout = Float()

    def build(self):
        return WM()


MainApp().run()
