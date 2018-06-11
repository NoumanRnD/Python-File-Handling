import os
x = [""] 
lines=[""]
Names=[""]
def Main():
   script_dir = os.path.dirname(__file__)
   rel_path = "Data\input_data2.txt"
   rel_names = "Data\input_name.txt"
   rel_nameout = "output\output_merged_data.txt"
   abs_file_path1 = os.path.join(script_dir, rel_path)
   abs_file_path2 = os.path.join(script_dir, rel_names)
     
 
   Names = open(abs_file_path2).readlines() 
   Names  = map(lambda s: s.strip(), Names)
    
   Names = filter(None, Names)
   lines = open(abs_file_path1).readlines() 
   lines  = map(lambda s: s.strip(), lines)
    
   lines = filter(None, lines)
   for i, val in enumerate(Names):
     j= len(lines)
     if (i < j):
          linesstring = lines[i]
          x2 = linesstring
          k = x2.split(',')
          j = [k[0]] + [','+l for l in k[1:]]
          if(val.find(j[0])!=-1):
           
            val = val.replace(j[0], linesstring)
            x.append(val)
          else:
            x.append(val)
            x.append(linesstring)
     else:
         x.append(val) 
   if os.path.exists(rel_nameout):
      open(rel_nameout, 'w').close()

   else:
     open(rel_nameout, 'w')
   
   file1 = open(rel_nameout , "w")
   for item in x:
     file1.write("%s\n" % item)

   file1.close()
   print (x)
   stayWatch =  raw_input('check results above , [input] something to exit:')
Main()	

 
