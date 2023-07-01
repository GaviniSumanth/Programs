import pandas as pd
from sklearn import tree
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report

# !pip install category_encoders
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from db import Model

# Load the dataset using pandas
df1 = pd.read_csv("datasets/HRDataset_v14.csv")
print(df1.columns)
df = df1.drop(
    [
        "ManagerName",
        "ManagerID",
        "LastPerformanceReview_Date",
        "MaritalDesc",
        "CitizenDesc",
        "HispanicLatino",
        "RaceDesc",
        "State",
        "Zip",
        "DOB",
        "Employee_Name",
        "EmpID",
        "MarriedID",
        "MaritalStatusID",
        "GenderID",
        "DeptID",
        "EmpStatusID",
        "PerfScoreID",
        "Position",
        "DateofHire",
        "DateofTermination",
        "TermReason",
        "Absences",
        "EngagementSurvey",
        "PositionID",
        "Salary",
    ],
    axis=1,
)
print(df.columns)
a = [
    "FromDiversityJobFairID",
    "Termd",
    "Sex",
    "EmploymentStatus",
    "Department",
    "RecruitmentSource",
    "PerformanceScore",
    "EmpSatisfaction",
    "SpecialProjectsCount",
    "DaysLateLast30",
]
df["Sex"] = df["Sex"].replace({"M", "F"}, {2, 1})
df["Department"] = df["Department"].replace(
    {
        "Production",
        "IT/IS",
        "Software Engineering",
        "Admin Offices",
        "Sales",
        "Executive Office",
    },
    {6, 5, 4, 3, 2, 1},
)
df["RecruitmentSource"] = df["RecruitmentSource"].replace(
    {
        "LinkedIn",
        "Indeed",
        "Google Search",
        "Employee Referral",
        "Diversity Job Fair",
        "On-line Web application",
        "CareerBuilder",
        "Website",
        "Other",
    },
    {9, 8, 7, 6, 5, 4, 3, 2, 1},
)
df["EmploymentStatus"] = df["EmploymentStatus"].replace(
    {"Active", "Voluntarily Terminated", "Terminated for Cause"}, {3, 2, 1}
)
for i in range(len(a)):
    print(a[i])
    print(df[a[i]].unique())

y = df.pop("PerformanceScore")
x = df
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, shuffle=True, stratify=y
)
HR = DecisionTreeClassifier()
HR = HR.fit(x_train, y_train)
# tree.plot_tree(HR)
# y1_pred = HR.predict(x_test)
# y1_pred.reshape(-1, 1)
# print(y1_pred)
# print(type(y1_pred))
# HR.predict_proba(x_test)
# confusion = confusion_matrix(y_test, y1_pred)
# print('Confusion Matrix\n')
# print(confusion)
# disp = ConfusionMatrixDisplay(confusion)
# disp.plot()
# plt.show()
# print('\nClassification Report\n')
# print(classification_report(y_test, y1_pred))
hdata = [
    {"identifier": "username", "label": "Enter Name:", "type": "text"},
    {
        "identifier": "FromDiversityJobFairID",
        "label": "Select Diversity Job Fair",
        "type": "radio",
        "options": ["No", "Yes"],
    },
    {
        "identifier": "Termd",
        "label": "Select Term",
        "type": "radio",
        "options": ["new Employee", "Old Employee"],
    },
    {
        "identifier": "Sex",
        "label": "Select Gender",
        "type": "radio",
        "options": ["Male", "Female"],
    },
    {
        "identifier": "EmploymentStatus",
        "label": "Select Employment Status",
        "type": "radio",
        "options": ["Active", "Voluntarily Terminated", "Terminated for Cause"],
    },
    {
        "identifier": "Department",
        "label": "Select Department",
        "type": "select",
        "options": [
            "Production",
            "IT/IS",
            "Software Engineering",
            "Admin Offices",
            "Sales",
            "Executive Office",
        ],
    },
    {
        "identifier": "RecruitmentSource",
        "label": "Select Recruitment Source ",
        "type": "select",
        "options": [
            "LinkedIn",
            "Indeed",
            "Google Search",
            "Employee Referral",
            "Diversity Job Fair",
            "On-line Web application",
            "CareerBuilder",
            "Website",
            "Other",
        ],
    },
    {
        "identifier": "EmpSatisfaction",
        "label": "Select Employee Satisfaction ",
        "type": "number",
        "options": ["1", "2", "3", "4", "5"],
        "min": 1,
        "max": 5,
    },
    {
        "identifier": "SpecialProjectsCount",
        "label": "Select no of Special Projects",
        "type": "number",
        "options": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "min": 1,
        "max": 9,
    },
    {
        "identifier": "DaysLateLast30",
        "label": "Select Days Late in Last 30 Days",
        "type": "number",
        "options": ["1", "2", "3", "4", "5", "6", "7"],
        "min": 1,
        "max": 7,
    },
]
adder = Model()
# adder.add_model("HRDataset",
#                 "The Employee performance can be calculated using different Parameters which can be easily gathered and used to make biasless decision on their performance",
#                 HR, Hrdata)
# print(adder.get_model("HRDataset").predict(x_test))
data1 = {
    "username": "h",
    "FromDiversityJobFairID": "Yes",
    "Termd": "new Employee",
    "Sex": "Female",
    "EmploymentStatus": "Terminated for Cause",
    "Department": "IT/IS",
    "RecruitmentSource": "Indeed",
    "EmpSatisfaction": "1",
    "SpecialProjectsCount": "5",
    "DaysLateLast30": "1",
}
# print(len(hdata))
# q = [0]*9
# print(len(q))
# print(q)


class Wrapper:
    def __init__(self, model, hdata):
        self.model = model
        self.hdata = hdata

    def predict(self, data):
        import pandas as pd

        a = [0] * 9
        for i in range(len(self.hdata) - 1):
            for j in range(len(self.hdata[i + 1]["options"])):
                if (
                    data[self.hdata[i + 1]["identifier"]]
                    == self.hdata[i + 1]["options"][j]
                ):
                    a[i] = [j + 1]
                    print(a)
        b = pd.DataFrame(a)
        ad = self.model.predict(b.transpose())
        if ad[0] == "Exceeds":
            return "The Employee Exceeds in his Performance"
        if ad[0] == "Fully Meets":
            return "The Employee Fully Meets in his Performance"
        if ad[0] == "Needs Improvement":
            return "The Employee Needs Improvement in his Performance"
        if ad[0] == "PIP":
            return "The Employee's Performance is below expectitions"


w2 = Wrapper(HR, hdata)
adder.add_model(
    "HRDataset",
    "The Employee performance can be calculated using different Parameters which can be easily gathered and used to make biasless decision on their performance",
    w2,
    hdata,
)
print(adder.get_model("HRDataset").predict(data1))
# def Hwrap(data):
#     a = []
#     for key in data.keys():
#         for i in range(len(hdata)-1):
#             for j in range(len(hdata[i+1]['options'])):
#                 # print(hdata[i+1]['options'])
#                 # print(data[key])
#                 if (data[key]) == (hdata[i+1]['options'][j]):
#                     print(key, end="+")
#                     print(type(data[key]))
#                     print(type(hdata[i+1]['options'][j]))
#                     print(hdata[i+1]['options'][j])
#                     a.insert(j+1, [j+1])
#                     break
#     b = pd.DataFrame(a)
#     print(a)
#     print(type(data['EmpSatisfaction']))
#     print(type(hdata[7]['options'][3]))
#     if (data['EmpSatisfaction'] == hdata[7]['options'][3]):
#         print("yes")
#     ad = adder.get_model("HRDataset").predict(b.transpose())
#     c = ad[0]
#     return c
#     pass
# Hwrap(data)
