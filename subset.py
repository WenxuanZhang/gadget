iport sys

print "useage:python subset.py <file> <line number> <outputfilename>"

f=open(sys.argv[1],"r")

print "file has been open"
output=open(sys.argv[3],'a')
i=0
for line in f:
    output.write(line)
    i=i+1;
    if (i>sys.argv[2]):
        output.close()
        break;

print "file has been save in current directory "


