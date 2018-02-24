#Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:
#Emp ID,Name,DOB,SSN,State
#214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#15,Samantha Lara,1993-09-08,848-80-7526,Colorado
#411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
#Then convert and export the data to use the following format instead:
#Emp ID,First Name,Last Name,DOB,SSN,State
#214,Sarah,Simpson,12/04/1985,***-**-8166,FL
#315,Samantha,Lara,09/08/1993,***-**-7526,CO
#411,Stacy,Charles,12/20/1957,***-**-8526,PA

import csv
import os


def format_name(fullname):
    listname = []
    name = fullname.split(' ')
    listname.append(name[0])
    listname.append(name[1])
    return listname
    
def format_DOB(fulldate):
    date = fulldate.split('-')
    day = date[2]
    month = date[1]
    year = date[0]
    redate = day+'/'+month+'/'+year
    return redate

def format_SIN(snumber):
    employee_SIN = str(snumber)
    ucoded = employee_SIN.split('-')
    sencode = '***-**-'+str(ucoded[2])
    return sencode


def format_ST(state):
    states = {'Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA','Colorado':'CO','Connecticut':'CT','Delaware':'DE','Florida':'FL','Georgia':'GA','Hawaii':'HI','Idaho':'ID','Illinois':'IL','Indiana':'IN','Iowa':'IA','Kansas':'KS','Kentucky':'KY','Louisiana':'LA','Maine':'ME','Maryland':'MD','Massachusetts':'MA','Michigan':'MI','Minnesota':'MN','Mississippi':'MS','Missouri':'MO','Montana':'MT','Nebraska':'NE','Nevada':'NV','New Hampshire':'NH','New Jersey':'NJ','New Mexico':'NM','New York':'NY','North Carolina':'NC','North Dakota':'ND','Ohio':'OH','Oklahoma':'OK','Oregon':'OR','Pennsylvania':'PA','Rhode Island':'RI','South Carolina':'SC','South Dakota':'SD','Tennessee':'TN','Texas':'TX','Utah':'UT','Vermont':'VT','Virginia':'VA','Washington':'WA','West Virginia':'WV','Wisconsin':'WI','Wyoming':'WY'}

    statename = state.strip()
    st = states[statename]
    return st


def write_records(data,file):
    
    filepath = os.path.join('output',file+'_report.csv')

    with open(filepath,'w',newline='') as reportfile:
        # Initialize csv.writer
        report = csv.writer(reportfile, delimiter=',')
        # Write the first row (column headers)
        report.writerow(['#Emp ID','First Name','Last Name','DOB','SSN','State'])
    
        for record in data:
            report.writerow(record)


def read_data(datafile):
      # read report from a file
      reportfile = os.path.join('output',datafile+'_report.csv')
      with open(reportfile,'r') as reportf:
            lines = reportf.read()
            print(lines)


def format_record_fields(datafile):
    filepath = os.path.join('data',datafile+'.csv')

    with open (filepath, 'r') as employee_data:
        employee_record = csv.reader(employee_data,delimiter=',')
        next(employee_record,None)   # skip header

        newdata = []

        for employee in employee_data:
            e_data = employee.split(',')
        
            first_last = format_name(e_data[1])
            redate = format_DOB(e_data[2])
            encoded = format_SIN(e_data[3])
            state = format_ST(e_data[4])

            #build the new record
            record = []
            record.append(e_data[0])
            record.append(first_last[0])
            record.append(first_last[1])
            record.append(redate)
            record.append(encoded)
            record.append(state)  
    
            newdata.append(record)

        return newdata


def PyBoss(files):
    for datafile in files:
        newrecords = format_record_fields(datafile)
        write_records(newrecords,datafile)
        read_data(datafile)


input_files = ('employee_data1','employee_data2')
PyBoss(input_files)



