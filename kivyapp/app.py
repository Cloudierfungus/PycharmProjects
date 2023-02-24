from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.toolbar import MDBottomAppBar
from kivy.event import EventDispatcher
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.widget import MDWidget
store = JsonStore('stow.json')


class MainApp(MDApp):
    text_input = ObjectProperty()
    store = JsonStore('stow.json')
    save = StringProperty()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "A400"
        pass


class MobileView(MDScreen):
    pass


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass


class WindowManager(MDScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.store = JsonStore('stow.json')

    def savetm(self):
        if self.store.exists('Teams'):
            self.store.delete('Teams',)
            self.store.put('Teams',
                           teamone=self.ids.team_one.text,
                           teamtwo=self.ids.team_two.text
                           )
        else:
            self.store.put('Teams',
                           teamone=self.ids.team_one.text,
                           teamtwo=self.ids.team_two.text
                           )

    def rem(self):

        self.ids.memb.remove_widget()

    class BoxS1(MDTextField):
        pass

    class BoxS2(MDTextField):
        pass

    pass


class ScreenOne(MDScreen):
    pass


class ScreenTwo(MDScreen):
    pass


class TeamScr(MDScreen):
    class Mbr1(MDTextField):
        pass

    class Mbr2(MDTextField):
        pass

    trait = property(Mbr2)

    class Member(Mbr2):
        pass

    class Widget(MDWidget, Member):
        def rem(self):
            self.remove_widget(self)
        pass

    class Layout1(MDGridLayout):
        def ad(self):
            ab = 0
            for child in self.children[:]:
                ab += 1
            if ab > 15:
                return
            elif ab < 15:
                mbr = TeamScr.Mbr2
                return self.add_widget(TeamScr.Widget())

        def rem(self):
            count = 0
            for child in self.children[:]:
                self.remove_widget(child)
                count += 1
                if count == 1:
                    return
                else:
                    return print(count)

        pass

    pass


if __name__ == '__main__':
    MainApp().run()


