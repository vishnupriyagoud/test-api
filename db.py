from flask import jsonify
import pymysql
from decimal import Decimal

def query(querystr , return_json=True):
    connection=pymysql.connect(host="localhost",
                                user="root",
                                password="Priya1116",
                                db="testapi",
                                cursorclass=pymysql.cursors.DictCursor )
    connection.begin()
    cursor=connection.cursor()
    cursor.execute(querystr)
    result=encode(cursor.fetchall())
    connection.commit()
    cursor.close()
    connection.close()
    if return_json:
        return jsonify(result)
    else:
        return result


def encode(data):
    for row in data:
        for key,value in row.items():
            if isinstance(value, Decimal):
                row[key]=str(value)
    return data
