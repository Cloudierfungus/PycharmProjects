from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
from kivymd.uix.textfield import MDTextField


class SelectTeamsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.team1_name_input = MDTextField(hint_text='Enter Team 1 Name', pos_hint={'center_x': 0.5, 'center_y': 0.7},
                                            size_hint_x=None, width=300)
        self.team2_name_input = MDTextField(hint_text='Enter Team 2 Name', pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                            size_hint_x=None, width=300)

        self.add_widget(
            MDLabel(text='Select Teams', halign='center', font_style='H5', pos_hint={'center_x': 0.5, 'center_y': 0.9}))
        self.add_widget(self.team1_name_input)
        self.add_widget(self.team2_name_input)

        self.next_button = MDRectangleFlatButton(text='Next', pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                                 size_hint_x=None, width=300, on_release=self.go_to_score_screen)
        self.add_widget(self.next_button)

    def go_to_score_screen(self, *args):
        team1_name = self.team1_name_input.text
        team2_name = self.team2_name_input.text

        if team1_name and team2_name:
            self.manager.team1_name = team1_name
            self.manager.team2_name = team2_name
            self.manager.current = 'score_screen'


class ScoreScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.team1_label = MDLabel(text=self.manager.team1_name, font_style='H5', halign='center',
                                   pos_hint={'center_x': 0.2, 'center_y': 0.9})
        self.team2_label = MDLabel(text=self.manager.team2_name, font_style='H5', halign='center',
                                   pos_hint={'center_x': 0.8, 'center_y': 0.9})

        self.team1_score = 0
        self.team2_score = 0

        self.team1_score_label = MDLabel(text=str(self.team1_score), halign='center',
                                         pos_hint={'center_x': 0.2, 'center_y': 0.5})
        self.team2_score_label = MDLabel(text=str(self.team2_score), halign='center',
                                         pos_hint={'center_x': 0.8, 'center_y': 0.5})

        self.team1_add_button = MDIconButton(icon='plus', pos_hint={'center_x': 0.2, 'center_y': 0.3},
                                             on_release=self.add_to_team1_score)
        self.team2_add_button = MDIconButton(icon='plus', pos_hint={'center_x': 0.8, 'center_y': 0.3},
                                             on_release=self.add_to_team2_score)

        self.add_widget(self.team1_label)
        self.add_widget(self.team2_label)
        self.add_widget(self.team1_score_label)
        self.add_widget(self.team2_score_label)
