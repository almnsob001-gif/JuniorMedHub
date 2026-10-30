from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.label import Label
from kivy.core.window import Window
import traceback
from kivy.utils import platform

# --- كود إجبار الوضع العمودي على أندرويد ---
if platform == 'android':
    try:
        from jnius import autoclass
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        activity.setRequestedOrientation(1) # 1 = Portrait
    except Exception as e:
        print("Could not force portrait:", e)
# -------------------------------------------

KV = """
ScreenManager:
    WelcomeScreen:
    DisclaimerScreen:
    HomeScreen:

# ==========================================
# شاشة الترحيب
# ==========================================
<WelcomeScreen>:
    name: "welcome"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(24)
        spacing: dp(20)
        
        Widget:
        
        MDIcon:
            icon: "stethoscope"
            halign: "center"
            font_size: dp(100)
            theme_text_color: "Primary"
            pos_hint: {"center_x": 0.5}
            size_hint_y: None
            height: dp(120)
            
        MDLabel:
            text: "JuniorMed Hub"
            halign: "center"
            font_style: "H3"
            theme_text_color: "Primary"
            bold: True
            size_hint_y: None
            height: dp(80)
            
        MDLabel:
            text: "Your pocket reference for clinical practice."
            halign: "center"
            font_style: "Subtitle1"
            text_size: self.width, None
            size_hint_y: None
            height: dp(60)
            
        Widget:
        
        MDFillRoundFlatButton:
            text: "Get Started"
            font_size: dp(18)
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            on_release: app.go_to_disclaimer()
            
        Widget:

# ==========================================
# شاشة إخلاء المسؤولية
# ==========================================
<DisclaimerScreen>:
    name: "disclaimer"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(16)
        spacing: dp(16)
        
        MDLabel:
            text: "Important Medical Notice"
            font_style: "H5"
            halign: "center"
            bold: True
            theme_text_color: "Primary"
            size_hint_y: None
            height: dp(60)
            
        MDCard:
            orientation: "vertical"
            padding: dp(20)
            radius: [20,]
            elevation: 4
            size_hint_y: 0.8
            pos_hint: {"center_x": 0.5}
            
            ScrollView:
                MDLabel:
                    text: app.disclaimer_text
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    markup: True
                    
        MDFillRoundFlatButton:
            text: "I Understand and Agree"
            font_size: dp(16)
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.9
            on_release: app.accept_disclaimer()

# ==========================================
# الشاشة الرئيسية
# ==========================================
<HomeScreen>:
    name: "home"
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "JuniorMed Hub"
            elevation: 4
            left_action_items: [["menu", lambda x: app.show_about()]]
            
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(16)
                spacing: dp(16)
                size_hint_y: None
                height: self.minimum_height
                
                MDCard:
                    size_hint_y: None
                    height: dp(80)
                    radius: [15,]
                    elevation: 2
                    padding: dp(16)
                    orientation: "horizontal"
                    spacing: dp(16)
                    MDIcon:
                        icon: "pill"
                        theme_text_color: "Primary"
                        font_size: dp(32)
                        size_hint_x: None
                        width: dp(40)
                    MDLabel:
                        text: "Drug Guide (Coming Soon)"
                        font_style: "H6"
                        valign: "center"
                        
                MDCard:
                    size_hint_y: None
                    height: dp(80)
                    radius: [15,]
                    elevation: 2
                    padding: dp(16)
                    orientation: "horizontal"
                    spacing: dp(16)
                    MDIcon:
                        icon: "calculator"
                        theme_text_color: "Primary"
                        font_size: dp(32)
                        size_hint_x: None
                        width: dp(40)
                    MDLabel:
                        text: "Medical Calculators (Coming Soon)"
                        font_style: "H6"
                        valign: "center"
                        
                MDCard:
                    size_hint_y: None
                    height: dp(80)
                    radius: [15,]
                    elevation: 2
                    padding: dp(16)
                    orientation: "horizontal"
                    spacing: dp(16)
                    MDIcon:
                        icon: "clipboard-text"
                        theme_text_color: "Primary"
                        font_size: dp(32)
                        size_hint_x: None
                        width: dp(40)
                    MDLabel:
                        text: "Clinical Protocols (Coming Soon)"
                        font_style: "H6"
                        valign: "center"
                        
                MDCard:
                    size_hint_y: None
                    height: dp(80)
                    radius: [15,]
                    elevation: 2
                    padding: dp(16)
                    orientation: "horizontal"
                    spacing: dp(16)
                    ripple_behavior: True
                    on_release: app.show_about()
                    MDIcon:
                        icon: "information"
                        theme_text_color: "Primary"
                        font_size: dp(32)
                        size_hint_x: None
                        width: dp(40)
                    MDLabel:
                        text: "About"
                        font_style: "H6"
                        valign: "center"
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
        try:
            self.title = "JuniorMed Hub"
            self.theme_cls.primary_palette = "Teal"
            self.theme_cls.theme_style = "Light"
            return Builder.load_string(KV)
        except Exception:
            error_trace = traceback.format_exc()
            print(error_trace)
            return Label(
                text=error_trace,
                text_size=(Window.width * 0.9, None),
                halign="center",
                valign="middle"
            )

    def go_to_disclaimer(self):
        self.root.current = "disclaimer"

    def accept_disclaimer(self):
        self.root.current = "home"

    def show_about(self):
        dialog = MDDialog(
            title="About JuniorMed Hub",
            text="Version 0.1.0\n\nBuilt with Kivy & KivyMD.\nDeveloped by a medical professional.",
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
