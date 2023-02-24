from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen


class ScreenOne(
                MDScreen(
                    MDLabel(text="From the Marshall K12 Schools Foundation",
                            halign="center",
                            pos_hint={"center_x": 0.5, "center_y": 0.8}
                            ),

                    MDRectangleFlatButton(
                        text="Welcome",
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                                          )
                    )
            ):
    pass

