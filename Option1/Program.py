import os
 
lines=[""]
Names=[""]
def Main():
   script_dir = os.path.dirname(__file__)
   rel_path = "Data\input_data.txt"
   abs_file_path = os.path.join(script_dir, rel_path)
   rel_output = "output\input_formatted_data.txt"
   rel_outputf = "output"
   rel_folder = os.path.join(script_dir, rel_outputf)
   out_file_path = os.path.join(script_dir, rel_output)
   
   Names = open(abs_file_path).readlines() 
   Names  = map(lambda s: s.strip(), Names)
   Names  = list(set(Names))
   Names = filter(None, Names)
   if not os.path.exists(rel_folder):
    os.makedirs(rel_folder)
   
   if os.path.exists(out_file_path):
      open(out_file_path, 'w').close()

   else:
     open(out_file_path, 'w')
   
   file1 = open(out_file_path , "w")
   for item in Names:
     file1.write("%s\n" % item)

   file1.close()
   stayWatch =  raw_input('check results above , [input] something to exit:')
Main()	

 
