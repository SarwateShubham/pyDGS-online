import csv
import os
from shutil import copy
import xlrd

count=0
book = xlrd.open_workbook("manifest-report.xlsx")
sheet = book.sheets()[0]

def find_t(X):
	for k in range(3,sheet.nrows):
		if(sheet.col(1)[k].value==('C'+X)):
			string=sheet.col(3)[k].value
			array = string.split(",")
			#print array[0]
			return array[0]

def just_do_it():
	for m in DIR1list :
					#print m[0:9]
					#print a[0:9]
					if(m[0:9].lower()==a[0:9].lower()):
						try:
							copy('./IN-DIR/'+m, './NEW/'+i[8:-4]+'/'+m)
							#print "File ",m,"was present and copied to the folder"
						except:
							input("PN "+m+"was not present!! Please check! Enter to continue")
						return
	
DIR1list=sorted(os.listdir('./IN-DIR'))
DIR2list=sorted(os.listdir('./PN-DIR'))
for i in DIR1list :
	if(i[0:7]=='receipt') :
		print "\nCurrently Processing ... ",i[8:-4]		
		os.makedirs('./NEW/'+i[8:-4])
		copy('./IN-DIR/'+i, './NEW/'+i[8:-4]+'/'+i)
		#print "File ",i," is present"
		a=find_t(i[8:-4])
		#print "Person named ",a," is present in Manifest"
		just_do_it()
		for j in DIR2list :
			if(i[8:-4]==j[4:-4]):
				 k =copy('./PN-DIR/'+j, './NEW/'+j[4:-4]+'/'+j)
				 

NEWlist=sorted(os.listdir('./NEW'))
print "\n\n\n-------------Summary of files transferred-------------\n\n\n"
for i in NEWlist :
	print "Folder ",i," has ", len(os.listdir('./NEW/'+i))," files. Files are : ",os.listdir('./NEW/'+i)

print "\nFiles with inappropriate number files\n"
for i in NEWlist :
   if( len(os.listdir('./NEW/'+i)) != 3 ):
	count = count + 1 
	print "Folder ",i," has ", len(os.listdir('./NEW/'+i))," files only Files are : ",os.listdir('./NEW/'+i)

print "\nTotal ",len(os.listdir('./NEW'))," folders created"
print count," folders have issues"
print "______________________________________________"
key = raw_input("Press 'e' for exitting!!\n")
if key == 'e':
	quit()
