# -*- coding: utf-8 -*-
#    MTUOC_task
#    Copyright (C) 2019  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import codecs
import os
from datetime import datetime

entrada=codecs.open("proces.txt","r",encoding="utf-8")
logfile=codecs.open("taskscheduler.log","a",encoding="utf-8")
alreadydone={}
new=True
while new:
    new=False
    for linia in entrada:
        linia=linia.strip()
        
        if not linia in alreadydone:
            new=True
            print(linia)
            alreadydone[linia]=1
            info="START\t"+str(datetime.now())+"\t"+linia
            os.system(linia)
            info="END\t"+str(datetime.now())+"\t"+linia
            logfile.write(linia+"\n")
    entrada.close()
    entrada=codecs.open("proces.txt","r",encoding="utf-8")

print("ALL PROCESSES DONE")
#to shutdown the computer after finishing all process. Comment if you want to avoid shutdown
#os.system(systemctl poweroff -i)
