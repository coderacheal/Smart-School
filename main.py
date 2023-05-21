from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivymd.uix.button import MDRoundFlatButton, MDRectangleFlatButton, MDFlatButton
from kivymd.uix.behaviors import HoverBehavior
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemableBehavior
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivy.config import Config
from matplotlib import pyplot as plt
from kivy.core.text import LabelBase
import src.exceptions as exceptions
import src.logins as logins
import src.staff as staff
from students import students 
import src.manage_setting as manage_setting
import src.analytics as analytics
# import payments
from src.payments import fees, expenditure

class Home(Screen):
    def logout(self):
        self.empty_class_dialog = MDDialog(
            title="Logging out...",
            text="Are you sure you want to log out?",
            radius=[40, 7, 40, 7],
            auto_dismiss=False,
            buttons=[
                MDRectangleFlatButton(
                    text="YES", on_release=self.close_dialog_and_logout),
                MDFlatButton(
                    text="NO", on_release=self.close_dialog
                ),
            ],
        )
        self.empty_class_dialog.open()

    def close_dialog(self, obj):
        self.empty_class_dialog.dismiss()

    def close_dialog_and_logout(self, obj):
        self.empty_class_dialog.dismiss()
        self.manager.current = "log in"


class Info(Screen):
    def logout(self):
        self.empty_class_dialog = MDDialog(
            title="Logging out...",
            text="Are you sure you want to log out?",
            radius=[40, 7, 40, 7],
            buttons=[
                MDRectangleFlatButton(
                    text="YES", on_release=self.close_dialog_and_logout),
                MDFlatButton(
                    text="NO", on_release=self.close_dialog
                ),
            ],
        )
        self.empty_class_dialog.open()

    def close_dialog(self, obj):
        self.empty_class_dialog.dismiss()

    def close_dialog_and_logout(self, obj):
        self.empty_class_dialog.dismiss()
        self.manager.current = "log in"



class WindowManager(ScreenManager):
    pass


class SmartTracker(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("Styles/main.kv")


if __name__ == "__main__":
    SmartTracker().run()
