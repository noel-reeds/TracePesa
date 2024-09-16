# FINTRACK API.  
A simple API to fastrack users expenditure.  


![fintrack logo](https://i.imgur.com/I3m75vU.png)  



## SETUP  

```
$ pip3 install -r requirements.txt  
```

## RUN  

```
$ API_HOST=0.0.0.0 API_PORT=5000 flask run  
```

## ROUTES  

- `POST /api/signup`: creates a new user with specified params.  
- `POST /api/expense/add`: adds a user expenditure.  
