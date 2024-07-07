import zibfile
import time 

folderpath = input('Path to the file: ')
zibf = zibfile.Zibfile(folderpath)
global result
result = 0 
global tried 
tried = 0 
c = 0
if not zibf:
    print('The zipped file/folder is not password protected! You can successfully open it')
if(result == 0):
    print("Sorry, password not found. A total of"+str(c)"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 charecters.")
else:
    duration  = endtime - startime
    print('Congratulations!!! Password found after trying '+str(c)+' combinations in'+str(duration)+' seconds')
    