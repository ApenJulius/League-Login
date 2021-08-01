import os, signal
import time, psutil
import pyautogui




def checkIfProcessRunning(processName): 
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def login(user, passw):
    kill()
    for x in range(4):
        print("opening client")
        os.startfile("C:\Riot Games\League of Legends\LeagueClient.exe")
        for x in range(10):
        
            if checkIfProcessRunning('RiotClientUxRender.exe'): #checks for login client
                print('Login running') 
                time.sleep(1) # with this it should work with input
                pyautogui.write(user) #enters username/password
                pyautogui.press('tab')
                pyautogui.write(passw)
                pyautogui.press('enter')
                return print("logged in") #just returns to show in command line and to break out of both loops

            else:
                print('Login not running') #just to show its attempring to find process 

def findProcessIdByName(processName):

    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects

def kill():
    listOfProcessIds = findProcessIdByName('LeagueClient.exe')
    if len(listOfProcessIds) > 0:
        print('Process Exists | PID and other details are')
    for elem in listOfProcessIds:
        processID = elem['pid']
        processName = elem['name']
        processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
        print((processID ,processName,processCreationTime ))
        os.kill(processID, signal.SIGBREAK)
    else :
        print('Client not open')




#login(user, passw) #to run the damn thing


