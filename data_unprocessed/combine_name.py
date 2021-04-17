# import xlrd

# def extract(inpath, resfile):
# 	data=xlrd.open_workbook(inpath, encoding_override='uft-8')
# 	table=data.sheets()[0]
# 	nrows=table.nrows
# 	ncols=table.ncols

# 	for i in range(1, nrows):
# 		alldata=table.row_values(i)
# 		cyr=alldata[0]
# 		lat=alldata[2]
# 		line=cyr+'|'+lat
# 		resfile.write(line)


# with open("names_combined.txt","w") as resfile:
# 	inpath='mongolian_clan_names'

import csv
filename='mongolian_clan_names.csv'
combine=[]

with open(filename,'r') as csvfile:
	with open('name_combined.txt','w') as resfile:
		reader=csv.reader(csvfile)
		rows=list(reader)

		for row in rows:
			cyr=row[0]
			lat=row[2]
			line=cyr+'|'+lat+'\n'
			resfile.write(line)

