from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Gray'
    pass

    sm = MDScreenManager()

    def scrch(self, sm):
        return sm.current(self.root.ids.Dash)

    class WM(MDScreenManager):
        pass

    pass


class CompL(MDLabel):
    pass


class MobileView(MDScreen):
    screen2 = MDScreen
    pass


class TabletView(MDScreen):
    pass


class ToolB(MDTopAppBar):
    pass


class DesktopView(MDScreen):
    pass


class Dash(MDScreen):
    pass


class MainM(MDScreen, MDResponsiveLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()
    pass


MainApp().run()