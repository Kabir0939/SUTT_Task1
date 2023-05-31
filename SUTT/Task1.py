import pandas as pd
datapath = "https://docs.google.com/spreadsheets/d/1jPq_zyLptX3My07oOxUpsrkPYJUB_ryEst8KA4dvMfk/export?format=csv"
data = pd.read_csv(datapath)
name = data.Name
id = data.iloc[:,1]
s1 = slice(4)
s2 = slice(8,12)
s3 = slice(4,6)
s4 = slice(6,8)
container = []
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
while x<len(name):  
    if(name[x][s4]=="PS"):
      d = "Single Degree "
      d+= list[name[x][s3]]
    else:
      d = "Dual Degree "
      d += list[name[x][s3]]+" + "+list[name[x][s4]]
        
    container.append( {
       
        "Name": id[x] , "Bits ID":  name[x],"Bits Mail": ("f"+name[x][s1]+name[x][s2]+"@pilani.bits-pilani.ac.in"),
                       "Branch": d      
                         } )
    x = x + 1
for y in container:    
    print(y)
    