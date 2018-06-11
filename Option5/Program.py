import os
import csv
import string
import sys
import matplotlib.pyplot as plt
import numpy as np

 
 
actualt=[""] 
linesVoltage=[""]
temperature=[""]
finallist = [""]
a = [""]
array = {}

actual_temp = "Data/temp.csv"
input_voltage = "Data\input_voltage.csv"
set_temperature = "Data\set_temperature.csv"
combined_data = "output\combined_data.csv"
script_dir = os.path.dirname(__file__)
  
 
 
actual_temp = os.path.join(script_dir, actual_temp)
input_voltage = os.path.join(script_dir, input_voltage)

set_temperature = os.path.join(script_dir, set_temperature)
 

def graph():
   
   actualt=[""] 
   linesVoltage=[""]
   temperature=[""]
   with open(actual_temp, 'rb') as f1:
     reader = csv.reader(f1)
     actualt = list(reader)
   with open(input_voltage, 'rb') as f2:
     reader = csv.reader(f2)
     linesVoltage = list(reader)  
   with open(set_temperature, 'rb') as f3:
     reader = csv.reader(f3)
     temperature = list(reader)
  
    
   
   x1 = [item for sublist in actualt for item in sublist]
   y2 = [item for sublist in temperature for item in sublist]
   y3 = [item for sublist in linesVoltage for item in sublist]
   xf = [float(i) for i in x1]
   yf = [float(i) for i in y2]
   y3f = [float(i) for i in y3]
   y = [int(i) for i in yf]
   x = [int(i) for i in xf]
   z = [int(i) for i in y3f]
   plt.bar(x,y,align='center') # A bar chart
   plt.xlabel('ticks')
   plt.ylabel('labels')
   plt.title('temperature comparison plot')
   for i in range(len(y)):
      plt.hlines(y[i],0,x[i]) # Here you are drawing the horizontal lines

   plt.savefig("output/temp_compare.png")
   plt.show()
  
   plt.bar(x,z,align='center') # A bar chart
   plt.xlabel('ticks')
   plt.ylabel('labels')
   plt.title('voltage plot')
   for i in range(len(y)):
      plt.hlines(z[i],0,x[i]) # Here you are drawing the horizontal lines

   plt.savefig("output/voltage_plot.png.png")
   plt.show() 
   
    
def Main():
    
   i = 0
   
   strg = ""
   with open(actual_temp, 'rb') as f1:
     reader = csv.reader(f1)
     actualt = list(reader)
   with open(input_voltage, 'rb') as f2:
     reader = csv.reader(f2)
     linesVoltage = list(reader)  
   with open(set_temperature, 'rb') as f3:
     reader = csv.reader(f3)
     temperature = list(reader)
     
   finallist = map(lambda a, b , c : a + b+c , actualt, linesVoltage , temperature)
  
    
   
      
   with open(combined_data, 'wb') as f4:
     writer = csv.writer(f4)
    
     writer.writerows(finallist)
   graph() 
   
Main()	

 
