# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:11:11 2015

@author: merongoitom
"""
import urllib

def read_text():    #funktion
    quotes = open("/Users/merongoitom/Desktop/Nanodegree/IntroToPython/Check_Prophanity/check_prophanity.txt")
            #Öppna filen i dokumentet
    read_file = quotes.read()   #hämta texten i dokumentet
    print read_file             #Printa ut texten i dokumentet
    quotes.close()              #stäng sedan den öppnaden filen i dokumentet
    
    check_profanity(read_file)  #starta funktionen nedan
    
def check_profanity(input_text):    #en fuktion med variabeln 'input_text'
    connection = urllib.urlopen('http://www.wdyl.com/profanity?q='+input_text)
                                    #öppna URL, och addera texten vi importera tidigare
    output = connection.read()      #Läs igenom outputet av länen ovan
    print output                    #printa outputet
    connection.close()              #stäng URL:en du öppnade!
    
    if 'true' in output:
        print "ALERT PROPHANITY DETECTED"
    elif 'false' in output: 
        print "NO Prophanity detected"
    else:
        "Issue scanning the document"


read_text()