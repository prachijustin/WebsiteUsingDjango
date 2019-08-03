import pandas as pd
import sqlite3

def search(searchTerm):
    try:
        conn = sqlite3.connect('test.db')
        sql = "SELECT * FROM MAPPING WHERE COMPANY_NAME LIKE '%{0}%' OR CORPORATE_IDENTIFICATION_NUMBER LIKE '%{0}%' LIMIT 10".format(searchTerm)
        df = pd.read_sql(sql, conn)
        print(df.to_json(orient="records"))
        return df.to_json(orient="records")
    except Exception as e:
        print (str(e))

# @app.route('/search', methods=['GET'])
def fetch_company_data(cin, state):
    try:
        conn = sqlite3.connect('test.db')
        tableName = state.replace(" ", "_").upper()
        sql = "SELECT * FROM {} WHERE CORPORATE_IDENTIFICATION_NUMBER = '{}'".format(tableName, cin)
        df = pd.read_sql(sql, conn)
        print(df.to_dict(orient="records"))
        return df.to_dict(orient="records")
    except Exception as e:
        print (str(e))
# search("Tata Projects")
# fetch_company_data('U45200TG2013PLC088608', 'Telangana')
