from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os
from kivymd.theming import ThemeManager
import pymysql

#Builder.load_file('login/login.kv')


class LoginWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cancel_login(self):
        self.parent.parent.current = 'scr_index'
        
    def sign_up(self):
        self.parent.parent.current = 'scr_signup'

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text
 
        db = pymysql.connect('localhost', 'root', 'kidflash', 'talanta')
        cursor = db.cursor()

        sql = "SELECT * FROM USERS WHERE USER_NAME = '%s' AND PASSWORD = '%s' " % (uname, passw)

        cursor.execute(sql)
        users = cursor.fetchall()

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]username and/or password required[/color]'
        else:
            if users:
                self.ids.info.text = ''
                self.ids.username_field.text = ''
                self.ids.pwd_field.text = ''
                self.parent.parent.current = 'scr_browse'
            else:
                info.text = '[color=#FF0000]Invalid username or password[/color]'


class LoginApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Brown'
    title = ""
    main_widget = None

    def build(self):
        return LoginWindow()


LoginApp().run()
