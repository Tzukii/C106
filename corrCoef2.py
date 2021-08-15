import plotly.express as px
import csv 
import numpy as np



def getDataSource(data_path):
    marks = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : marks, "y": days_present}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between marks in percentage and days present in class :-  \n--->",correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()