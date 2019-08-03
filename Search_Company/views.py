from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import pandas as pd
import sqlite3

def search(request):
    if request.method == "GET":
        searchTerm = request.GET.get('searchTerm')
        print(searchTerm)
        try:
            conn = sqlite3.connect('test.db')
            sql = "SELECT * FROM MAPPING WHERE COMPANY_NAME LIKE '%{0}%' OR CORPORATE_IDENTIFICATION_NUMBER LIKE '%{0}%' LIMIT 10".format(searchTerm)
            df = pd.read_sql(sql, conn)
            # return df.to_json(orient="records"))
            # print(df.to_json(orient="records"))
            df = df.rename(columns={"COMPANY_NAME": "name", "CORPORATE_IDENTIFICATION_NUMBER": "cin", "REGISTERED_STATE": "state"})
            myjson = df.to_json(orient="records")
            # print (myjson)
            return HttpResponse(myjson, content_type="application/json")
        except Exception as e:
            print (str(e))

    else:
        # print("error")
        return HttpResponse("ERROR")

# @app.route('/search', methods=['GET'])
def fetch_company_data(request):
    try:
        cin = request.GET['cin']
        state = request.GET['state']
        # print (cin, state)
        conn = sqlite3.connect('test.db')

        tableName = state.replace(" ", "_").upper()
        sql = "SELECT * FROM {} WHERE CORPORATE_IDENTIFICATION_NUMBER = '{}'".format(tableName, cin)
        df = pd.read_sql(sql, conn)
        ds={}
        df = df.to_dict()
        for d in df.keys():
            ds[d]=df[d][0]
        # print(ds)
        return render(request, "show_company.html",context=ds)
        # return df.to_dict(orient="records")
    except Exception as e:
        # print (str(e))
        return HttpResponse("Text only, please.", content_type="text/plain")
# search("Tata Projects")
# fetch_company_data('U45200TG2013PLC088608', 'Telangana')

# # Create your views here.
def search_company(request):
     return render(request,'search_company.html')
