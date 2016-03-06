#!/usr/bin/python

import sys
from lxml import html
import requests

arguments = sys.argv

word = ""

if len(arguments) == 1:
    exit("usage: dud WORD")
elif len(arguments) == 2:
    word = arguments[1]

page = requests.get("http://www.duden.de/rechtschreibung/"+word)
tree = html.fromstring(page.text)

meanings = tree.xpath("//*[contains(@id,'block-duden-tiles-1')]")

for meaning in meanings[0].getchildren()[1].getchildren():
    print("asd")

