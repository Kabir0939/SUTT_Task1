import pandas as pd

#reading google spreadsheet as csv file through url 
datapath = "https://docs.google.com/spreadsheets/d/1jPq_zyLptX3My07oOxUpsrkPYJUB_ryEst8KA4dvMfk/export?format=csv"
data = pd.read_csv(datapath)


id = data.Name #this list contains Bits ID of all the Students
name = data.iloc[:,1] #this list contains names of all the Students
s1 = slice(4)
s2 = slice(8,12)
s3 = slice(4,6)
s4 = slice(6,8)
container = []

#List ocontaining all the branches
list = {
"AA": "ECE",
"AB": "Manu",
"A1" : "Chemical",
"A2" : "Civil",
"A3" : "EEE",
"A4" : "Mech",
"A5" : "Pharma",
"A7" : "CSE",
"A8" : "ENI",
"B1" : "MSc BIO",
"B2" : "MSc Chem",
"B3" : "MSc Eco",
"B4" : "MSc Mathematics",
"B5" : "MSc Physics"
}
x=0
while x<len(id):  
    
#To check Whether the student is Single Degree or Dual Degree and add the branches of all the students
    if(id[x][s4]=="PS"):
      d = "Single Degree "
      d+= list[id[x][s3]]
    else:
      d = "Dual Degree "
      d += list[id[x][s3]]+" + "+list[id[x][s4]]
        
#Storing the name , Bits ID , Bits mail , Branch as Dictionary  
    container.append( {
       
        "Name": name[x] , "Bits ID":  id[x],"Bits Mail": ("f"+id[x][s1]+id[x][s2]+"@pilani.bits-pilani.ac.in"),
                       "Branch": d      
                         } )
    x = x + 1

#printing all the detailes of the students     
for y in container:    
    print(y) 
    
