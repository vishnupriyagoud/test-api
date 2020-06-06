from flask_restful import Resource, reqparse
from db import query 

class Emp(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('empno',type=int , required=True, help= "cant leave blank")
        data=parser.parse_args()
        print(data)
        try:
            return query(f"""SELECT * FROM testapi.emp WHERE empno={data['empno']};""")
        except:
            return {"message":"error connecting table"},500

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('empno',type=int , required=True, help= "cant leave blank")
        parser.add_argument('ename',type=str , required=True, help= "cant leave blank")
        parser.add_argument('job',type=str, required=True, help= "cant leave blank")
        parser.add_argument('mgr',type=int , required=True, help= "cant leave blank")
        parser.add_argument('hiredate',type=str , required=True, help= "cant leave blank")
        parser.add_argument('sal',type=str , required=True, help= "cant leave blank")
        parser.add_argument('comm',type=str )
        parser.add_argument('deptno',type=int , required=True, help= "cant leave blank")
        parser.add_argument('pass',type=str , required=True, help= "cant leave blank")

        data=parser.parse_args()
        try:
            x = query(f"""SELECT * FROM testapi.emp WHERE empno={data['empno']};""", return_json=False)
            if len(x)>0:
                return { "message":"empno already exists"}
        except:
            return {"message":"error inserting into table"},500

        if data['comm']!=None:
            try:
                query(f"""INSERT INTO testapi.emp values({data['empno']},
                                                        '{data['ename']}',
                                                        '{data['job']}',
                                                        {data['mgr']},
                                                        '{data['hiredate']}',
                                                        '{data['sal']}',
                                                        '{data['comm']}',
                                                        {data['deptno']},
                                                        '{data['pass']}');""")
            except:
                return {"message":"error inserting into table"},500
            return {"message":"Success"},201      
        else:
            try:
                query(f"""INSERT INTO testapi.emp (empno, ename, job, mgr, hiredate, sal, deptno, pass)
                                                    values({data['empno']},
                                                        '{data['ename']}',
                                                        '{data['job']}',
                                                        {data['mgr']},
                                                        '{data['hiredate']}',
                                                        '{data['sal']}',
                                                        {data['deptno']},
                                                        '{data['pass']}');""")
            except:
                return {"message":"error inserting into table"},500
            return {"message":"Success"},201 