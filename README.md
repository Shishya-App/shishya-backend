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

1.
```http
https://shishya-backend-user.herokuapp.com/register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | Registers new users (working both admin and user side) |

```
curl --location --request POST 'https://shishya-backend-user.herokuapp.com/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "202051214@iiitvadodara.ac.in",
    "password": "demopass",
    "username": "mugdha1"
}'
```

2.

```http
https://shishya-backend-user.herokuapp.com/login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | Login user (working both admin and user side) |

 
```
curl --location --request POST 'https://shishya-backend-user.herokuapp.com/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "demopass",
    "username": "mugdha1"
}'
```

3. 

```http
https://shishya-backend-user.herokuapp.com/adminpanel/personal-details/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` | Get API personal details of user|

```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/personal-details/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU'
```


![image](https://user-images.githubusercontent.com/85048574/183633002-613816e1-e033-4dea-a2a3-0c498fd998b9.png)

4. 
```http
https://shishya-backend-user.herokuapp.com/adminpanel/document/1
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` | Get API, get documents of an user|


Curl Request

```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/document/1'
```
![image](https://user-images.githubusercontent.com/85048574/183633206-520758e4-18a8-4d70-b7f5-3240e61a8762.png)

5.

```http
https://shishya-backend-user.herokuapp.com/adminpanel/questions/
https://shishya-backend-user.herokuapp.com/adminpanel/questions/${form_id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` | View all questions from all forms|
| `id` | `int` | View questions of a particular Form|


```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/questions/1' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU'

```
![image](https://user-images.githubusercontent.com/85048574/185064105-242efe11-267d-44fa-8a93-21b73f2a9f96.png)


6. 

```http
https://shishya-backend-user.herokuapp.com/adminpanel/form/
https://shishya-backend-user.herokuapp.com/adminpanel/form/${form_id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` | View all Forms|
| `id` | `int` | View form from form.id|

```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/form/1' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU'

```
![image](https://user-images.githubusercontent.com/85048574/185063748-544e2da5-daaf-4b2d-8b17-c30d4cfa3c8e.png)

7.
```http
https://shishya-backend-user.herokuapp.com/adminpanel/form/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` | Create new Form|

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

8. (In-progress, don't use)
```http
https://shishya-backend-user.herokuapp.com/adminpanel/questions/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` |Add question in an existing form|

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

9. 

```http
https://shishya-backend-user.herokuapp.com/userpanel/profile-documents/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` |Retrieve NAD+Custom uploaded documents in profile section|

```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/userpanel/profile-documents/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4MzQwODgwLCJpYXQiOjE2NjEwNjA4ODAsImp0aSI6IjRlOWYzZTZkZjE3NjRlMDI4M2M5ZGJmNmEwN2YxZWZjIiwidXNlcl9pZCI6Mn0.-X4_PHZ2XOBo_oTkOugPa-h9dRdrlmrZDHj-tXUVAps'

```
sample output
```
{
    "user": 2,
    "NAD_Document": [
        {
            "id": 1,
            "user": 2,
            "SSC": 1,
            "HSC": 1,
            "MigrationCertificate": 1,
            "JEEmarksheet": 1,
            "JEEallotmentLetter": 1,
            "DisabilityCertificate": 1,
            "DomicileCertificate": 1,
            "PAN": 1,
            "BirthCertificate": 1,
            "SportsCertificate": 1,
            "TransferCertificate": 1,
            "CasteCertificate": 1,
            "Passport": 1,
            "IncomeCertificate": 1,
            "MedicalCertificate": 1,
            "NationalityCertificate": 1
        }
    ],
    "Custom_Document": []
}
```
"Custom_Document": [] , JSON in this will get auto appended whenever user uploads the document

10. 

```http
https://shishya-backend-user.herokuapp.com/userpanel/custom-document/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` |Upload custom documents in profile section|

How to use?
```
{
    "File": <upload from PC>, (required)
    "PagesNo": <enter/retreive>, (required)
    "Title": "Sample Title", (required)
    "isVerified": false, (default)
    "user": <This is auto fill field, which is handled by backend>
}
```