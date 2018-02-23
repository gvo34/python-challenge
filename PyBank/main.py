#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period


import os
import csv

def average_revenue_change(revenuelist):
      # revenue change between 2 consecutive months
      avg_changes = []
      allr = len(revenuelist)-1
      for r in range(0,allr):
            r1 = int(revenuelist[r])
            r2 = int(revenuelist[r+1])
            change = r2-r1
            avg_changes.append(change)
      return avg_changes


def print_financial_report(file_name, months, totalr, sum_av, sum_ch, greatest_incr, date_is, greatest_decr, date_ds):
      # write report into given file name
      reportfile = os.path.join('output',file_name+'financial_report.txt')
      with open(reportfile,'w', newline = '') as reportf:
            print("Financial Report on "+file_name,file=reportf)
            print("===================================================================",file=reportf)
            print("  Total months reported: "+ months,file=reportf)
            print("  Total revenue: "+totalr,file=reportf)
            print("  The average revenue: " + str(sum_av)+" with average change of "+ str(sum_ch), file=reportf)
            print("  The greatest increase: " + str(greatest_incr) + " on " +date_is,file=reportf)
            print("  The greatest decrease: " + str(greatest_decr) + " on " +date_ds,file=reportf)


def create_financial_report(dates, revenues, total, chg_averages):
      # calculate totals
      months = str(len(dates))
      total = str(total)
      all_av = int(sum(revenues)/len(revenues))
      chg_av = int(sum(chg_averages))/len(chg_averages)
      
      g_incr = max(chg_averages) 
      date_i = chg_averages.index(g_incr) 
      d_incr = dates[date_i+1]       
      g_decr = min(chg_averages) 
      date_d = chg_averages.index(g_decr) 
      d_decr = dates[date_d+1]       
      
      print_financial_report(file, months, total, all_av, chg_av, g_incr, d_incr, g_decr, d_decr)


def read_financial_report(file_name):
      # read report from a file
      reportfile = os.path.join('output',file_name+'financial_report.txt')
      with open(reportfile,'r') as reportf:
            lines = reportf.read()
            print(lines)



# Provide a list of input files to read data from
input_file = ('budget_data_1','budget_data_2')

for file in input_file:
      bankraw = os.path.join('data', file+'.csv')
      rawrevenues = []
      rawdates = []
      total_revenue = 0

      with open(bankraw, 'r') as bankfile:
        bankreader = csv.reader(bankfile, delimiter=',')
        next(bankreader, None)  #skip header
        
        # Loop through the data
        for row in bankreader:
          row_date = row[0]
          rawdates.append(row_date)
          row_rev =  int(row[1])
          rawrevenues.append(row_rev)
             
          total_revenue = total_revenue + row_rev
             
        # collect change averages and reports
        averages = average_revenue_change(rawrevenues)
        
        create_financial_report(rawdates, rawrevenues, total_revenue, averages)
        
        read_financial_report(file)
