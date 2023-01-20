import os

#pb = open("GPruebas/Tests/autempb.robot","w+",encoding="utf-8")

if True:
    #open text file in read mode
    text_file = open("Tests/autempb.robot", "r",encoding="utf-8")
    
    #read whole file to a string
    data = text_file.read()
    
    #close file
    text_file.close()

    
 
    print(data)