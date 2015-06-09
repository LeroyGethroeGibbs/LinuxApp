__author__ = 'karinamarie'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.storage.jsonstore import JsonStore
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.factory import Factory
from functionfile import check_password
from kivy.uix.dropdown import DropDown
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from functionfile import check_password
from kivy.adapters.dictadapter import DictAdapter
from kivy.adapters.listadapter import ListAdapter
from kivy.base import EventLoop
from kivy.core.window import Window
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.dictadapter import ListAdapter
from kivy.uix.button import Button

store = JsonStore('hello.json')

# Builder.load_file('loginpage.kv')
Builder.load_file('newprojectform.kv')
Builder.load_file('generalmenu.kv')

# global variable
PERSON = ''
from kivy.properties import ObjectProperty
import time
from kivy.clock import Clock


class LoginPage(AnchorLayout):
    def check_upper(self):
        self.ids.statuslogin.text = ''
        self.ids.statuslogin.color = [1, 1, 1, 1]
        for x in self.ids.un_input.text:
            if x.isupper():
                self.ids.statuslogin.text = 'please use all \nlowercase characters'
                self.ids.statuslogin.color = [1, 0, 0, 1]
            else:
                pass

    def login_set_global(self):
        global PERSON
        self.ids.loginbutton.text = self.ids.un_input.text
        PERSON = self.ids.un_input.text
        ### self.ids.statuslogin.text = check_password(self.ids.un_input.text, self.ids.pw_input.text)
        if check_password(self.ids.un_input.text, self.ids.pw_input.text) == True:
            self.clear_widgets()
            Window.set_title('You are signed in as %s'%(PERSON))
            self.add_widget(Factory.GeneralMenu())
        elif check_password(self.ids.un_input.text, self.ids.pw_input.text) == False:
            self.ids.statuslogin.text = 'Please try your credentials again'
        else:
            self.ids.statuslogin.text = check_password(self.ids.un_input.text, self.ids.pw_input.text)




store = JsonStore('projectlist.json')

from random import randint

class MainView(BoxLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        super(MainView, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.list_adapter = ListAdapter(data=["Project #{0}\t".format(i) + '{0}'.format(store[i]['profile']['projecttitle']) for i in store.keys()  ], cls=ListItemButton,
                                        sorted_keys=[])
        self.list_adapter.bind(on_selection_change=self.selection_change)
        list_view = ListView(adapter=self.list_adapter)
        self.add_widget(list_view)
        self.add_widget(Button(text="select random item", size_hint=(.3,.5),on_press=self.callback))

    def callback(self, instance):
        index = randint(0, 9)
        # index = len(self.data)
        # index= range(9)
        self.change_from_code = True
        if not self.list_adapter.get_view(index).is_selected:
            self.list_adapter.get_view(index).trigger_action(duration=0)
        self.change_from_code = False

    def selection_change(self, adapter, *args):
        if self.change_from_code:
            print "selection change from code"
        else:
            print "selection changed by click"
class OpenExistingProject(BoxLayout):
    import radar_chart
    def make_radar(self):

        return

    pass

class RootHome(BoxLayout):
    # def __init__(self, **kwargs):

    def show_report(self):
        self.clear_widgets()
        report = LoginPage()
        self.add_widget(report)

    def show_define_design_requirements(self):
        self.clear_widgets()
        self.add_widget(DefineDesignRequirements())

    def show_new_project_form(self):
        self.clear_widgets()
        projectform = NewProjectForm()
        self.add_widget(projectform)

    def color_change(self, score):
        codes = [[0.57254902, 0.93333333, 0.54117647, 1.],
                 [0.97647059, 1., 0., 1.],
                 [0.98823529, 0.64313725, 0., 1.],
                 [0.98431373, 0., 0.1372549, 1.]]
        list = [1, 2, 3, 4]
        ind = find(score, list)
        return codes[ind]


class CustomDropDown(DropDown):
    pass


class DefineDesignRequirements(TabbedPanel):
    pass
class NewProjectForm(BoxLayout):
    pass
class StorageKinds():
    pass


class Form1App(App):
    def build(self):
        root = RootHome()
        self.title = 'hello'
        from kivy.core.window import Window
        # Window.borderless = True


        return root

    def on_start(self):
        time.sleep(.5)


    def octopus(self, username):
        un = username
        print un
        self.title='Welcome %s'%(un)

if __name__ == '__main__':
    Form1App().run()
