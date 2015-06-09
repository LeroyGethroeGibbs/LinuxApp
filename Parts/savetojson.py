__author__ = 'karinamarie'
from kivy.storage.jsonstore import JsonStore
from kivy.event import EventDispatcher
import json
import csv
import wx
import wx.grid as gridlib

storej = JsonStore('projectlist.json')

p = []
for key in storej.keys():
    p.append(key)
print p
# Write CSV Header
# f.writerow(["pk", "model", "codename", "name", "content_type"])

# Make csv function
def make_csv(project):
    # define & clear lists for each project number
    list = []
    profilelist = []
    contentlist = []

    print project + ' project'

    file = ('%s.csv' % (project))
    f = csv.writer(open(file, "wb+"))

    for key in storej.get((project)):
        list.append(key)
    print list  # [profile, content]
    for key in storej[project]['profile']:
        print key
        profilelist.append(key)
    print profilelist  # [projectid, created_at, creator, timeinproject]

    for key in storej[project]['content']['designrequirements']:
        print key
        contentlist.append(key)
    print contentlist

    print '\n\n'
    f.writerow([project])
    f.writerow([list[0]])
    f.writerow([profilelist[0], storej[project]['profile']['%s' % (profilelist[0])]])
    f.writerow([profilelist[1], storej[project]['profile']['%s' % (profilelist[1])]])
    f.writerow([profilelist[2], storej[project]['profile']['%s' % (profilelist[2])]])
    f.writerow([profilelist[3], storej[project]['profile']['%s' % (profilelist[3])]])
    f.writerow([profilelist[4], storej[project]['profile']['%s' % (profilelist[4])]])
    ## ##


    ## ##

    f.writerow([None])
    f.writerow([list[1]])
    f.writerow(['Design Requirments'])
    f.writerow([None, 'Design Requirments',
                'Design Requirment Rationale',
                'Design Requirment\n Importance Score',
                'Design Requirement\n Importance Score Rationale'])
    i = 0
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drisr'],
                ])
    i = 1
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drisr'],
                ])
    i = 2
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drisr'],
                ])
    i = 3
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drisr'],
                ])
    i = 4
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drisr'],
                ])
    i = 5
    f.writerow([contentlist[i],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drr'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['dris'],
                storej[project]['content']['designrequirements']['%s' % (contentlist[i])]['drisr'],
                ])
    #             x[1],
    #            x["content"]]
    #            )

    #             x["model"],
    #             x["fields"]["codename"],
    #             x["fields"]["name"],
    #             x["fields"]["content_type"]])
    return list, profilelist, contentlist

import wx
import wx.grid as gridlib

class Frame(wx.Frame):
    # ----------------------------------------------------------------------
    def __init__(self, **kwargs):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="A Simple Grid", size=(1000,600))

        sizer_main = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel( self )
        sizer_inner = wx.BoxSizer( wx.VERTICAL)
        self.grid = wx.grid.Grid( self.panel, wx.ID_ANY)

        # Grid
        self.grid.CreateGrid( 6, 4 )
        self.grid.EnableEditing( True)

        self.grid.SetDefaultRenderer(wx.grid.GridCellAutoWrapStringRenderer())

        self.grid.SetCellValue(0,0,'Render propulsion system exhaust resistant to cracking')
        self.grid.SetCellValue(1,0, 'Do not introduce new impacts on operating environment as result of design modification')
        self.grid.SetCellValue(2,0, 'Render propulsion system exhaust fully and reliably functional for sufficient time to complete research voyages')
        self.grid.SetCellValue(3,0, 'Ensure that propulsion system exhaust fix does not inhibit function or maintenance of other genset components')
        self.grid.SetCellValue(4,0, 'Do not introduce new impacts on access control as result of design modification')
        self.grid.SetCellValue(5,0, 'Ensure that propulsion system exhaust does not induce additional backpressure on genset operation')

        self.grid.SetCellValue(0,1,'Current cracking and leakage of exhaust system results in shutdown of shipboard propulsion system due to room habitability alarms')
        self.grid.SetCellValue(1,1,'Equipment is designed to function correctly in existing operating environment.')
        self.grid.SetCellValue(2,1,'Room habitability issues violate NAVSEA and ABS crew habitability standards for onboard ship safety, OSHA standards for confined spaces')
        self.grid.SetCellValue(3,1,'Minor or major alterations to the exhaust system can result in impeded access to critical equipment, if not factored into DS.')
        self.grid.SetCellValue(4,1,'Equipment is designed for adequate access control currently.')
        self.grid.SetCellValue(5,1,'Minor or major alterations to the exhaust system can result in impeded funtion of genset, if not factored into DS.')

        self.grid.SetCellValue(0,2,'4')
        self.grid.SetCellValue(1,2,'2')
        self.grid.SetCellValue(2,2,'4')
        self.grid.SetCellValue(3,2,'4')
        self.grid.SetCellValue(4,2,'2')
        self.grid.SetCellValue(5,2,'3')

        self.grid.SetCellValue(0,3,'')
        self.grid.SetCellValue(1,3,'')
        self.grid.SetCellValue(2,3,'')
        self.grid.SetCellValue(3,3,'')
        self.grid.SetCellValue(4,3,'')
        self.grid.SetCellValue(5,3,'')


        self.grid.SetColLabelValue(0,'Design \nRequirement')
        self.grid.SetColLabelValue(1,'DRR')
        self.grid.SetColLabelValue(2,'DRIS')
        self.grid.SetColLabelValue(3,'DRISR')

        self.grid.SetRowLabelValue(0, 'Functionality')
        self.grid.SetRowLabelValue(1, 'Operational \nEnvironment')
        self.grid.SetRowLabelValue(2, 'Health, Safety, \nand Environment')
        self.grid.SetRowLabelValue(3, 'Manageability')
        self.grid.SetRowLabelValue(4, 'Security')
        self.grid.SetRowLabelValue(5, 'Interfacing \nSystems')



        self.grid.EnableGridLines( True )
        self.grid.SetGridLineColour([1,1,1,1])
        self.grid.SetMargins(0,0)
        print self.grid.GetDefaultColLabelSize()
        ##self.grid.SetColLabelSize()

        # Columns
        self.grid.EnableDragColMove( True )
        self.grid.EnableDragColSize( True )
        self.grid.SetColLabelSize( 80 )
        ##

        print self.grid.GetColLabelSize()
        self.grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Rows
        self.grid.EnableDragRowSize( True )
        self.grid.SetRowLabelSize(120 )
        self.grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        self.grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )

        sizer_inner.Add( self.grid, 1, wx.ALL, 5)


        self.panel.SetSizer( sizer_inner)
        self.panel.Layout()
        sizer_inner.Fit( self.panel)
        sizer_main.Add( self.panel, 1, wx.EXPAND|wx.ALL, 2 )

        self.SetSizer( sizer_main )
        self.Layout()
        self.Centre( wx.BOTH )
        self.Show()
        print self.GetSize()
        # Connect Events
        self.grid.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_edit )

        # Some essential stuff for resizing
        font = wx.Font(pointSize = 9, family = wx.DEFAULT, style = wx.NORMAL, weight = wx.NORMAL, faceName = 'Consolas')
        self.dc = wx.ScreenDC()
        row=6
        col=4
         ##
        attr = self.grid.GetOrCreateCellAttr(0,0) ##
        self.dc.SetFont(attr.GetFont())

    def on_edit( self, event):
        row = event.GetRow()

        col= event.GetCol()
        print col
        print '\n\n'
        size = self.dc.GetTextExtent(self.grid.GetCellValue(row, col))

        text = self.grid.GetCellValue(row, col)
        text2 = wordwrap.wordwrap(text, self.grid.GetRowSize(row), self.dc, breakLongWords = False)
        w, h, lineHeight = max(self.dc.GetMultiLineTextExtent(text2), [80,20,10])
        print w
        print h
        print lineHeight
        print size
        print self.grid.GetRowLabelSize()
        print 'centebury'
        coll=[]
        roww=[]
        for i in range(0,5):
            coll.append(self.grid.GetColSize(i))

            print coll
            print '\n'
        print max(coll)
        for i in range(0,7):
            roww.append(self.grid.GetRowSize(i))
            print roww
        print max(roww)


        #if size[0]  > self.grid.GetColSize(col):
        w = max(size[0], self.grid.GetColSize(col), self.grid.GetColLabelSize())
        self.grid.SetColSize(col, w)
        w = min(size[0], self.grid.GetColSize(col), self.grid.GetColLabelSize())
        self.grid.SetColLabelSize(w)

        #if size[1] < self.grid.GetRowSize(col):
        h = max(h, self.grid.GetRowSize(row))
        self.grid.SetRowSize(row, h)
        h = min(h, self.grid.GetRowSize(row))
        self.grid.SetRowLabelSize(h)

        self.panel.Layout()

        p_title = storej[project]['profile']['%s' % (profilelist[4])]

        ###myGrid.SetCellValue(0, 0, p_title)
    #wx.grid.EVT_GRID_CELL_CHANGE(3, 'Banana Face')

from wx.lib import wordwrap
import wx.grid

if __name__ == "__main__":
    # for project in p:
    project = '123'
    list, profilelist, contentlist = make_csv(project)

    app = wx.App(False)
    ##app = wx.PySimpleApp()
    Frame()
    app.MainLoop()

