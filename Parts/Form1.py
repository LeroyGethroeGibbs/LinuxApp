__author__ = 'karinamarie'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.button import Button
from kivy.core.text import LabelBase




class RootHome(TabbedPanel):
    def color_change(self, score):
        codes = [[ 0.57254902,  0.93333333,  0.54117647,  1.],
                 [ 0.97647059,  1.,          0.,          1.],
                 [ 0.98823529,  0.64313725,  0.,          1.],
                 [ 0.98431373,  0.,          0.1372549,   1.]]
        list = [1,2,3,4]
        ind = find(score, list)
        return codes[ind]


class Form1App(App):
    def build(self):
        return RootHome()
     #   return Button(text='Hello World')

if __name__ == '__main__':

    Form1App().run()