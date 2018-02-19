import os
import csv

rawrevenues = []
rawdates = []
total_revenue = 0
years = ['YEAR']
months = []
current_year = 0
revenues = [] #revenues per year
need_revenue = False
avg_changes = []

greatest_increase = 0
greatest_decrease = 0

bankraw = os.path.join('Generators','budget_data2.csv')

def average_change(revenuelist):
      allr = len(revenuelist)-1
      # average between 2 consecutive months      
      for r in range(0,allr):
            r1 = int(revenuelist[r])
            r2 = int(revenuelist[r+1])
            change = (r1+r2)/2
            avg_changes.append(change)


def print_financial_report():
      reportfile = os.path.join('output','financial_report.txt')
      with open(reportfile,'w', newline = '') as reportf:
            print("Financial Report",file=reportf)
            print("===================================================================",file=reportf)
            print("Read " + str(len(rawdates)) +  " Months with total revenue of "+ str(total_revenue),file=reportf)
            print("counted "+str(len(years)-1)+" years with accumulative revenues of",file=reportf)
            sum_av = int(sum(rawrevenues)/len(rawrevenues))
            print ("the average revenue change " + str(sum_av),file=reportf)
            greatest_increase = max(rawrevenues)
            date_i = rawrevenues.index(greatest_increase)
            date_is = rawdates[date_i]       
            print("The greatest increase was " + str(greatest_increase) + " on " +date_is,file=reportf)
            greatest_decrease = min(rawrevenues)
            date_i = rawrevenues.index(greatest_decrease)
            date_is = rawdates[date_i]       
            print("The greatest decrease was " + str(greatest_decrease) + " on " +date_is,file=reportf)
            print("printing...")

      #summary = zip (years, revenues)
      #for s in summary:
      #      print(s)

def read_financial_report():
      reportfile = os.path.join('output','financial_report.txt')
      with open(reportfile,'r') as reportf:
            lines = reportf.read()
            print(lines)



with open(bankraw, 'r') as bankfile:
    # Split the data on commas
    bankreader = csv.reader(bankfile, delimiter=',')
    # Loop through the data
    for row in bankreader:
          #skip header
          if row[1] != "Revenue":
             row_date = row[0]
             rawdates.append(row_date)
             row_rev =  int(row[1])
             rawrevenues.append(row_rev)

             md = row_date.split('-')
             if current_year != md[1]:
                  years.append(md[1]) #new year recorded
                  current_year = md[1]
                  need_revenue = True                  
             #print(" year "+current_year+" , month "+str(md[0]) + " add "+str(row_rev)+ " to " +str(yearly_revenue))
             if need_revenue:
                  revenues.append(total_revenue)
                  need_revenue = False
             total_revenue = total_revenue + row_rev                                                              
    revenues.append(total_revenue)
    average_change(rawrevenues)

print_financial_report()
print("Done ")
read_financial_report()
