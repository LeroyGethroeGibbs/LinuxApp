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
from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
from kivy.graphics.context_instructions import Color

from kivy.properties import ListProperty, ObjectProperty

import random




class ScatterTextWidget(BoxLayout):
    text_colour = ListProperty([1,0,0,1])

    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)


    def change_label_colour(self, *args):
        colour = [random.random() for i in xrange(3)] + [1]
        self.text_colour = colour

class BananaApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == '__main__':
    BananaApp().run()
