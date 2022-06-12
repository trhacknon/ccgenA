import sys
import random
import time
import os
time.sleep(1)
print"""
+=====================+=====================+
|                                                        |
|                                CCGen v2.0              |
|                                                        |
|                        CODED BY : trhacknon            |
|       E-mail : jeremydiliotti@gmail.com         |
+=====================+=====================+
\n"""

with open('up1.txt') as f:
    for line in f:
        print line.strip()

time.sleep(1)
def cardgenerator():
    binn = raw_input("Enter Bin (Ex :521086) : ")
    mm = raw_input("Mois (MM) : ")
    yy = raw_input("Annee (YY) : ")
    i=1
    for i in range(0,100):
            i=i+1
            geneccv = random.randint(100,999)
            genenum = random.randint(1000000000,9999999999)
            creditcard = (binn,genenum)
            creditcardstr = "%s%s"%(creditcard)
            all = creditcardstr,"|",mm,"|",yy,"|",geneccv
            allstring = "%s%s%s%s%s%s%s"%(all)
            print allstring

cardgenerator()
