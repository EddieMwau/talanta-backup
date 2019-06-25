from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
import os

from kivymd.theming import ThemeManager

Builder.load_file('signup/signup.kv')


class SignupWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cancel_signup(self):
        self.parent.parent.current = 'scr_index'

    def register_user(self):
        firstname = self.ids.fname_field
        fname = firstname.text

        lastname = self.ids.lname_field
        lname = lastname.text

        username = self.ids.username_field
        uname = username.text

        emailadd = self.ids.email_field
        email = emailadd.text

        password = self.ids.pwd_field
        pwd = password.text

        confirm_pwd = self.ids.confirm_pwd_field
        c_pwd = confirm_pwd.text

        designation = self.ids.designation_field
        des = designation.text

        info = self.ids.info

        db = pymysql.connect('localhost', 'root', 'kidflash','talanta')
        cursor = db.cursor()
        cursor1 = db.cursor()

        sql = "INSERT INTO USERS(FIRST_NAME,LAST_NAME,USER_NAME,EMAIL,PASSWORD,DESIGNATION)" \
              " VALUES ('%s','%s','%s','%s','%s','%s')" % (fname,lname,uname,email,pwd,des)

        sql2 = "SELECT * FROM USERS"
        cursor1.execute(sql2)
        results = cursor1.fetchall()

        usernames = []
        emails = []
        for result in results:
            usernames.append(result[3])
            emails.append(result[4])

        try:
            if fname == '' or lname == '' or uname == '' or email == '' or pwd == '' or des not in ['artist', 'gallery', 'enthusiast']:
                info.text = '[color=#FF0000]please fill out all fields![/color]'
            elif uname in usernames:
                info.text = '[color=#FF0000]Username already exists. Try another![/color]'
            elif email in emails:
                info.text = '[color=#FF0000]Email address already exists![/color]'
            elif pwd != c_pwd:
                info.text = '[color=#FF0000]password mismatch![/color]'
            else:
                cursor.execute(sql)
                db.commit()
                # TODO: add clear widgets
                self.parent.parent.current = 'scr_si'
        except:
            db.rollback()
            # for debugging purposes
            print('error')

        db.close()


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Brown'
    title = "SignUp"
    main_widget = None

    def build(self):
        return ExampleTextFields()


Example().run()
