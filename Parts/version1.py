# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:43:32 2015

@author: karinamarie
"""

__author__ = 'karinamarie'
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.storage.jsonstore import JsonStore
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.dropdown import DropDown
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.adapters.dictadapter import DictAdapter
from kivy.adapters.listadapter import ListAdapter
from kivy.base import EventLoop
from kivy.core.window import Window
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.dictadapter import ListAdapter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
import time
from kivy.clock import Clock
import json
from kivy.uix.popup import Popup
from kivy.logger import Logger
import datetime
from kivy.uix.accordion import Accordion

from kivy.uix.rst import RstDocument
from kivy.uix.tabbedpanel import TabbedPanelItem

Builder.load_file('generallayout.kv')

# global variable
PERSON = ''


class LoginPage(AnchorLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)

    def check_user_exists(self, username):
        general_store = JsonStore('general.json')
        un = username
        key = '%s' % (un)

        p = general_store.get("users")
        list = json.dumps(p.keys())
        if key in p:
            return True
        else:
            False

    def check_password(self, un, pw):
        general_store = JsonStore('general.json')
        key = '%s' % (un)

        p = general_store.get("users")
        list = json.dumps(p.keys())
        print list
        if key in p:
            matching_pw = json.dumps(general_store.get("users")[key])
            print("\nmatching_pw = " + matching_pw)
            print '%s' % (pw)

            if '"%s"' % (pw) == matching_pw:
                return True
            else:
                return False
        else:
            warning = 'username not found'
            return warning

    def login_set_global(self):
        global PERSON
        global LOGINTIME
        self.ids.loginbutton.text = self.ids.un_input.text
        PERSON = self.ids.un_input.text
        LOGINTIME = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        ### self.ids.statuslogin.text = check_password(self.ids.un_input.text, self.ids.pw_input.text)
        if self.check_password(self.ids.un_input.text, self.ids.pw_input.text) == True:
            self.clear_widgets()
            Window.set_title('You are signed in as %s' % (PERSON) + '\t' + LOGINTIME)
            self.add_widget(Factory.GeneralLayout())
        elif self.check_password(self.ids.un_input.text, self.ids.pw_input.text) == False:
            self.ids.statuslogin.text = 'Please try your credentials again'
        else:
            self.ids.statuslogin.text = self.check_password(self.ids.un_input.text, self.ids.pw_input.text)

class MainView(BoxLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        super(MainView, self).__init__(**kwargs)
        #project_store = JsonStore('projectlist.json')
        lis, project_store = FApp().other()

        print lis
        print project_store

        self.list_adapter = ListAdapter(data=[("Project " + r + ' ' + project_store[r]['profile']['projecttitle'])
                                        for r in lis],
                                        cls=ListItemButton,
                                        sorted_keys=[])
        self.list_adapter.bind(on_selection_change=self.callback)
        list_view = ListView(adapter=self.list_adapter)
        self.add_widget(list_view)

    def callback(self, instance):
        global PROJECT
        p_num= instance.selection[0].text.split(' ')[1]
        PROJECT = p_num
        print p_num
        print 'project'
        return PROJECT

class GeneralLayout(BoxLayout):
    pass
class RootHome(BoxLayout):

    def show_project_view(self):
        self.clear_widgets()
        self.add_widget(ViewProject())

class ViewProject(FloatLayout):
    pass

class ViewProjectFormTemplate(Accordion):

     def show_screenthree(self):
         self.ids._sm.current = 'screenthree'

class FApp(App):

    store = JsonStore('projectlist.json')

    def build(self):
        root = RootHome()
        return root

    def other(self):
        lis = self.store.keys()
        return lis, self.store

if __name__ == '__main__':
    FApp().run()
