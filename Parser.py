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
    sText = sText.replace(u'Á', 'A')
    sText = sText.replace(u'À', 'A')
    sText = sText.replace(u'á', 'a')
    sText = sText.replace(u'à', 'a')
    sText = sText.replace(u'Ã', 'A')
    sText = sText.replace(u'ã', 'a')
    sText = sText.replace(u'Â', 'A')
    sText = sText.replace(u'â', 'a')
    sText = sText.replace(u'Ä', 'A')
    sText = sText.replace(u'ä', 'a')
    sText = sText.replace(u'É', 'E')
    sText = sText.replace(u'È', 'E')
    sText = sText.replace(u'é', 'e')
    sText = sText.replace(u'è', 'e')
    sText = sText.replace(u'Ê', 'E')
    sText = sText.replace(u'ê', 'e')
    sText = sText.replace(u'Ë', 'E')
    sText = sText.replace(u'ë', 'e')
    sText = sText.replace(u'Í', 'I')
    sText = sText.replace(u'Ì', 'I')
    sText = sText.replace(u'í', 'i')
    sText = sText.replace(u'ì', 'i')
    sText = sText.replace(u'Ï', 'I')
    sText = sText.replace(u'ï', 'i')
    sText = sText.replace(u'Ú', 'U')
    sText = sText.replace(u'Ù', 'U')
    sText = sText.replace(u'ú', 'u')
    sText = sText.replace(u'ù', 'u')
    sText = sText.replace(u'Ü', 'U')
    sText = sText.replace(u'ü', 'u')
    sText = sText.replace(u'ú', 'u')
    sText = sText.replace(u'ù', 'u')
    sText = sText.replace(u'Ó', 'O')
    sText = sText.replace(u'Ò', 'O')
    sText = sText.replace(u'ó', 'o')
    sText = sText.replace(u'ò', 'o')
    sText = sText.replace(u'Õ', 'O')
    sText = sText.replace(u'õ', 'o')
    sText = sText.replace(u'Ö', 'O')
    sText = sText.replace(u'ö', 'o')
    sText = sText.replace(u'Ç', 'C')
    sText = sText.replace(u'ç', 'c')
    sText = sText.replace(u'Ñ', 'N')
    sText = sText.replace(u'ñ', 'n')
    sText = sText.replace(u'Ý', 'Y')
    sText = sText.replace(u'ý', 'y')
    sText = sText.replace(u'?', '')
    sText = sText.replace(u'!', '')
    sText = sText.replace(u'/', '+')
    sText = sText.replace(u'\\', '')
    sText = sText.replace(u'ª', '.a')
    sText = sText.replace(u'°', '.o')
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
