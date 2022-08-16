# shishyaBackend-user

## Development 🔧

## Setup

```
git clone https://github.com/Shishya-App/shishyaBackend-user.git
```

### For setting virtual environment

```sh
virtualenv venv
```

### For activating virtual environment in Windows

```sh
venv/Scripts/activate
```

### For activating virtual environment in Linux and macOS

```sh
source venv/bin/activate
```

### For deactivating virtual environment
```sh
deactivate
```
After creating virtual environment

### Start

```sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## APIs in use

1. Register user: https://shishya-backend-user.herokuapp.com/register/
```
curl --location --request POST 'https://shishya-backend-user.herokuapp.com/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "202051214@iiitvadodara.ac.in",
    "password": "demopass",
    "username": "mugdha1"
}'
```

2. Login user: https://shishya-backend-user.herokuapp.com/login/
```
curl --location --request POST 'https://shishya-backend-user.herokuapp.com/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "demopass",
    "username": "mugdha1"
}'
```

3. Get API personal details of user: https://shishya-backend-user.herokuapp.com/adminpanel/personal-details/
Access token required to pass in bearer token

Curl Request:
```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/personal-details/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MzIyNTA4LCJpYXQiOjE2NjAwNDI1MDgsImp0aSI6IjRjZDg3ZDFmODFmYjQ1YmFhOGUxM2M4OTBmMzA5MDUyIiwidXNlcl9pZCI6Mn0.CNaBL33gdotywmoFak0AaCJDKUlLnj0a3m6SPbzWxrU'
```


![image](https://user-images.githubusercontent.com/85048574/183633002-613816e1-e033-4dea-a2a3-0c498fd998b9.png)

4. Get API, get documents of an user: https://shishya-backend-user.herokuapp.com/adminpanel/document/1
Access token required to pass in bearer token
Curl Request

```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/document/1'
```
![image](https://user-images.githubusercontent.com/85048574/183633206-520758e4-18a8-4d70-b7f5-3240e61a8762.png)

5.  https://shishya-backend-user.herokuapp.com/adminpanel/questions/Form1
```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/questions/Form1' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU'

```

6.  https://shishya-backend-user.herokuapp.com/adminpanel/questions/Form1

```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/questions/Form1' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU'

```
