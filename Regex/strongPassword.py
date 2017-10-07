import re

def retry() :
	
	print("Check another password ?")
	retry = input()
	if(not(re.compile(r'no|n',re.I)).search(retry)) :
		return True
	else :
		return False

def checkStrong(password) :

	if(not(re.compile(r'([a-z])+')).search(password)) :
		print("A strong password should contain atleast one lower case character") 
		return False
	if(not(re.compile(r'([A-Z])+')).search(password)) :
		print("A strong password should contain atleast one UPPER case character") 
		return False
	if(not(re.compile(r'([0-9])+')).search(password)) :
		print("A strong password should contain atleast one digit (0-9) character") 
		return False
	if(not(re.compile(r'(.){8,}')).search(password)) :
		print("A strong password should contain atleast 8 characters") 
		return False
	return True

while(1) :

	password = input("Enter a password : ");
	if((re.compile(r' ')).search(password)) :
		print("Password must not contain spaces !")
		if(retry()) :
			continue
		else :
			exit()
	else :
		if(checkStrong(password)) :
			print("Your Password is strong")
			retry()
		else :
			print("Your Password was weak")
			if(retry()) :
				continue
			else :
				exit()


