from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.cards import MDCardPost
from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivy.metrics import dp
from kivy.core.window import Window
import pymysql

Builder.load_file('browse/browse.kv')


class BrowseWindow(BoxLayout):
    def __init__(self, **kwargs:
		super().__init__(kwargs)


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Card Post"
    cards_created = False

    def build(self):
        self.screen = Factory.BrowseWindow()
        return self.screen

    def on_start(self):
        def callback_for_menu_items(text_item):
            toast(text_item)

        def callback(instance, value):
            if value and isinstance(value, int):
                toast('Set like in %d stars' % value)
            elif value and isinstance(value, str):
                toast('Repost with %s ' % value)
            elif value and isinstance(value, list):
                toast(value[1])
            else:
                toast('Delete post %s' % str(instance))

        instance_grid_card = self.screen.ids.grid_card
        buttons = ['facebook', 'vk', 'twitter']
        menu_items = [
            {'viewclass': 'MDMenuItem',
             'text': 'Example item %d' % i,
             'callback': callback_for_menu_items}
            for i in range(2)
        ]

        if not self.cards_created:
            self.cards_created = True
            # loop database; load from tables
            db = pymysql.connect('localhost', 'root', 'kidflash', 'talanta')
            cursor = db.cursor()
            sql = "SELECT * FROM USERS"
            cursor.execute(sql)
            results = cursor.fetchall()
            names = []
            for result in results:
                names.append(result[1])

            for i in range(len(names)):
                instance_grid_card.add_widget(
                    MDCardPost(name_data=names[i], text_post="card with text",
                               swipe=True, callback=callback,card_size=(dp(300),dp(150))))
                instance_grid_card.add_widget(
                    MDCardPost(source="./assets/kitten-1049129_1280.jpg",
                               tile_text="Little Baby",
                               tile_font_style="H5",
                               text_post="",
                               with_image=True,card_size=(dp(300),dp(300)), callback=callback,
                               buttons=buttons))


Example().run()
