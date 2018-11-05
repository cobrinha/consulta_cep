#!/usr/bin/python
#-*- coding: utf-8 -*-

import wx
import wx.grid

def create(parent, app):
    return Frame1(parent, app)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1COMBOBOX1, 
 wxID_FRAME1COMBOBOX2, wxID_FRAME1PANEL1, wxID_FRAME1STATICLINE1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, 
] = [wx.NewId() for _init_ctrls in range(16)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt, app):
         # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(557, 273), size=wx.Size(451, 383),
              style=wx.STAY_ON_TOP|wx.DEFAULT_FRAME_STYLE|wx.MINIMIZE_BOX,
              title='CompuCEP 0.1v')
        self.SetClientSize(wx.Size(443, 356))

        self.app = app

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(443, 356),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='CEP:', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 42), size=wx.Size(44, 16), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(64, 40), size=wx.Size(100, 21),
              style=0, value='')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='Procurar',
              name='button1', parent=self.panel1, pos=wx.Point(192, 38),
              size=wx.Size(120, 23), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(0, 200), size=wx.Size(440, 152),
              style=wx.TE_MULTILINE, value='')

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(8, 80),
              size=wx.Size(416, 2), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='RUA:', name='staticText2', parent=self.panel1,
              pos=wx.Point(16, 123), size=wx.Size(25, 13), style=0)

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(64, 120), size=wx.Size(218, 21),
              style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Busca por CEP:', name='staticText3', parent=self.panel1,
              pos=wx.Point(16, 16), size=wx.Size(73, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='Busca por endere\xe7o:', name='staticText4',
              parent=self.panel1, pos=wx.Point(16, 96), size=wx.Size(99, 13),
              style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5, label='UF:',
              name='staticText5', parent=self.panel1, pos=wx.Point(304, 123),
              size=wx.Size(17, 13), style=0)

        self.comboBox1 = wx.ComboBox(choices=['Acre','Alagoas','Amazonas','Amap\xe1','Bahia','Cear\xe1','Distrito Federal','Esp\xedrito Santo','Goi\xe1s','Maranh\xe3o','Minas Gerais','Mato Grosso do Sul','Mato Grosso','Par\xe1','Para\xedba','Pernambuco','Piau\xed','Paran\xe1',
        'Rio de Janeiro','Rio Grande do Norte','Rond\xf4nia','Roraima','Rio Grande do Sul','Santa Catarina','Sergipe','S\xe3o Paulo','Tocantins'], id=wxID_FRAME1COMBOBOX1,
              name='comboBox1', parent=self.panel1, pos=wx.Point(338, 120),
              size=wx.Size(100, 21), style=0, value='')
        self.comboBox1.SetLabel('')
        self.comboBox1.Bind(wx.EVT_COMBOBOX, self.EvtComboBox1)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label='CIDADE:', name='staticText6', parent=self.panel1,
              pos=wx.Point(16, 160), size=wx.Size(42, 13), style=0)

        self.comboBox2 = wx.ComboBox(choices=[], id=wxID_FRAME1COMBOBOX2,
              name='comboBox2', parent=self.panel1, pos=wx.Point(64, 152),
              size=wx.Size(220, 21), style=0, value='')
        self.comboBox2.SetLabel('')

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='Procurar',
              name='button2', parent=self.panel1, pos=wx.Point(318, 152),
              size=wx.Size(120, 23), style=0)

    def EvtComboBox1(self, event):
        self.sUf = ""
        if event.GetString() == u'Acre':
          self.sUf = 'AC'
        elif event.GetString() == u'Alagoas':
          self.sUf = 'AL'
        elif event.GetString() == u'Amap\xe1':
          self.sUf = 'AP'
        elif event.GetString() == u'Amazonas':
          self.sUf = 'AM'
        elif event.GetString() == u'Bahia':
          self.sUf = 'BA'
        elif event.GetString() == u'Cear\xe1':
          self.sUf = 'CE'
        elif event.GetString() == u'Distrito Federal':
          self.sUf = 'DF'
        elif event.GetString() == u'Esp\xedrito Santo':
          self.sUf = 'ES'
        elif event.GetString() == u'Goi\xe1s':
          self.sUf = 'GO'
        elif event.GetString() == u'Maranh\xe3o':
          self.sUf = 'MA'
        elif event.GetString() == u'Minas Gerais':
          self.sUf = 'MG'
        elif event.GetString() == u'Mato Grosso do Sul':
          self.sUf = 'MS'
        elif event.GetString() == u'Mato Grosso':
          self.sUf = 'MT'
        elif event.GetString() == u'Par\xe1':
          self.sUf = 'PA'
        elif event.GetString() == u'Para\xedba':
          self.sUf = 'PB'
        elif event.GetString() == u'Pernambuco':
          self.sUf = 'PE'
        elif event.GetString() == u'Piau\xed':
          self.sUf = 'PI'
        elif event.GetString() == u'Paran\xe1':
          self.sUf = 'PR'
        elif event.GetString() == u'Rio de Janeiro':
          self.sUf = 'RJ'
        elif event.GetString() == u'Rio Grande do Norte':
          self.sUf = 'RN'
        elif event.GetString() == u'Rond\xf4nia':
          self.sUf = 'RO'
        elif event.GetString() == u'Roraima':
          self.sUf = 'RR'
        elif event.GetString() == u'Rio Grande do Sul':
          self.sUf = 'RS'
        elif event.GetString() == u'Santa Catarina':
          self.sUf = 'SC'
        elif event.GetString() == u'Sergipe':
          self.sUf = 'SE'
        elif event.GetString() == u'S\xe3o Paulo':
          self.sUf = 'SP'
        elif event.GetString() == u'Tocantins':
          self.sUf = 'TO'

        self.app.OnCidades()

    def __init__(self, parent, app):
        self._init_ctrls(parent, app)
