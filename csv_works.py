#Reference : http://www.geeksforgeeks.org/working-csv-files-python/

import csv
 
# header names
fields = ['name', 'branch', 'year', 'cgpa']
 
# 1. write data rows
rows = [ ['Nikhil', 'COE', '2', '9.0'],
         ['Sanchit', 'COE', '2', '9.1'],
         ['Aditya', 'IT', '2', '9.3'],
         ['Sagar', 'SE', '1', '9.5'],
         ['Prateek', 'MCE', '3', '7.8'],
         ['Sahil', 'EP', '2', '9.1']]
 
# writing to csv file using writer method
with open("writercsvfile.csv", 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile,lineterminator="\n\n",delimiter="-")
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)


# 2. write data rows as dictionary objects
mydict =[{'name': 'Nikhil','branch': 'COE', 'cgpa': '9.0','year': '2'},
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
         {'branch': 'IT', 'cgpa': '9.3','year': '2','name': 'Aditya'},
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

# writing to csv file using DictWriter method
with open('dictwritercsvfile.csv', 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)
     
    # writing headers (field names)
    writer.writeheader()
     
    # writing data rows
    writer.writerows(mydict)


# 3. read csv file
fields = []
rows = []
 
# reading csv file using reader method
with open('writercsvfile.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter='-')                 # creating a csv reader object
    
    fields = next(csvreader)                       # fetch headers
 
    for row in csvreader:
        rows.append(row)
 
    print("Total no. of rows: %d"%(csvreader.line_num)) # get total number of rows

print('Field names are:' + " ".join(fields))

for row in rows:
    print(*row)


# 4. read csv file
with open('writercsvfile.csv','r') as csvfile:
    dictcsvreader = csv.DictReader(csvfile,delimiter='-')

    for row in dictcsvreader:                                       # headers known, used as keys
        print(row['name'],row['branch'],row['year'],row['cgpa'])