import requests

# url ="http://127.0.0.1:8000/api/users_list"
# response=requests.get(url)
# print(response.text)
ip="http://127.0.0.1:8000"

def get_token():
    # Get AUTH TOKEN
    url ="%s/api/auth/"%(ip)  # in python 3 type 
    response=requests.post(url,data={'username':'amity','password':'amity555'})
    return response.json()

def get_data():
    url =f"{ip}/api/users_list/"         ## in format string type
    Token=get_token()
    header={'Authorization':"Token "+(Token)}   ## in direct calling
    response=requests.get(url, headers=header)
    emp_data=response.json()
    for e in emp_data:
        print(e)


def create_new():
    url =f"{ip}/api/users_list/" 
    header={'Authorization':f"Token {get_token()}"} 
    data={
        "name": "AMI",
        "employee_id": "HQ6",
        "ranking": 6.0,
        "age": 55,
    }
    response=requests.post(url, data=data, headers=header)
    print(response.text)


def edit_data(employee_id):
    url =f"{ip}/api/users_list/{employee_id}/" 
    header={'Authorization':f"Token {get_token()}"} 
    data={
        "name": "AMIT YADAV",
        "employee_id": "HQ6",
        "ranking": 66.0,
        "age": 25,
    }
    response=requests.put(url, data=data, headers=header)
    print(response.text,response.status_code)

def delete_data(employee_id):
    url =f"{ip}/api/users_list/{employee_id}/" 
    header={'Authorization':f"Token {get_token()}"}
    response=requests.delete(url, headers=header)
    print(response.text,response.status_code)

for e in range(21):
    if e>5:
        delete_data(e)








# def create_new(count):
#     url =f"{ip}/api/users_list/" 
#     header={'Authorization':f"Token {get_token()}"}  ## in direct calling type
#     print(header)
#     data={
#         "employee_id": f"HQ{count}",
#         "name": "",
#         "ranking": 6.0,
#         "age": 55,
#     }
#     response=requests.post(url, data=data, headers=header)
#     print(response.text)

# for e in range(20):
#     create_new(e)