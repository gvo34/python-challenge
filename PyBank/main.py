#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period


import os
import csv

def average_change(revenuelist):
      allr = len(revenuelist)-1
      # average between 2 consecutive months      
      for r in range(0,allr):
            r1 = int(revenuelist[r])
            r2 = int(revenuelist[r+1])
            change = r2-r1
            avg_changes.append(change)
      return avg_changes
            
def print_financial_report(file_name, months, totalr, sum_av, sum_ch, greatest_incr, date_is, greatest_decr, date_ds):
      reportfile = os.path.join('output',file_name+'financial_report.txt')
      with open(reportfile,'w', newline = '') as reportf:
            print("Financial Report on "+file_name)#,file=reportf)
            print("===================================================================")#,file=reportf)
            print("  Total months reported: "+ months)
            print("  Total revenue: "+totalr+" over a period of "+str(len(years)-1)+" years")#,file=reportf)
            
            print("  The average revenue: " + str(sum_av)+" with average change of "+ str(sum_ch))#, file=reportf)
            print("  The greatest increase: " + str(greatest_incr) + " on " +date_is)#,file=reportf)
            print("  The greatest decrease: " + str(greatest_decr) + " on " +date_ds)#,file=reportf)

def read_financial_report(file_name):
      reportfile = os.path.join('output',file_name+'financial_report.txt')
      with open(reportfile,'r') as reportf:
            lines = reportf.read()
            print(lines)

input_file = ('budget_data_1','budget_data_2')
for file in input_file:
      # select input data file
      bankraw = os.path.join('data', file+'.csv')
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

      with open(bankraw, 'r') as bankfile:
        # Split the data on commas
        bankreader = csv.reader(bankfile, delimiter=',')
        # Loop through the data
        for row in bankreader:
          if row[1] == "Revenue":  #skip header
             next
          else:   
             row_date = row[0]
             rawdates.append(row_date)
             row_rev =  int(row[1])
             rawrevenues.append(row_rev)
             
             md = row_date.split('-')
             if current_year != md[1]:
                  years.append(md[1]) #new year recorded
                  current_year = md[1]
                  need_revenue = True                  
        
             if need_revenue:
                  revenues.append(total_revenue)
                  need_revenue = False
             total_revenue = total_revenue + row_rev
             
        # collect total
        revenues.append(total_revenue)
        averages = average_change(rawrevenues)

        #summary = zip (years, revenues)
        #for s in summary:
        #    print(s)
             

        months = str(len(rawdates))
        total = str(total_revenue)
        all_av = int(sum(rawrevenues)/len(rawrevenues))
        chg_av = int(sum(averages))/len(averages)
             
        g_incr = max(rawrevenues)
        date_i = rawrevenues.index(g_incr)
        d_incr = rawdates[date_i]       
        g_decr = min(rawrevenues)
        date_d = rawrevenues.index(g_decr)
        d_decr = rawdates[date_d]       
        
        print_financial_report(file, months, total, all_av, chg_av, g_incr, d_incr, g_decr, d_decr)
        print("Done ")
#          read_financial_report(file)
