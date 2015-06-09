__author__ = 'karinamarie'
from kivy.storage.jsonstore import JsonStore
from kivy.event import EventDispatcher
import json
import csv
storej = JsonStore('projectlist.json')

p=[]
for key in storej.keys():
    p.append(key)
print p
# Write CSV Header
#f.writerow(["pk", "model", "codename", "name", "content_type"])
for project in p:
    #define & clear lists for each project number
    list = []
    profilelist=[]
    contentlist=[]

    print project + ' project'

    file = ('%s.csv'%(project))
    f = csv.writer(open(file, "wb+"))


    for key in storej.get((project)):
        list.append(key)
    print list # [profile, content]
    for key in storej[project]['profile']:
        print key
        profilelist.append(key)
    print profilelist # [projectid, created_at, creator, timeinproject]

    for key in storej[project]['content']['designrequirements']:
        print key
        contentlist.append(key)
    print contentlist


    print '\n\n'
    f.writerow([project])
    f.writerow([list[0]])
    f.writerow([profilelist[0], storej[project]['profile']['%s'%(profilelist[0])]])
    f.writerow([profilelist[1], storej[project]['profile']['%s'%(profilelist[1])]])
    f.writerow([profilelist[2], storej[project]['profile']['%s'%(profilelist[2])]])
    f.writerow([profilelist[3], storej[project]['profile']['%s'%(profilelist[3])]])
    f.writerow([None])
    f.writerow([list[1]])
    f.writerow(['Design Requirments'])
    f.writerow([None, 'Design Requirments',
                'Design Requirment Rationale',
                'Design Requirment\n Importance Score',
                'Design Requirement\n Importance Score Rationale'])
    i=0
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drisr'],
                ])
    i=1
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drisr'],
                ])
    i=2
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drisr'],
                ])
    i=3
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drisr'],
                ])
    i=4
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drisr'],
                ])
    i=5
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s'%(contentlist[i])]['drisr'],
                ])
    #             x[1],
    #            x["content"]]
    #            )

    #             x["model"],
    #             x["fields"]["codename"],
    #             x["fields"]["name"],
    #             x["fields"]["content_type"]])

import wx
import wx.grid as gridlib

class MyGrid(gridlib.Grid):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        gridlib.Grid.__init__(self, parent)
        self.CreateGrid(12, 8)


        # test all the events
        self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.OnCellLeftClick)
        self.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK, self.OnCellRightClick)
        self.Bind(gridlib.EVT_GRID_CELL_LEFT_DCLICK, self.OnCellLeftDClick)
        self.Bind(gridlib.EVT_GRID_CELL_RIGHT_DCLICK, self.OnCellRightDClick)

        self.Bind(gridlib.EVT_GRID_LABEL_LEFT_CLICK, self.OnLabelLeftClick)
        self.Bind(gridlib.EVT_GRID_LABEL_RIGHT_CLICK, self.OnLabelRightClick)
        self.Bind(gridlib.EVT_GRID_LABEL_LEFT_DCLICK, self.OnLabelLeftDClick)
        self.Bind(gridlib.EVT_GRID_LABEL_RIGHT_DCLICK, self.OnLabelRightDClick)

        self.Bind(gridlib.EVT_GRID_ROW_SIZE, self.OnRowSize)
        self.Bind(gridlib.EVT_GRID_COL_SIZE, self.OnColSize)

        self.Bind(gridlib.EVT_GRID_RANGE_SELECT, self.OnRangeSelect)
        self.Bind(gridlib.EVT_GRID_CELL_CHANGE, self.OnCellChange)
        self.Bind(gridlib.EVT_GRID_SELECT_CELL, self.OnSelectCell)

        self.Bind(gridlib.EVT_GRID_EDITOR_SHOWN, self.OnEditorShown)
        self.Bind(gridlib.EVT_GRID_EDITOR_HIDDEN, self.OnEditorHidden)
        self.Bind(gridlib.EVT_GRID_EDITOR_CREATED, self.OnEditorCreated)

        evt.Skip()

    def OnRowSize(self, evt):
        print "OnRowSize: row %d, %s\n" % (evt.GetRowOrCol(),
                                           evt.GetPosition())
        evt.Skip()

    def OnColSize(self, evt):
        print "OnColSize: col %d, %s\n" % (evt.GetRowOrCol(),
                                           evt.GetPosition())
        evt.Skip()
########################################################################
class MyForm(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="A Simple Grid")
        panel = wx.Panel(self)

        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(12, 8)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        myGrid.SetCellValue()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
