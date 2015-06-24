__author__ = 'karinamarie'
##

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.pagelayout import PageLayout
from kivy.uix.tabbedpanel import TabbedPanel
import os, datetime
from kivy.factory import Factory
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from kivy.uix.popup import Popup
#import plotly as py
from kivy.lang import Builder

from kivy.garden.modernmenu import ModernMenu
Builder.load_file('loginpage.kv')


class MyPageLayout(PageLayout):
    pass

class RootHome(BoxLayout):

    def show_report(self):
        self.clear_widgets()
        #report = Factory.ProjectReport()
        report = Factory.LoginPage()
        self.add_widget(report)
        #self.add_widget(Image(source='cropped_lumpy2.png'))

        #get all back



    def show_radar(self):
        self.clear_widgets()
        x = WidgetOne()
        self.add_widget(x)
    def trial(self):
        #popup = Popup(title='Test popup',content=Label(text='Hello world'),size_hint=(None, None), size=(400, 400))
        popup = Popup(title='Test popup',content=LoginScreen(),size_hint=(None, None), size=(400, 400))

        popup.open()


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        #self.password.bind(on_text_validate= popup.dismiss())


# class ProjectForm(PageLayout):
#   pass

class WidgetOne(BoxLayout):
    def make_radar_chart(self):
        x = np.linspace(0, 1)
        y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

        plt.fill(x, y, 'r')
        plt.grid(True)
        return plt.show()



class WidgetTwo(BoxLayout):
    pass

class StartUpForm(ScreenManager):
    pass
class Picture(Scatter):

    source = StringProperty(None)

class BananaApp(App):
    def build(self):
        root = RootHome()
        return RootHome()


    def save(self, something, number):
        fob = open('test.txt', 'w')
        fob.write(something + "\n")
        fob.write(number)
        fob.close()


if __name__ == '__main__':
    BananaApp().run()
