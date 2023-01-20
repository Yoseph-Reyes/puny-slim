from os import system
import os


def test(param):
    pb = open("GPruebas/Tests/"+param['name']+".robot","w+",encoding="utf-8")
    count = int(param['contador']) +1
    pb.write("*** Settings ***\n")
    pb.write("Documentation  "+param['title']+" \n")
    pb.write("Library  SeleniumLibrary\n")

    pb.write("*** Variables ***\n")

    pb.write("${url}=      "+param['url']+" \n")
            
    pb.write("*** Test Cases ***\n")

    pb.write(param['doc']+"\n")
    pb.write("    [documentation]  "+param['doc']+"\n")
    pb.write("    Open Browser  ${url}  Chrome\n")
    pb.write("    Wait Until Element Is Visible  id:"+param["id0"]+"  timeout=5\n")
    pb.write("    Set Focus To Element  id:"+param["id0"]+"\n")
    
    for i in range(count):
        if param["accion"+str(i)] == "Click Element":
            pb.write("    "+param["accion"+str(i)]+"  id:"+param["id"+str(i)]+"\n")
        else:
            pb.write("    "+param["accion"+str(i)]+"  id:"+param["id"+str(i)]+"  "+param["var"+str(i)]+"\n")
        
    #pb.write("    "+param+"  id:${ID1text}  tomsmith\n")
    
    #pb.write("    Click Element  css:button[type='submit']\n")
    pb.write("    "+param["accionres"]+"  "+param['varres']+"  timeout=5\n")
    pb.write("    Close Browser\n")

    pb.write("*** Keywords ***\n")

    ############PARAMETROS DE LA PRUEBA PARA ALMACENAR EN EL HISTORIAL########################################

    parametros = open("GPruebas/Parametros/"+param['name']+".txt","w+",encoding="utf-8")
    count = int(param['contador']) + 1
    parametros.write(str(count)+"\n")
    parametros.write(param['url']+"\n")
    parametros.write(param['name']+"\n")
    parametros.write(param['title']+"\n")
    parametros.write(param['doc']+"\n")

    for i in range(count):
        if param["accion"+str(i)] == "Click Element":
            parametros.write(param['obj'+str(i)]+"\n"+param["accion"+str(i)]+"\n"+param["id"+str(i)]+"\n"+" \n")
        else:
            parametros.write(param['obj'+str(i)]+"\n"+param["accion"+str(i)]+"\n"+param["id"+str(i)]+"\n"+param["var"+str(i)]+"\n")
        
    parametros.write(" \n"+param["accionres"]+"\n"+param['varres'])

    return ("GPruebas/Tests/"+param['name']+".robot")

def pre(param):
    resp = test(param)
    print (resp)
    system("robot -d GPruebas/Results "+resp)
    path = os.getcwd()

    #system("start chrome "+path+"/GPruebas/Results/report.html")
    system("start chrome "+path+"/GPruebas/Results/log.html")
    return ("Exito")

