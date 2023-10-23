from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')

def result(request):
    data = pd.read_csv('./resource/diabetes.csv')

    x = data.drop("Outcome", axis=1)
    y = data['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    model = LogisticRegression()
    model.fit(x_train, y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])




    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    result1 = ""
    if pred == [1]:
        result1 = "Positive"
    else:
        result1 = "Negative"

    return render(request,'report.html',{"result2":result1})
def predict2(request):
    return render(request,'predict2.html')

def result_2(request):
    heart_data = pd.read_csv('./resource/heart.csv')

    a = heart_data.drop("target", axis=1)
    b = heart_data['target']

    a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.2, stratify=b, random_state=2)

    model = LogisticRegression()
    model.fit(a_train, b_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    val13 = float(request.GET['n13'])
    val13 = float(request.GET['n13'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8,val9,val10,val11,val12,val13]])

    result4 = ""
    if pred == [1]:
        result4 = "Positive"
    else:
        result4 = "Negative"

    return render(request,'report_2.html',{"result3":result4})
