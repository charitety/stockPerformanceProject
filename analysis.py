import statistics as st
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt


#DIS: Walt Disney
DISdata = []
with open("DIS.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #Saving this DictReader object into a list of dictionaries to analyze
    for row in reader:
        DISdata.append(row)

i = 0 
DISstdiv = []
while i < len(DISdata):
    if i + 1 >= len(DISdata) or i + 2 >= len(DISdata) or i + 3 >= len(DISdata) or i + 4 >= len(DISdata):
        break
    day1 = float(DISdata[i]["price"])
    day2 = float(DISdata[i + 1]["price"])
    day3 = float(DISdata[i + 2]["price"])
    day4 = float(DISdata[i + 3]["price"])
    day5 = float(DISdata[i + 4]["price"])
    x = st.pstdev([day1,day2,day3,day4,day5]) 
    DISstdiv.append(x)
    i += 5

#DIS: Visualization
plt.plot(DISstdiv)
plt.xlabel("Weeks") 
plt.ylabel("Standard Deviation of Closing Price")  
plt.title("Weekly Standard Deviations of Walt Disney (Apr 2021- Mar 2022)") 
plt.savefig("DISstdiv.png")
plt.show()


#GOOGL: Alphabet Inc.(Google) 
GOOGLdata = []
with open("GOOGL.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #Saving this DictReader object into a list of dictionaries to analyze
    for row in reader:
        GOOGLdata.append(row)

i = 0 
GOOGLstdiv = []
while i < len(GOOGLdata):
    if i + 1 >= len(GOOGLdata) or i + 2 >= len(GOOGLdata) or i + 3 >= len(GOOGLdata) or i + 4 >= len(GOOGLdata):
        break
    day1 = float(GOOGLdata[i]["price"])
    day2 = float(GOOGLdata[i + 1]["price"])
    day3 = float(GOOGLdata[i + 2]["price"])
    day4 = float(GOOGLdata[i + 3]["price"])
    day5 = float(GOOGLdata[i + 4]["price"])
    x = st.pstdev([day1,day2,day3,day4,day5]) 
    GOOGLstdiv.append(x)
    i += 5

#GOOGL: Visialization
plt.plot(GOOGLstdiv)
plt.xlabel("Weeks") 
plt.ylabel("Standard Deviation of Closing Price")  
plt.title("Weekly Standard Deviations of Google (Apr 2021- Mar 2022)") 
plt.savefig("GOOGLstdiv.png")
plt.show()

#ME: 23andMe Holding Co.
MEdata = []
with open("ME.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #Saving this DictReader object into a list of dictionaries to analyze
    for row in reader:
        MEdata.append(row)

i = 0 
MEstdiv = []
while i < len(MEdata):
    if i + 1 >= len(MEdata) or i + 2 >= len(MEdata) or i + 3 >= len(MEdata) or i + 4 >= len(MEdata):
        break
    day1 = float(MEdata[i]["price"])
    day2 = float(MEdata[i + 1]["price"])
    day3 = float(MEdata[i + 2]["price"])
    day4 = float(MEdata[i + 3]["price"])
    day5 = float(MEdata[i + 4]["price"])
    x = st.pstdev([day1,day2,day3,day4,day5]) 
    MEstdiv.append(x)
    i += 5

#ME: Visualization
plt.plot(MEstdiv)
plt.xlabel("Weeks") 
plt.ylabel("Standard Deviation of Closing Price")  
plt.title("Weekly Standard Deviations of 23andMe Holding Co.(June 2021 - Mar 2022)") 
plt.savefig("MEstdiv.png")
plt.show()


#NVAX: Novavax Inc.
NVAXdata = []
with open("NVAX.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #Saving this DictReader object into a list of dictionaries to analyze
    for row in reader:
        NVAXdata.append(row)

i = 0 
NVAXstdiv = []
while i < len(NVAXdata):
    if i + 1 >= len(NVAXdata) or i + 2 >= len(NVAXdata) or i + 3 >= len(NVAXdata) or i + 4 >= len(NVAXdata):
        break
    day1 = float(NVAXdata[i]["price"])
    day2 = float(NVAXdata[i + 1]["price"])
    day3 = float(NVAXdata[i + 2]["price"])
    day4 = float(NVAXdata[i + 3]["price"])
    day5 = float(NVAXdata[i + 4]["price"])
    x = st.pstdev([day1,day2,day3,day4,day5]) 
    NVAXstdiv.append(x)
    i += 5

#NVAX: Visualization
plt.plot(NVAXstdiv)
plt.xlabel("Weeks") 
plt.ylabel("Standard Deviation of Closing Price")  
plt.title("Weekly Standard Deviations of Novavax Inc (Apr 2021- Mar 2022)") 
plt.savefig("NVAXstdiv.png")
plt.show()

PFEdata = []
with open("PFE.csv", "r") as infile:
    reader = csv.DictReader(infile)
    #Saving this DictReader object into a list of dictionaries to analyze
    for row in reader:
        PFEdata.append(row)

i = 0 
PFEstdiv = []
while i < len(PFEdata):
    if i + 1 >= len(PFEdata) or i + 2 >= len(PFEdata) or i + 3 >= len(PFEdata) or i + 4 >= len(PFEdata):
        break
    day1 = float(PFEdata[i]["price"])
    day2 = float(PFEdata[i + 1]["price"])
    day3 = float(PFEdata[i + 2]["price"])
    day4 = float(PFEdata[i + 3]["price"])
    day5 = float(PFEdata[i + 4]["price"])
    x = st.pstdev([day1,day2,day3,day4,day5]) 
    PFEstdiv.append(x)
    i += 5

# PFE: Visualization
plt.plot(PFEstdiv)
plt.xlabel("Weeks") 
plt.ylabel("Standard Deviation of Closing Price")  
plt.title("Weekly Standard Deviations of Pfizer Inc. (Apr 2021- Mar 2022)") 
plt.savefig("PFEstdiv.png")
plt.show()











