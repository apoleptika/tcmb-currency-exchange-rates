# module for command line and arguments
import sys
# module for command line arguments parser
import getopt 
from datetime import datetime

argv=sys.argv
currentdate = datetime.today().strftime('%d.%m.%Y')
arg_firstdate = ""
firstdate=""
arg_lastdate = ""
lastdate=""
arg_help = "{0} -f <firstdate> -l <lastdate> ".format(argv[0])
    
try:
    opts, args = getopt.getopt(argv[1:], "h:f:l:", ["help", "firstdate=", "lastdate="])
except:
    print(arg_help)
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-h", "--help"):
        # print the help message
        print(arg_help)  
        sys.exit(2)
    elif opt in ("-f", "--firstdate"):
        arg_firstdate = arg
        # convert string to date
        firstdate = datetime.strptime(arg_firstdate, '%d.%m.%Y')
        # convert date to specific format
        firstdate = firstdate.strftime('%d.%m.%Y')
    elif opt in ("-l", "--lastdate"):
        arg_lastdate = arg
        lastdate = datetime.strptime(arg_lastdate, '%d.%m.%Y')
        lastdate = lastdate.strftime('%d.%m.%Y')
    
if not firstdate:
    firstdate = datetime.strptime(currentdate, '%d.%m.%Y')
    firstdate = firstdate.strftime('%d.%m.%Y')

