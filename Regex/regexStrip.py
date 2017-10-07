import re
import sys

def regexStrip(*arg) :

	new = arg[0]
	if(len(arg) == 2) :
		new = (re.compile(r'^(' + arg[1] + '){1,}')).sub('',new)
		new = (re.compile(r'(' + arg[1] + '){1,}$')).sub('',new)
		return new
	else :
		new = (re.compile(r'^( ){1,}')).sub('',new)
		new = (re.compile(r'( ){1,}$')).sub('',new)
		return new

#ans = "00000hey buddy this is strip00000"
#ans = "  hey buddy this is strip  "
#print("original  :", ans)
#ans = regexStrip(ans)
#print(ans.strip())
#ans = regexStrip(ans,'0')
#print(ans.strip('0'))
#print("stripped :",ans)