import os
import sys


    
def SearchToFile(search_dir):
    for(path,dirs,files) in os.walk(search_dir):
        for filename in files:
            if filename.endswith(".msg"):
                #print(os.path.join(path,filename))
                os.system(str(os.getcwd())+"\\outlookmsgfile.py"+" \""+os.path.join(path,filename)+"\"")
    
    
if os.path.isdir(sys.argv[1]):
    search_dir = sys.argv[1]
    SearchToFile(search_dir)