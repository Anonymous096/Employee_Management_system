# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 11:52:32 2021
@author: Saksham
"""

import pandas as pd
import matplotlib.pyplot as plt

def menu():
    print('\n\n\n\n\n***************************************************************')
    print('                  Employee Management System                   ')
    print('***************************************************************\n')
    print("1. Data Analysis")
    print("2. Data Manipulation")
    print("3. Data Visualization")
    print("0. Exit")
    print("****************************************************************")

def sub_menu1():
    print("      1. Reading CSV file")
    print("      2. Reading file without Index")
    print("      3. Reading file with new Column names")

def sub_menu2():
    print("      1. Reading few rows ")
    print("      2. Read 3 records from top and 2 from bottom from File")
    print("      3. Duplicate file with new name")
    print("      4. Read with specific columns  ")
    print("      5. Create csv file with dataframe ")
    print("      6. Read csv file - emp  ")
    print("      7. Find Maximum Salary  ")
    print("      8. Create datailemp file with data given in df2    ")

def sub_menu3():
    print("      1. Line Plot")
    print("      2. Bar Plot")

def read():
    print()     
    print('****************************************************************')
    print("                          Data Analysis                         ")
    print('****************************************************************')
    print()
    Data = pd.read_csv('D:\Employee Management Sys\EmpMgmt.csv')
    print(Data)

def no_index():
    Data2 = pd.read_csv('D:\Employee Management Sys\EmpMgmt.csv', index_col=0)
    print()
    print('                         WITHOUT INDEX                              ')
    print(Data2)

def new_clonam():
    df=pd.read_csv("D:\Employee Management Sys\EmpMgmt.csv",skiprows=1,names=[ 'EID' ,'Ename','Age','Residence','Post','salary', 'Mobile'])
    print()
    print(df)
#new_clonam()

def readRow():
    print('*****************************************************************')
    print('                        Data Manipulation                        ')
    print('*****************************************************************')
    print("                             Reading few rows                    \n")
    df = pd.read_csv('D:\Employee Management Sys\EmpMgmt.csv', nrows=3)
    print(df)
    df = pd.read_csv('D:\Employee Management Sys\EmpMgmt.csv', nrows=5)
    print('\n', df)
#readRow()    
    
def top_bottom():
    print('\n                Reading top 3 rows and last 2 rows from file    \n')
    df=pd.read_csv("D:\Employee Management Sys\EmpMgmt.csv")
    #print(df)
    print('              top 3 rows           \n')
    print(df.head(3))
    print('\n             last 2 rows           \n')
    print(df.tail(2))

def duplicate():
    print('                     Duplicate file with new name               \n')
    print("           duplicate file with new name as empnew           \n")
    df=pd.read_csv("D:\Employee Management Sys\EmpMgmt.csv")
    df.to_csv("EmpMgmt2.csv")
    print(df)
#duplicate()

def spec_col():
    print('\n                     Read With Specific Columns                 \n')
    df=pd.read_csv("D:\Employee Management Sys\EmpMgmt.csv",usecols=['EmpID' ,'Name','Salary'])
    print(df)
#spec_col()

def create_file():
    print('\n                   Create csv file with dataframe                 \n')
    students={'New Emplyee':[110,111,112,113,114,115],'Name':['Sunil','Amit','Neeta','Umar','Ajay','Ravi']}
    df1=pd.DataFrame(students)
    print(df1)
    df1.to_csv("EmpMgmt3.csv")
#create_file()

def csv():
    print('\n                           Read csv file - emp                    \n')
    print( '                        Reading File emp                     \n')
    df=pd.read_csv("D:\Employee Management Sys\EmpMgmt.csv")
    print(df)
#csv()

def maxsal():
    print('\n                            Find Maximum Salary                  \n')
    df=pd.read_csv("D:\Employee Management Sys\EmpMgmt.csv")
    print("Highest Salary")
    print(df.Salary.max())
#maxsal()

def create_detailemp():
    print('\n               Create datailemp file with data given in df2      \n')
    employee={'First Name':['Tarun','Arvind','Bhuvan','Rakesh'],'Last Name':['Kumar','Jain','Gupta','Kumar'],
              'Father Name':['S.K.Kumar','Rajinder Jain','Ravinder Gupta','J.Kumar']}
    df2=pd.DataFrame(employee)
    print(df2)
    df2.to_csv("EmpMgmt4.csv")
#create_detailemp()

def line_graph():
    print('\n*****************************************************************')
    print('                         Data Visualization                      ')
    print('*****************************************************************\n')
    print('                         LINE GRAPH                              ')
    df = pd.read_csv('D:\Employee Management Sys\EmpMgmt.csv')

    x = df['Name']
    y = df['Salary']

    plt.xlabel('Name')
    plt.ylabel('Salary')

    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()
#line_graph()

def bar_graph():
    print('\n           BAR GRAPH                              ')
    df2 = pd.read_csv('D:\Employee Management Sys\EmpMgmt.csv')

    x = df2['Name']
    y = df2['Salary']

    plt.xlabel('Name')
    plt.ylabel('Salary')

    plt.bar(x, y)
    plt.show()
#bar_graph()

menu()
opt = int(input("Enter Your Choice: "))
while opt!=0:
    if opt==1:
        sub_menu1()
        opt1=""
        opt1=int(input('Choose The Option: '))
        if opt1==1:
            read()
        elif opt1==2:
            no_index()
        elif opt1==3:
            new_clonam()
        else:
            print('Invalid Option')
        
    elif opt==2:
        sub_menu2()
        opt2=""
        opt2=int(input('Choose The Option: '))
        if opt2==1:
            readRow()
        elif opt2==2:
            top_bottom()
        elif opt2==3:
             duplicate()
        elif opt2==4:
             spec_col()
        elif opt2==5:
             create_file()
        elif opt2==6:
             csv()
        elif opt2==7:
             maxsal()
        elif opt2==8:
             create_detailemp()
        else:
            print('invalid option')
    elif opt==3:
        sub_menu3()
        opt3=""
        opt3=int(input('Choose Your Option: '))
        if opt3==1:
         line_graph()
        elif opt3==2:
             bar_graph()
        else:
            print('invalid option')
    else:
        print("Invalid Choice")
    
    menu()
    opt = int(input("Enter Your Choice: "))    
