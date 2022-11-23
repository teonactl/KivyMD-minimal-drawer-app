from kivy.lang import Builder
from kivy.properties import  ObjectProperty
from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView


KV = '''

<ContentNavigationDrawer>
    id : c_n_draw

    MDList:
        id: cd_list

        OneLineListItem:
            id : pag1_nav
            text: "Pag 1"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "screen1"

        OneLineListItem:
            id: pag2_nav
            text: "Pag 2"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "screen2"
  
        OneLineListItem:
            id: pag3_nav
            text: "Pag 3"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "screen3"

MDScreen:
    name : "main_scr"
    id: main

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            id : topbar_id
            elevation: 4
            title: "Minumum App"
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationLayout:
            x: topbar_id.height
            size_hint_y: 1 - topbar_id.height/root.height

            ScreenManager:
                id: screen_manager

                MDScreen:
                    name: "screen1"
                    MDBoxLayout
                        orientation: 'vertical'
                        MDLabel : 
                            text : "Screen 1"
                            pos_hint: {'x': 0.5, 'y': 0.5}
                MDScreen:
                    name: "screen2"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDLabel : 
                            text : "Screen 2"
                            pos_hint: {'x': 0.5, 'y': 0.5}

                MDScreen:
                    name :"screen3"
                    MDBoxLayout:
                        orientation: "vertical"
                        padding : 20
                        MDLabel : 
                            text : "Screen 3"
                            pos_hint: {'x': 0.5, 'y': 0.5}

                        MDSpinner:
                            size_hint: None, None
                            size: dp(46), dp(46)
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            active: True

                  
                   

            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)

                ContentNavigationDrawer:

                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

'''


class ContentNavigationDrawer(ScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()



class BandiApp(MDApp):

    def build(self):
               
        return   Builder.load_string(KV) 



if __name__ == "__main__":
    BandiApp().run()
