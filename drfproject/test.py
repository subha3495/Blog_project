import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
# def get_resources(id=None):
#     data ={}
#     if id is not None:
#         data ={'id':id}
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resources()

def post_resources():
    new_emp ={ 'eid':4,'ename':'supi','esal':60000,'eadd':'bp'}
    
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
post_resources()


# def update_resource(id):
#     new_emp ={'id':id,'ename':'SUNNY123','esal':5548}
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(3)

# def delete_resource(id):
#     new_emp ={'id':id}
#     resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(6)