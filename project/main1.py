from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from login.login import SigninWindow
from landing.landing import LandingWindow
from index.index import IndexWindow
from signup.signup import SignupWindow
from welcome.welcome import WelcomeWindow
from category.category import CategoryWindow
from errorpage.errorpage import ErrorPageWindow
from upload.upload import UploadWindow

Builder.load_file('main/main.kv')


class MainWindow(BoxLayout):

    index_widget = IndexWindow()
    landing_widget = LandingWindow()
    login_widget = SigninWindow()
    signup_widget = SignupWindow()
    welcome_widget = WelcomeWindow()
    category_widget = CategoryWindow()
    error_widget = ErrorPageWindow()
    upload_widget = UploadWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.scr_su.add_widget(self.signup_widget)
        self.ids.scr_si.add_widget(self.login_widget)
        self.ids.scr_index.add_widget(self.index_widget)
        self.ids.scr_la.add_widget(self.landing_widget)
        self.ids.scr_welcome.add_widget(self.welcome_widget)
        self.ids.scr_category.add_widget(self.category_widget)
        self.ids.scr_error.add_widget(self.error_widget)
        self.ids.scr_upload.add_widget(self.upload_widget)


class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MainApp().run()
