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

from kivy.core.window import Window
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.dictadapter import ListAdapter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.adapters.dictadapter import DictAdapter
from kivy.adapters.listadapter import ListAdapter
from kivy.base import EventLoop
import time
from kivy.clock import Clock
import json
from kivy.uix.popup import Popup
from kivy.logger import Logger
import datetime
from kivy.core.text import LabelBase
LabelBase.register(name="FreeMono",
                   fn_regular="FontFiles/FreeMono.ttf",
                   fn_bold="FontFiles/FreeMonoBold.ttf",
                   fn_italic="FontFiles/FreeMonoOblique.ttf",
                   fn_bolditalic="FontFiles/FreeMonoBoldOblique.ttf")
from kivy.uix.rst import RstDocument
from kivy.uix.tabbedpanel import TabbedPanelItem

Builder.load_file('newprojectform.kv')
Builder.load_file('generalmenu.kv')

# global variable
PERSON = ''


class LoginPage(AnchorLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)

    def on_focus(self, instance, value):
        if value:
            print('User focused', instance)
        else:  ## Check general.json to see if username exists already

            print('User defocused', instance)

    def on_text_validate(self):
        if self.check_user_exists(self.ids.un_input):
            self.ids.un_label.text = 'You exist'
        else:
            self.ids.pw_label.text = 'no'

    def on_enter(self, instance, value):
        print('User pressed enter in', instance)

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

    def check_upper(self):
        self.ids.statuslogin.text = ''
        self.ids.statuslogin.color = [1, 1, 1, 1]
        for x in self.ids.un_input.text:
            if x.isupper():
                self.ids.statuslogin.text = 'please use all \nlowercase characters'
                self.ids.statuslogin.color = [1, 0, 0, 1]
            else:
                pass

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
            self.add_widget(Factory.GeneralMenu())
        elif self.check_password(self.ids.un_input.text, self.ids.pw_input.text) == False:
            self.ids.statuslogin.text = 'Please try your credentials again'
        else:
            self.ids.statuslogin.text = self.check_password(self.ids.un_input.text, self.ids.pw_input.text)



PROJECT =''

class MainView(BoxLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        super(MainView, self).__init__(**kwargs)
   # def build(self):
       # global store
        project_store = JsonStore('projectlist.json')
        self.list_adapter = ListAdapter(data=[("Project " + r + ' ' + project_store[r]['profile']['projecttitle'])
                                              for r in project_store.keys()],
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


class OpenExistingProject(BoxLayout):
    import radar_chart

    def make_radar(self):
        return

    pass

# from kivy.garden.cefpython import CefBrowser, cefpython
from kivy.app import App

# class CefBrowserApp(App):
#     def build(self):
#         return CefBrowser(start_url='http://kivy.org')

from kivy.uix.checkbox import CheckBox

class MyCheckBox(GridLayout):
    # pass
    def on_checkbox_active(self, value):
        if value:
            print('The checkbox', self, 'is active')
        else:
            print('The checkbox', self,'is inactive')
    def abc(self):
        self.ids._PDSV.text = '55'

dropdown = DropDown()


lisp =[['Functionality', 'functionality'] ,
       ['Operational \nEnvironment', 'operationalenvironment'],
       ['Health, Safety, \nand Environment','healthsafetyandenvironment'],
       ['Manageability', 'manageability'],
       ['Security', 'security'],
       ['Interfacing \nSystems', 'interfacingsystems']]
print [(lisp[i][0]) for i in range(0,5)]


class RootHome(BoxLayout):




    def abc(self, value):
       # _PDSV.text = value
        return

    def show_report(self):
        self.clear_widgets()
        report = LoginPage()
        self.add_widget(report)


    def callback(self):
        print 'banana cakes'
        self.parent.parent.parent.show_report()

    btn = Button(text = 'Main\n Menu', size_hint_y = None, height =64,  on_press=callback)
    dropdown.add_widget(btn)

    btn = Button(text = ' Edit Design\n Requirements', size_hint_y = None, height =44, on_press=callback)
    dropdown.add_widget(btn)

    btn = Button(text = ' Upload Design\n Sketch', size_hint_y = None, height =44, on_press=callback)
    dropdown.add_widget(btn)

    # def __init__(self, **kwargs):
    def on_touch_up(self, touch):
        if touch.button == 'right':
            self.add_widget(dropdown)



    def show_project_view(self):

        self.clear_widgets()
        self.add_widget(ViewProject())

    def show_proposed_design_solution(self):
        self.clear_widgets()
        self.add_widget(DesignSolutionHelpContent())
        self.add_widget(DefineProposedDesignSolution())

    def show_define_design_requirements(self):
        self.clear_widgets()
        self.add_widget(DefineDesignRequirements())

    def show_new_project_form(self):
        self.clear_widgets()
        projectform = NewProjectForm()
        self.add_widget(projectform)

    def store_stuff(self):

        self.store[PROJECT]['profile']['projectid'] = PROJECT

        print PROJECT
        print self.store[PROJECT]






    def color_change(self, score):
        codes = [[0.57254902, 0.93333333, 0.54117647, 1.],
                 [0.97647059, 1., 0., 1.],
                 [0.98823529, 0.64313725, 0., 1.],
                 [0.98431373, 0., 0.1372549, 1.]]
        list = [1, 2, 3, 4]
        ind = find(score, list)
        return codes[ind]

from kivy.uix.accordion import Accordion
from kivy.uix.accordion import AccordionItem


class ViewProjectFormTemplate(Accordion):
    global PROJECT
    def show_screenthree(self):
        self.ids._sm.current = 'screenthree'




class DefineDesignRequirements(TabbedPanel):
    pass

class TabbedPanelTemplate(TabbedPanelItem):
    pass
    # def on_call(self,store):
    #     self.spit_store(self.ids.yes.text, self.ids.DR_F.text, self.ids.DRR_F.text, self.ids.DRIS_F.value, self.ids.DRISR_F.text, store)
    # def __init__(self):
    #     "content": {"designrequirements": {"manageability": {"drisr": " ",
    #                                                                       "drr": " ",
    #                                                                       "dr": " ",
    #                                                                       "dris": " "},
    #                                                     "healthsafetyandenvironment": {"drisr": " ",
    #                                                                                    "drr": " ",
    #                                                                                    "dr": " ",
    #                                                                                    "dris": " "},
    #                                                     "operationalenvironment": {"drisr": " ",
    #                                                                                "drr": " ",
    #                                                                                "dr": " ",
    #                                                                                "dris": " "},
    #                                                     "functionality": {"drisr": " ",
    #                                                                       "drr": " ",
    #                                                                       "dr": " ",
    #                                                                       "dris": " "},
    #                                                     "security": {"drisr": " ",
    #                                                                  "drr": " ",
    #                                                                  "dr": " ",
    #                                                                  "dris": " "},
    #                                                     "interfacingsystems": {"drisr": " ",
    #                                                                            "drr": " ",
    #                                                                            "dr": " ",
    #                                                                            "dris": " "}},
    #                              "solutions": {"sol2": "2", "sol1": "1"}}


from kivy.config import Config

class DesignSolutionTemplate(TabbedPanelItem):
    def form2_store(self, text, DRCB, PDSA, PDSC, PDSCS, PDSV):
        print PROJECT
        self.store[PROJECT]["content"] = {'designsolution1': {'functionality': '', 'operatingenvironment':''}}
        print text
        if text == lisp[0][0]:
            print DRCB
            print PDSA
            print PDSC
            print PDSCS
            print PDSV

            ## ## ## ## ## ## ##
            self.store[PROJECT]['content']['designsolution1'][lisp[0][1]] = {"drcb": DRCB,
                                                                        "pdsa": PDSA,
                                                                        "pdsc": PDSC,
                                                                        "pdscs": PDSV}
            print self.store[PROJECT]['content']
            print lisp[0][1]

        elif text == lisp[1][0]:
            self.store[PROJECT]['content']['designsolution1'][lisp[1][1]] = {"drcb": DRCB,
                                                                        "pdsa": PDSA,
                                                                        "pdsc": PDSC,
                                                                        "pdscs": PDSCS}
            print self.store[PROJECT]['content']['designsolution1']

        # elif text == lisp[2][0]:
        #     print lisp[2][1]
        #
        #     store[PROJECT]['content']['designsolution1'][lisp[2][1]] = {"drcb": DRCB,
        #                                                                 "pdsa": PDSA,
        #                                                                 "pdsc": PDSC,
        #                                                                 "pdscs": PDSCS}
        # elif text == lisp[3][0]:
        #     print lisp[3][1]
        #     store[PROJECT]['content']['designsolution1'][lisp[3][1]] = {"drcb": DRCB,
        #                                                                 "pdsa": PDSA,
        #                                                                 "pdsc": PDSC,
        #                                                                 "pdscs": PDSCS}
        #
        # elif text == lisp[4][0]:
        #     print lisp[4][1]
        #     store[PROJECT]['content']['designsolution1'][lisp[4][1]] = {"drcb": DRCB,
        #                                                                 "pdsa": PDSA,
        #                                                                 "pdsc": PDSC,
        #                                                                 "pdscs": PDSCS}
        # elif text == lisp[5][0]:
        #     print lisp[5][1]
        #     store[PROJECT]['content']['designsolution1'][lisp[5][1]] = {"drcb": DRCB,
        #                                                                 "pdsa": PDSA,
        #                                                                 "pdsc": PDSC,
        #                                                                 "pdscs": PDSCS}
        else:
            pass


class Poppy(Popup):
    def on_text_validate(self):
        if self.ids.popupinput.text.isalpha():
            self.dismiss()
        else:
            self.title = 'Your input must \nonly contain letters'
class DefineProposedDesignSolution(TabbedPanel):
    pass

class DesignSolutionHelpContent(BoxLayout):
    pass



# class DesignSolutionTemplate(TabbedPanelItem):

    # def on_save(self, value,DRCB, PDSA, PDSC, PDSCS, PDSV ):
    #     return
    #  pass


from kivy.uix.floatlayout import FloatLayout
PROJECT=''

class NewProjectForm(FloatLayout):

    def check_user_exists(self, project):
       # project_store = JsonStore('projectlist.json')
        pr = project
        key = '%s' % (pr)
        for each in store:
            print store.get(each)['profile']['projecttitle']
        # p= project_store.get("users")
        # list = json.dumps(p.keys())
        # if key in p:
        if 'M' in project:
            popup = Popup(title='Test popup', size_hint=(.3, .3),
                          content=Label(text='That project name already exists.\n Please enter a new Project Title'),
                          auto_dismiss=True)
            popup.open()
            return True
        else:
            False
    def project_set_global(self):
       # project_store = JsonStore('projectlist.json')
        nn= self.ids._projectidnumber.text
        Window.set_title('You are signed in as %s' % (PERSON) + '\t' + LOGINTIME + nn)
        store[nn] = {"profile":{"projecttitle": "Scuba Mask Rebuild",
                                        "projectid": "124",
                                        "creator": "Bartholomew",
                                        "created_at": "April 9, 2015",
                                        "timeinproject": "1026 seconds"}
                     }
        return PERSON






class StorageKinds():
    pass


class ViewProject(FloatLayout):
    pass
class ProjectSolutionForm(BoxLayout):
    pass

from kivy.input.providers.mouse import MouseMotionEvent
from os.path import join

class Form1App(App):
    def build(self):
        self.icon = 'cropped_lumpy2.png'
        Config.set("input", "mouse", "mouse, disable_multitouch")
        root = RootHome()
        self.title = 'hello'
        self.store = JsonStore('projectlist.json')
        from kivy.core.window import Window
        # Window.borderless = True
        return root

    def on_start(self):
        time.sleep(.5)

    def g_store(self):
        w = self.store
        return w

    def spit_store(self, text,DR_F, DRR_F, DRIS_F, DRISR_F):
       # store = JsonStore('projectlist.json')
        print text
        print PROJECT

        g = self.store.get(PROJECT)
        print g
        if text == lisp[0][0]:
            print DR_F
            print type(DRR_F)
            print DRIS_F
            print DRISR_F
            g['content']['designrequirements'][lisp[0][1]] = {"drisr": DRISR_F, "drr": DRR_F, "dr": DR_F, "dris": DRIS_F}

            print g
            print g['content']


            # store[PROJECT]= {"content":{'designrequirements':{ lisp[0][1] : { 'drisr':DRISR_F,
            #                                                                      'drr':DRR_F,
            #                                                                      'dr':DR_F,
            #                                                                      'dris':DRIS_F}}}}


            print lisp[0][1]

        elif text == lisp[1][0]:
            print lisp[1][1]
            store[PROJECT]['content']['designrequirements'][lisp[1][1]] = {"drisr": DRISR_F, "drr": DRR_F, "dr": DR_F, "dris": DRIS_F}
            print store[PROJECT]['content']
        elif text == lisp[2][0]:
            print lisp[2][1]
            store[PROJECT]['content']['designrequirements'][lisp[2][1]] = {"drisr": DRISR_F, "drr": DRR_F, "dr": DR_F, "dris": DRIS_F}
        elif text == lisp[3][0]:
            print lisp[3][1]
        elif text == lisp[4][0]:
            print lisp[4][1]
        elif text == lisp[5][0]:
            print lisp[5][1]
        else:
            pass
        return store


if __name__ == '__main__':
    Form1App().run()
    # CefBrowserApp().run()
    #
    # cefpython.Shutdown()
