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

5.  Get request to get all questions of a form: https://shishya-backend-user.herokuapp.com/adminpanel/questions/1
Formally: https://shishya-backend-user.herokuapp.com/adminpanel/questions/<form_id>
```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/questions/1' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU'

```
![image](https://user-images.githubusercontent.com/85048574/185064105-242efe11-267d-44fa-8a93-21b73f2a9f96.png)


6.   https://shishya-backend-user.herokuapp.com/adminpanel/form/1
Formally: https://shishya-backend-user.herokuapp.com/adminpanel/form/<form_id>

```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/form/1' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU'

```
![image](https://user-images.githubusercontent.com/85048574/185063748-544e2da5-daaf-4b2d-8b17-c30d4cfa3c8e.png)

7. Post Request to **create forms**: https://shishya-backend-user.herokuapp.com/adminpanel/form/
```
curl --location --request POST 'https://shishya-backend-user.herokuapp.com/adminpanel/form/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Form2",
    "owner": 2
}'
```
![image](https://user-images.githubusercontent.com/85048574/185063622-9df4e294-8b8d-4be2-a684-498663515ede.png)

8. Add Question in existing form: https://shishya-backend-user.herokuapp.com/adminpanel/questions/

```
curl --location --request POST 'https://shishya-backend-user.herokuapp.com/adminpanel/questions/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU' \
--header 'Content-Type: application/json' \
--data-raw '{
    "form": 1,
    "title": "F2",
    "technique": "file_upload"
}'

```