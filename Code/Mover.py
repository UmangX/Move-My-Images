#Personal Project By Umangx.cf


from os import listdir 
from os import chdir
from os import system
from getpass import getuser


#gets the username for windows
user = getuser()


#the download directory 
Download = ('C:/Users/'+user+'/Downloads/')

#changes the pwd to directory 
chdir(Download)


#the main directory to move to //user-specific
des = ('d:/os') 

#gets the list of files
files = listdir()


def movejpg(i):
	if i[-3:len(i)] == "jpg":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + des)




def mainloop():
    for i in files:movejpg(i)


#exexute the main Search and Move Loops 
mainloop()
