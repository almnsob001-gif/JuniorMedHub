"""
JuniorMed Hub - Milestone 1
A pocket reference for medical residents and students.
"""

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


KV = """
ScreenManager:
    WelcomeScreen:
    DisclaimerScreen:
    HomeScreen:


<WelcomeScreen>:
    name: "welcome"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(24)
        spacing: dp(16)
        Widget:
        MDLabel:
            text: "JuniorMed Hub"
            halign: "center"
            font_style: "H3"
            theme_text_color: "Primary"
        MDLabel:
            text: "A pocket reference for medical residents and students"
            halign: "center"
            font_style: "Subtitle1"
        Widget:
        MDRaisedButton:
            text: "Get Started"
            pos_hint: {"center_x": 0.5}
            on_release: app.go_to_disclaimer()
        Widget:


<DisclaimerScreen>:
    name: "disclaimer"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(12)
        MDLabel:
            text: "Important Medical Notice"
            font_style: "H5"
            halign: "center"
            size_hint_y: None
            height: dp(48)
        ScrollView:
            MDLabel:
                text: app.disclaimer_text
                size_hint_y: None
                height: self.texture_size[1]
                markup: True
        MDRaisedButton:
            text: "I Understand and Agree"
            pos_hint: {"center_x": 0.5}
            on_release: app.accept_disclaimer()


<HomeScreen>:
    name: "home"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(16)
        spacing: dp(12)
        MDLabel:
            text: "JuniorMed Hub"
            font_style: "H5"
            halign: "center"
            size_hint_y: None
            height: dp(48)
        MDLabel:
            text: "Version 0.1.0"
            halign: "center"
            font_style: "Caption"
            size_hint_y: None
            height: dp(24)
        Widget:
        MDRaisedButton:
            text: "Drug Guide  (coming soon)"
            disabled: True
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
        MDRaisedButton:
            text: "Medical Calculators  (coming soon)"
            disabled: True
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
        MDRaisedButton:
            text: "Clinical Protocols  (coming soon)"
            disabled: True
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
        MDRaisedButton:
            text: "About"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            on_release: app.show_about()
        Widget:
"""


class WelcomeScreen(Screen):
    pass


class DisclaimerScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class JuniorMedHubApp(MDApp):
    disclaimer_text = (
        "[b]JuniorMed Hub[/b] is an educational reference tool for "
        "healthcare professionals and students.\n\n"
        "The information provided is for [b]general educational purposes "
        "only[/b] and does [b]NOT[/b] constitute medical advice, "
        "diagnosis, or treatment.\n\n"
        "Always verify drug doses, formulas, and protocols against "
        "official sources and your institution's guidelines before "
        "applying them in clinical practice.\n\n"
        "The developers assume no liability for any clinical decisions "
        "made based on this application."
    )

    def build(self):
        self.title = "JuniorMed Hub"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def go_to_disclaimer(self):
        self.root.current = "disclaimer"

    def accept_disclaimer(self):
        self.root.current = "home"

    def show_about(self):
        dialog = MDDialog(
            title="About JuniorMed Hub",
            text=(
                "Version 0.1.0\n\n"
                "A pocket reference for medical residents, "
                "interns, and students.\n\n"
                "Built with Kivy & KivyMD."
            ),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *a: dialog.dismiss(),
                )
            ],
        )
        dialog.open()


if __name__ == "__main__":
    JuniorMedHubApp().run()
