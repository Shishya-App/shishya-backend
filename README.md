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
| - | - | Registers new users (User side) |

```
curl --location --request POST 'https://shishya-backend-user.herokuapp.com/register/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=62KjlMixjCOIaieXB4eUNjQidMxmzhsxHmcrjhXZpaPlzMvZb4EhCqdOQNg5t8wx' \
--data-raw '{
    "email": "mugdha2@iiitvadodara.ac.in",
    "password": "********",
    "username": "mugdha2",
    "first_name": "Mugdha",
    "last_name" : "Sharma",
    "adhaar_no": "<a string of length 12, integers>"
}'
```
As per the problem statement,after registration the user gets OTP at linked phone number with Adhaar card. Twilio free version was used for this purpose.As of now, register only works on some adhaar number because of limited database (if used on heroku url). For local trials, go to django admin and add adhaar number with phone number at DB before registration.

![image](https://user-images.githubusercontent.com/85048574/187081109-9851027a-2b49-47cd-99bc-2897acc32112.png)

Then use the same adhaar to get OTP at registered mobile number.

2.
```http
https://shishya-backend-user.herokuapp.com/verify-otp/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| id | Integer | User ID (provided by django)|
| OTP | string | string of length 12 characters made of integers|

```
{
    "id": 17,
    "OTP" : "****************"
}

```
3.

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
sample output of a user
```
{
    "username": "mugdha4",
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3ODY4Mzk1OCwiaWF0IjoxNjYxNDAzOTU4LCJqdGkiOiJlZjY4Y2YxYmNiNDI0ZWEwOWYwOThmNjBiYmUyOTIyYyIsInVzZXJfaWQiOjR9.DX9IIWP2j6fR6H2fkbicS56kwAuztZm0-HiX6mY2Y7U",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4NjgzOTU4LCJpYXQiOjE2NjE0MDM5NTgsImp0aSI6Ijg1MzAyYTE0OWI2OTRmNDI4ODQ2MTNlMWIxNzkzMDY5IiwidXNlcl9pZCI6NH0.CPKuozrnFPdApmbTHoTjT2C38lu6FLQp2a3SjWAVGmU"
    },
    "first_name": "Mugdha",
    "last_name": "Sharma"
}

```

4. 

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

5. 
```http
https://shishya-backend-user.herokuapp.com/adminpanel/document/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` | Get API, get documents of an user|


Curl Request

```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/document/'
```
![image](https://user-images.githubusercontent.com/85048574/183633206-520758e4-18a8-4d70-b7f5-3240e61a8762.png)

6.

```http
https://shishya-backend-user.herokuapp.com/adminpanel/all-questions/${form_id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `form_id` | `int` | View questions of a particular Form|


```
curl --location --request GET 'https://shishya-backend-user.herokuapp.com/adminpanel/questions/1' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTMxNjM5LCJpYXQiOjE2NjA2NTE2MzksImp0aSI6Ijk3OGIwZmE1YmVjMzQ5NjNhMTVjNGU3ZGRhNjQyMGJiIiwidXNlcl9pZCI6Mn0.WpnaBg8LL_dfXvLD38OFKEQBPyc6X05rgneGHbvbBFU'

```
Sample output

```
{
    "text_questions": [],
    "file_questions": [
        {
            "id": 1,
            "form": 1,
            "title": "Adhaar",
            "answer": [],
            "technique": "file_upload"
        }
    ],
    "MCQ_questions": [],
    "pre_verified": [
        {
            "id": 2,
            "form": 1,
            "title": "BirthCertificate",
            "answer": [],
            "technique": "pre_verified"
        },
        {
            "id": 3,
            "form": 1,
            "title": "HSC",
            "answer": [],
            "technique": "pre_verified"
        }
    ]
}

```


7. 

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
curl --location --request POST 'http://127.0.0.1:8000/adminpanel/form/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTI2OTE1LCJpYXQiOjE2NjA2NDY5MTUsImp0aSI6ImJhMTgxYjhkYzllYTRhZTY4OGY4NjM0NzQxM2JiYjRhIiwidXNlcl9pZCI6Mn0.F8AeaijHfPtHZV6oqgZQiulpgN5SyczQYRBFPi78nhI' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=62KjlMixjCOIaieXB4eUNjQidMxmzhsxHmcrjhXZpaPlzMvZb4EhCqdOQNg5t8wx' \
--data-raw '{
    "title": "Form3",
    "owner": 35,
    "deadline": "2022-08-26",
    "description": "sample description",
    "academic_year": 2020
}'
```
![image](https://user-images.githubusercontent.com/85048574/185063622-9df4e294-8b8d-4be2-a684-498663515ede.png)

```
8. 

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

9. 

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

10. 

```http
https://shishya-backend-user.herokuapp.com/userpanel/recent-upload/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` |Get recent 5 documents from the profile|



11.

```http
https://shishya-backend-user.herokuapp.com/adminpanel/bool-docs/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `String` |Check which pre-verified documents are already uploaded for user|

Sample Output:

```

{
    "SSC": false,
    "HSC": false,
    "AdhaarFile": false,
    "MigrationCertificate": false,
    "JEEmarksheet": false,
    "JEEallotmentLetter": false,
    "DisabilityCertificate": false,
    "DomicileCertificate": false,
    "PAN": false,
    "BirthCertificate": true,
    "SportsCertificate": false,
    "TransferCertificate": false,
    "CasteCertificate": false,
    "Passport": false,
    "IncomeCertificate": false,
    "MedicalCertificate": false,
    "NationalityCertificate": false
}

```

12. Get all Questions of a form

```http
http://127.0.0.1:8000/adminpanel/questions/1
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `pk` | `String` |Check which pre-verified documents are already uploaded for user|

Sample Output:

```
{
    "text_questions": [],
    "file_questions": [
        {
            "id": 1,
            "form": 1,
            "title": "Adhaar",
            "answer": [],
            "technique": "file_upload"
        }
    ],
    "MCQ_questions": [],
    "pre_verified": [
        {
            "id": 2,
            "form": 1,
            "title": "BirthCertificate",
            "answer": [],
            "technique": "pre_verified"
        },
        {
            "id": 3,
            "form": 1,
            "title": "HSC",
            "answer": [],
            "technique": "pre_verified"
        }
    ]
}

```

13. Get all Responses of a form

Post: https://shishya-backend-user.herokuapp.com/adminpanel/view-responses/

```
{
"form":1
}
```

Sample Output:

```
{
    "Custom_Upload": [
        {
            "id": 1,
            "answer": "/media/docs/riya_--blr_to_abad_dxBRQeg.pdf",
            "form": 1,
            "user": 1,
            "question": 1
        },
        {
            "id": 2,
            "answer": "/media/docs/riya_--blr_to_abad_nKqR3sV.pdf",
            "form": 1,
            "user": 4,
            "question": 1
        },
        {
            "id": 3,
            "answer": "/media/docs/riya_--blr_to_abad_LVgs4za.pdf",
            "form": 1,
            "user": 1,
            "question": 1
        }
    ],
    "Pre Verified": [
        {
            "id": 1,
            "title": "HSC",
            "form": 1,
            "question": 3,
            "file_id": 1,
            "user": 4
        }
    ]
}

```