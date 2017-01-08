#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
sys.path.insert(0,"/home/rong/Software/translate-2.0.0")
from translate import Translator

import codecs
import csv

'''
translator= Translator(to_lang="zh")
translation = translator.translate("This is a pen.")
print (translation)'''

output = []
translator= Translator(to_lang="zh")

f = codecs.open( 'Level3.csv', 'r+w', 'utf-8' ) #open the file in read universal mode
f2 = open('Level3_out.csv', 'wb')

spamwriter = csv.writer(f2, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

for line in f:
    cells = line.split( "," )
    output.append( ( cells[0].strip() ) ) #since we want the first, second and third column
    translation = translator.translate(cells[0])
    print (translation)
    spamwriter.writerow([cells[0].strip()]+[(""+translation).encode('utf-8')])

f.close()
f2.close()


