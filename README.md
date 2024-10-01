# FINTRACK API.  
A simple API to fastrack users expenditure.  


![fintrack logo](https://i.imgur.com/I3m75vU.png)  



## SETUP  

```
$ pip3 install -r requirements.txt  
```

## RUN  

```
$ API_HOST=0.0.0.0 API_PORT=5000 python app.py  
```

## ROUTES  

- `POST /api/v1/signup`: creates a new user with specified params(email, password, username, name).  
- `POST /api/v1/expense/add`: adds a user expenditure.  
- `DELETE /api/v1/expense/remove/int:expense_id>`: deletes an expenditure.
- `GET /api/v1/expense/get_expenses/<int:user_id>`: returns all expenses.
- `PUT /api/v1/expense/update/<int:expense_id>`: updates an expenditure.
- `PUT /api/v1/reset_password:<int>`: resets user password(params: {email, newpassword})
