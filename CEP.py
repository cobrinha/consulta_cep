#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import win32com.client
import unicodedata
from Parser import Parser

import wx
import wx.grid
import Frame1

modules = {'Frame1' : [1, 'CompuCEP', 'none://Frame1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame1.create(None, self)
        try:
          self.conn = win32com.client.Dispatch("ADODB.Connection")
          lPath =  os.getcwd().split("\\")
          self.db = str("\\".join(lPath)+"\\Cep.mdb")
          self.DSN="Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + self.db
          self.conn.Open(self.DSN)
          self.cmd = win32com.client.Dispatch("ADODB.Command")
          self.cmd.ActiveConnection = self.conn
          self.rs = win32com.client.Dispatch("ADODB.Recordset")
          self.oParser = Parser()
          self.main.button1.Bind(wx.EVT_BUTTON, self.OnBuscar)
          self.main.button2.Bind(wx.EVT_BUTTON, self.OnBuscarEnd)
          self.main.statusBar = wx.StatusBar(self.main, -1)
          self.main.statusBar.SetFieldsCount(1)
          self.main.SetStatusBar(self.main.statusBar)
          self.main.statusBar.SetStatusText("Digite o CEP a ser consultado")

          self.main.Show()
          self.SetTopWindow(self.main)
          return True

        except Exception, e:
          print("Erro ao conectar com banco de dados! - "+str(e.args))
          sys.exit(2)

    def OnCidades(self):
        self.lCidades = {}
        uf = self.main.sUf
        self.main.statusBar.SetStatusText("Buscando cidades de "+uf)
        sql = "SELECT Codigo, Descricao FROM tblCidades WHERE UF = '%s'" % uf
        self.cmd.CommandText = sql
        self.rs = self.cmd.Execute
        (self.rs, result) = self.cmd.Execute()
        self.main.comboBox2.Clear()
        iCont = 0
        sRes = ''

        while not self.rs.EOF:
          self.main.comboBox2.Append(self.rs.Fields[1].Value)
          self.lCidades[self.rs.Fields[1].Value] = self.rs.Fields[0].Value
          self.rs.MoveNext()

        self.main.statusBar.SetStatusText("")
        return

    def OnBuscarEnd(self, event):
        import unicodedata
        sCidade = self.main.comboBox2.GetValue()
        sEnd    = unicodedata.normalize('NFKD', self.main.textCtrl3.GetValue()).encode('ascii','ignore')

        iCodCid = ""
        try:
          for k, v in self.lCidades.iteritems():
            if k == sCidade:
              iCodCid = v

          sql = "SELECT UF, CodigoCidade, CodigoBairro, LOG_TIPO_LOGRADOURO, DescricaoSemAcento, CEP FROM "
          sql = sql + "tblLogradouros WHERE CodigoCidade = "+str(iCodCid)+" AND DescricaoSemAcento LIKE '%"+str(sEnd)+"%'"

          self.cmd.CommandText = sql
          self.rs = self.cmd.Execute
          (self.rs, result) = self.cmd.Execute()

          iCont = 0
          sRes = ''

          while not self.rs.EOF:
            iCont = 1
            sql1 = "SELECT Descricao FROM tblBairros WHERE Codigo = "+str(self.rs.Fields[2].Value)
            self.cmd.CommandText = sql1
            rs1 = self.cmd.Execute
            (rs1, result1) = self.cmd.Execute()

            sql2 = "SELECT Descricao FROM tblCidades WHERE Codigo = "+str(self.rs.Fields[1].Value)
            self.cmd.CommandText = sql2
            rs2 = self.cmd.Execute
            (rs2, result2) = self.cmd.Execute()

            import unicodedata
            sBairro = unicodedata.normalize('NFKD',rs1.Fields[0].Value).encode('ascii','ignore')
            sCidade = unicodedata.normalize('NFKD',rs2.Fields[0].Value).encode('ascii','ignore')
            sLog    = unicodedata.normalize('NFKD',self.rs.Fields[3].Value).encode('ascii','ignore')
            sEnd    = unicodedata.normalize('NFKD',self.rs.Fields[4].Value).encode('ascii','ignore') 
            sCEP    = unicodedata.normalize('NFKD',self.rs.Fields[5].Value).encode('ascii','ignore') 
            sUF     = self.rs.Fields[0].Value

            sRes +=  '\n'
            sRes +=  '------------------------------------------------\n\n'
            sRes +=  ''+str(sLog)+" "+str(sEnd)+'\n'
            sRes +=  'Bairro: '+str(sBairro)+'\n'
            sRes +=  'Cidade: '+str(sCidade)+'\n'
            sRes +=  'Estado: '+str(sUF)+'\n'
            sRes +=  'CEP: '+str(sCEP)+'\n'
            sRes +=  '------------------------------------------------\n\n'

            self.rs.MoveNext()

          if iCont == 0:
            wx.MessageBox('CEP não encontrado!', 'CompuCEP')
            self.main.statusBar.SetStatusText("Não encontrado!")
            return False
          else:
            if iCont > 1:
              self.main.statusBar.SetStatusText("Exibindo "+str(iCont)+" resultados encontrados")
            else:
              self.main.statusBar.SetStatusText("Exibindo "+str(iCont)+" resultado encontrado")

          sRes = unicode(sRes, errors='ignore')
          self.main.textCtrl2.SetValue(sRes)


        except Exception, e:
          self.main.statusBar.SetStatusText("Erro! Verifique se os campos: UF, CIDADE E RUA foram preenchidos")
          print str(e.args)


    def OnBuscar(self, event):
        cep = self.main.textCtrl1.GetValue()
        cep = cep.replace('-', '')
        
        self.main.textCtrl2.SetValue("")

        if len(cep) != 8:
          wx.MessageBox('CEP Inválido!', 'CompuCEP')
          self.main.statusBar.SetStatusText("Digite o CEP novamente")
          return False

        sql = "SELECT UF, CodigoCidade,CodigoBairro, LOG_TIPO_LOGRADOURO,DescricaoSemAcento,CEP FROM tblLogradouros WHERE CEP = '%s'" % cep
        self.cmd.CommandText = sql
        self.rs = self.cmd.Execute
        (self.rs, result) = self.cmd.Execute()

        iCont = 0
        sRes = ''

        while not self.rs.EOF:
          iCont = iCont + 1
          sql1 = "SELECT Descricao FROM tblBairros WHERE Codigo = "+str(self.rs.Fields[2].Value)
          self.cmd.CommandText = sql1
          rs1 = self.cmd.Execute
          (rs1, result1) = self.cmd.Execute()

          sql2 = "SELECT Descricao FROM tblCidades WHERE Codigo = "+str(self.rs.Fields[1].Value)
          self.cmd.CommandText = sql2
          rs2 = self.cmd.Execute
          (rs2, result2) = self.cmd.Execute()

          import unicodedata
          sBairro = unicodedata.normalize('NFKD',rs1.Fields[0].Value).encode('ascii','ignore')
          sCidade = unicodedata.normalize('NFKD',rs2.Fields[0].Value).encode('ascii','ignore')
          sLog    = unicodedata.normalize('NFKD',self.rs.Fields[3].Value).encode('ascii','ignore')
          sEnd    = unicodedata.normalize('NFKD',self.rs.Fields[4].Value).encode('ascii','ignore') 
          sCEP    = unicodedata.normalize('NFKD',self.rs.Fields[5].Value).encode('ascii','ignore') 
          sUF     = self.rs.Fields[0].Value

          sRes +=  '\n'
          sRes +=  '------------------------------------------------\n\n'
          sRes +=  ''+str(sLog)+" "+str(sEnd)+'\n'
          sRes +=  'Bairro: '+str(sBairro)+'\n'
          sRes +=  'Cidade: '+str(sCidade)+'\n'
          sRes +=  'Estado: '+str(sUF)+'\n'
          sRes +=  'CEP: '+str(sCEP)+'\n'
          sRes +=  '------------------------------------------------\n\n'

          self.rs.MoveNext()
        
        if iCont == 0:
          wx.MessageBox('CEP não encontrado!', 'CompuCEP')
          self.main.statusBar.SetStatusText("Não encontrado!")
          return False
        else:
          if iCont > 1:
            self.main.statusBar.SetStatusText("Exibindo "+str(iCont)+" resultados encontrados")
          else:
            self.main.statusBar.SetStatusText("Exibindo "+str(iCont)+" resultado encontrado")

        sRes = unicode(sRes, errors='ignore')
        self.main.textCtrl2.SetValue(sRes)

def main():
    application = BoaApp(0)
    application.MainLoop()

main()
