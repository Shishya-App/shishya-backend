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
--data-raw '{
    "email": "202051214@iiitvadodara.ac.in",
    "password": "demopass",
    "username": "mugdha2"
}'
```

2. Login user: https://shishya-backend-user.herokuapp.com/login/
```
--data-raw '{
    "password": "demopass",
    "username": "mugdha2"
}'
```

3. Get API personal details of user: https://shishya-backend-user.herokuapp.com/adminpanel/personal-details/
Access token required to pass in bearer token
![image](https://user-images.githubusercontent.com/85048574/183628885-f5401eae-4e3a-44dc-9214-fdb799b2bc06.png)

4. Get API, get documents of an user: https://shishya-backend-user.herokuapp.com/adminpanel/document/1
Access token required to pass in bearer token
![image](https://user-images.githubusercontent.com/85048574/183629085-73c50b38-adae-4d31-81a1-651255904abf.png)

