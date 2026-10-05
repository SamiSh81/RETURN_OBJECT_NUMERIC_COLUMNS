# Calling Pandas Libray
import pandas as pd
# Reading dataset
data=pd.read_csv("StudentsPerformance.csv")

# Creating two lists
lst_obj_data=[]
lst_numeric_data=[]
def ReturnObjectDataSet():
    for count_lst_obj in (data.select_dtypes(include=["object"])):
        lst_obj_data.append(count_lst_obj)
    return lst_obj_data

# Returning numeric dataset
def ReturnNumericDataSet():
    for count_lst_numeric in (data.select_dtypes(exclude=["object"])):
        lst_numeric_data.append(count_lst_numeric)
    return lst_numeric_data

# The procedure printing columns of dataset
def ProceduerPrintDataset():
    print("The object dataset:",ReturnObjectDataSet())
    print("The numeric dataset:",ReturnNumericDataSet())

ProceduerPrintDataset()




