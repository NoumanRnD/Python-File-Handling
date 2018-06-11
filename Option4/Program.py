import os
import csv
import string
import sys
import matplotlib.pyplot as plt
import numpy as np

 
actual_temp = ""
actualt=[""] 
temperature2=[""]
temperature=[""]
 
a = [""]
array = {}
script_dir = os.path.dirname(__file__)
actual_temp = 'Data/input_temperature1.txt'
actual_temp2 = "Data/input_temperature2.txt"   
 
 
actual_temp = os.path.join(script_dir, actual_temp)
actual_temp2 = os.path.join(script_dir, actual_temp2)

 

def Main():
    
   with open(actual_temp) as f:
     temperature = f.read().splitlines()
   with open(actual_temp2) as f2:
     temperature2 = f2.read().splitlines()
  


   
   
   xf = [float(i) for i in temperature]
   print (xf)
   yf = [float(i) for i in temperature2]
   y = [int(i) for i in yf]
   x = [int(i) for i in xf]
   avg= (reduce(lambda x,y:x+y,x)/len(x))
   
   plt.bar(x,y,align='center') # A bar chart
   plt.xlabel('ticks')
   plt.ylabel('labels')
   plt.title('temperature comparison plot')
   for i in range(len(y)):
      plt.hlines(y[i],0,x[i]) # Here you are drawing the horizontal lines
   plt.plot(x, y, 'r-')
 
  
   
   plt.axvline(avg, color='green', linewidth=2)
   plt.savefig("output/firstname_temp_plot.png")
   plt.show()
  
    
    
   
    

   
Main()	

 
