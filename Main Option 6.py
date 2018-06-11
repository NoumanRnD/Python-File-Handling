import os
import csv
import string
import sys
import imp
 



 

def Main():
  
  ans=True
  while ans:
    print ("""
    1.Option 1 reading files
    2.Option 2 merging files
    3.Option 3 Sin wave
    4.Option 4 temprature graph
    5.Option 5 CSV Merging
    6.Option 6 Exit/Quit
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1":
       
       main = imp.load_source('Option1', 'Option1/Program.py')
       print("\n Method called sucessfully") 
    elif ans=="2":
      main = imp.load_source('Option2', 'Option2/Program.py')
      print("\n Method called sucessfully") 
    elif ans=="3":
      main = imp.load_source('Option3', 'Option3/Program.py')
      print("\n Method called sucessfully")
    elif ans=="4":
      main = imp.load_source('Option4', 'Option4/Program.py')
      main.Main()
      print("\n Method called sucessfully")
    elif ans=="5":
      main = imp.load_source('Option5', 'Option5/Program.py')
      print("\n Method called sucessfully") 
    elif ans=="6":
      print("\n Goodbye") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 


Main()	

 
