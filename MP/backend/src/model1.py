from db import Model
from pandas.core.groupby.groupby import IndexLabel
import pandas as pd
from sklearn import tree
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report

# !pip install category_encoders
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the dataset using pandas
df1 = pd.read_csv("datasets/students_adaptability_level_online_education.csv")
df = df1.drop(["Education Level", "IT Student", "Location"], axis=1)
df["Device"] = df["Device"].replace({"Tab", "Mobile", "Computer"}, {3, 2, 1})
df["Load-shedding"] = df["Load-shedding"].replace({"Low", "High"}, {1, 2})
df["Internet Type"] = df["Internet Type"].replace({"Wifi", "Mobile Data"}, {1, 2})
df["Gender"] = df["Gender"].replace({"Boy": 2, "Girl": 1})
df["Self Lms"] = df["Self Lms"].replace({"Yes", "No"}, {2, 1})
df.Age = df.Age.replace(
    {"21-25": 5, "16-20": 4, "11-15": 3, "26-30": 6, "6-10": 2, "1-5": 1}
)
df["Institution Type"] = df["Institution Type"].replace(
    {"Non Government", "Government"}, {2, 1}
)
df["Financial Condition"] = df["Financial Condition"].replace(
    {"Mid": 2, "Poor": 1, "Rich": 3}
)
df["Network Type"] = df["Network Type"].replace({"4G": 3, "3G": 2, "2G": 1})
df["Class Duration"] = df["Class Duration"].replace({"3-6": 3, "1-3": 2, "0": 1})
print(df.head())
y = df.pop("Adaptivity Level")
x = df
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, shuffle=True, stratify=y
)
student = DecisionTreeClassifier()
student = student.fit(x_train, y_train)
sdata = [
    {"identifier": "username", "label": "Enter Name:", "type": "text"},
    {
        "identifier": "Gender",
        "label": "Select Your Gender",
        "type": "radio",
        "options": ["Girl", "Boy"],
    },
    {
        "identifier": "Age",
        "label": "Select Your Age",
        "type": "select",
        "options": ["1-5", "6-10", "11-15", "16-20", "21-25", "26-30"],
    },
    {
        "identifier": "Institution Type",
        "label": "Select Institution Type",
        "type": "radio",
        "options": ["Government", "Non Government"],
    },
    {
        "identifier": "Load-shedding",
        "label": "Select amount of Load-shedding",
        "type": "radio",
        "options": ["Low", "High"],
    },
    {
        "identifier": "Financial Condition",
        "label": "Select Financial Condition",
        "type": "radio",
        "options": ["Poor", "Mid", "Rich"],
    },
    {
        "identifier": "Internet Type",
        "label": "Select Internet Type",
        "type": "radio",
        "options": ["Wifi", "Mobile Data"],
    },
    {
        "identifier": "Network Type",
        "label": "Select Network Type",
        "type": "radio",
        "options": ["2G", "3G", "4G"],
    },
    {
        "identifier": "Class Duration",
        "label": "Select Online Class Duration",
        "type": "select",
        "options": ["0", "1-3", "3-6"],
    },
    {
        "identifier": "Self Lms",
        "label": "Did you have self lms",
        "type": "radio",
        "options": ["No", "Yes"],
    },
    {
        "identifier": "Device",
        "label": "Select Device ",
        "type": "select",
        "options": ["Computer", "Mobile", "Tab"],
    },
]
adder = Model()


class Wrapper:
    def __init__(self, model, sdata):
        self.model = model
        self.sdata = sdata

    def predict(self, data):
        import pandas as pd

        a = [0] * 10
        for i in range(len(self.sdata) - 1):
            for j in range(len(self.sdata[i + 1]["options"])):
                if (
                    data[self.sdata[i + 1]["identifier"]]
                    == self.sdata[i + 1]["options"][j]
                ):
                    a[i] = [j + 1]
                    print(a[i])
        b = pd.DataFrame(a)
        ad = self.model.predict(b.transpose())
        if ad[0] == "Low":
            return "The Student has Low Adaptabiliy"
        if ad[0] == "Moderate":
            return "The Student has Moderate adaptability"
        if ad[0] == "High":
            return "The Student has High adaptability"


data = {
    "username": "h",
    "FromDiversityJobFairID": "Yes",
    "Termd": "new Employee",
    "Sex": "Female",
    "EmploymentStatus": "Terminated for Cause",
    "Department": "IT/IS",
    "RecruitmentSource": "Indeed",
    "EmpSatisfaction": 1,
    "SpecialProjectsCount": 5,
    "DaysLateLast30": 1,
}
test = {
    "username": "hello",
    "Gender": "Girl",
    "Age": "1-5",
    "Institution Type": "Government",
    "Load-shedding": "Low",
    "Financial Condition": "Poor",
    "Internet Type": "Wifi",
    "Network Type": "2G",
    "Class Duration": "0",
    "Self Lms": "No",
    "Device": "Mobile",
}
w1 = Wrapper(student, sdata)
adder.add_model(
    "Student_Adaptability",
    "Student adaptability to online classes refers to their ability to effectively adjust and thrive in the digital learning environment. It involves acquiring the necessary technological skills, managing time efficiently, staying motivated, and actively participating in virtual discussions and assignments to achieve academic success remotely",
    w1,
    sdata,
)
print(adder.get_model("Student_Adaptability").predict(test))
