import boto3
import requests
import json
import pathlib

print("Welcome to myDropbox Application")
print("============================================================")
print("      Please input command (put , get , view , quit)")
print("")
print("      If u want to upload file type 'put [filename]'")
print("     If u want to download file type 'get [filename]'")
print("  If you want to view files u have uploaded just type 'view'")
print("     If you want to quit the program just type 'quit'")
print("============================================================")

while(True):
    link = "https://d3oi3fkp7l.execute-api.ap-northeast-1.amazonaws.com/default/myDropbox"
    command = input().split()
    if(command[0] == "quit"):
        print("Bye!!")
        break
    elif(command[0] == "view"):
        if(len(command) != 1):
            print("Please enter valid command")
        else:
            response = requests.post(link,params={"command":command[0]})
            results = json.loads(response.text)
            for item in results:
                name = item['key']
                size = item['size']
                last_modified = item['last_modified']
                print("File name:" + name +" size:" + size + " last modified:" + last_modified)
    
    
    elif(command[0] == "get"):
        if(len(command)>2):
            print("U cant get many files in the same times")
        elif(len(command)==1):
            print("Please enter filename")
        else:
            response = requests.post(link,params={"command":command[0] , "Key":command[1]})
            print(response.text)


    elif(command[0] == "put"):
        if(len(command)>2):
            print("U cant put many files in the same times")
        elif(len(command) == 1):
            print("Please enter filename")
        else:
            directory =  str(pathlib.Path("mydropbox.py").parent.absolute()) 
            #print(directory)
            #print(directory+"\\"+command[1])
            try:
                file = open(directory+'\\'+command[1],"rb").read()
                #print(file)
                response = requests.post(link,params={"command":command[0],"Key":command[1], "Body":file})
                print(response.text)
            except:
                print("cant find this file")
            #file.close()
    else:
        print("Please enter valid cammand!!!!!!")
