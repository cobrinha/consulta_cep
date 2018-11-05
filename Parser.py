#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import re
import htmlentitydefs

class Parser:
  def __init__(self):
    pass

  def getBetween(self, sText, sIni, sEnd):
    sText  = re.compile(sIni+'(.*?)'+sEnd, re.DOTALL |  re.IGNORECASE).findall(sText)
    return sText

  def replaceAcentos(self, sText):
    sText = sText.replace(u'�', 'A')
    sText = sText.replace(u'�', 'A')
    sText = sText.replace(u'�', 'a')
    sText = sText.replace(u'�', 'a')
    sText = sText.replace(u'�', 'A')
    sText = sText.replace(u'�', 'a')
    sText = sText.replace(u'�', 'A')
    sText = sText.replace(u'�', 'a')
    sText = sText.replace(u'�', 'A')
    sText = sText.replace(u'�', 'a')
    sText = sText.replace(u'�', 'E')
    sText = sText.replace(u'�', 'E')
    sText = sText.replace(u'�', 'e')
    sText = sText.replace(u'�', 'e')
    sText = sText.replace(u'�', 'E')
    sText = sText.replace(u'�', 'e')
    sText = sText.replace(u'�', 'E')
    sText = sText.replace(u'�', 'e')
    sText = sText.replace(u'�', 'I')
    sText = sText.replace(u'�', 'I')
    sText = sText.replace(u'�', 'i')
    sText = sText.replace(u'�', 'i')
    sText = sText.replace(u'�', 'I')
    sText = sText.replace(u'�', 'i')
    sText = sText.replace(u'�', 'U')
    sText = sText.replace(u'�', 'U')
    sText = sText.replace(u'�', 'u')
    sText = sText.replace(u'�', 'u')
    sText = sText.replace(u'�', 'U')
    sText = sText.replace(u'�', 'u')
    sText = sText.replace(u'�', 'u')
    sText = sText.replace(u'�', 'u')
    sText = sText.replace(u'�', 'O')
    sText = sText.replace(u'�', 'O')
    sText = sText.replace(u'�', 'o')
    sText = sText.replace(u'�', 'o')
    sText = sText.replace(u'�', 'O')
    sText = sText.replace(u'�', 'o')
    sText = sText.replace(u'�', 'O')
    sText = sText.replace(u'�', 'o')
    sText = sText.replace(u'�', 'C')
    sText = sText.replace(u'�', 'c')
    sText = sText.replace(u'�', 'N')
    sText = sText.replace(u'�', 'n')
    sText = sText.replace(u'�', 'Y')
    sText = sText.replace(u'�', 'y')
    sText = sText.replace(u'?', '')
    sText = sText.replace(u'!', '')
    sText = sText.replace(u'/', '+')
    sText = sText.replace(u'\\', '')
    sText = sText.replace(u'�', '.a')
    sText = sText.replace(u'�', '.o')
    sText = sText.lower().replace(u'&eacute;', 'e')
    return sText
  	
  def stripHtml(self, sText):
    s = re.sub( '<[^>]*>', '', sText)
    return s

  def unescape(self, text):
      def fixup(m):
          text = m.group(0)
          if text[:2] == "&#":
              # character reference
              try:
                  if text[:3] == "&#x":
                      return unichr(int(text[3:-1], 16))
                  else:
                      return unichr(int(text[2:-1]))
              except ValueError:
                  pass
          else:
              # named entity
              try:
                  text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
              except KeyError:
                  pass
          return text # leave as is
      return re.sub("&#?\w+;", fixup, text)
