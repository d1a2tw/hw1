

# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '105061151.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive ten data points from the beginning.


#target_data = data[:12]
list=["C0A880","C0F9A0","C0G640","C0R190","C0X260"]
dict={list[0]:"none",list[1]:"none",list[2]:"none",list[3]:"none",list[4]:"none"}


data2=[]
i=0

while i<len(data):
  if data[i]["WDSD"]!="-99.000" and data[i]["WDSD"]!="-999.000" :
       
       
       data2.append(data[i])

  i=i+1


search=0
while search<5:
  
   max=-100.0
   min=+100.0
   i=0
   num=0
   
   while i<len(data2):
      
     
      if data2[i]["station_id"]==list[search]:
         num=num+1
         hello=float(data2[i]["WDSD"])
      
     
      
         if hello>max:
            max=hello
         

         if hello<min:
            min=hello
       
      i=i+1
   
  

   diff=abs(max-min)
   if num!=0 and diff!=0 :
      
      dict[list[search]]=str(diff)
   

   search=search+1



print[ [list[0],dict[list[0]]],[list[1],dict[list[1]]],[list[2],dict[list[2]]],[list[3],dict[list[3]]],[list[4],dict[list[4]]]     ]



#=======================================


# Part. 4

#=======================================

# Print result

#print(target_data)

#print(data)

#========================================