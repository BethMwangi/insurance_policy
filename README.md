# insurance_policy

## 🎯 Task

Develop an API endpoint create a customer and get policy quote based on age range

---

### 📖 Description

* MVC Architecture
* Database has dummy records- dbSqlite used 
* Supports pagination
* Supports Filtration
* Support searching

### 🔧 Authentication and authorization

- Authentication can be handled in two ways, ie,
    - Method 1: Use Django Basic Authentication system to authenticate users by use of email and password fields, these users can either be set as 'admin/superusers/', 'basic system backend users'. In order to access views and handle specific tasks, django default permissions or use of custom permissions can be used.
    - Method 2: When a customer is being created, in order to get quotes and get a list of their quotes, a us of TokenAuthentication, in order to identify the request and determine if it is permitted 

### 🔎 Improvements

- Complete CRUD operation: Mostly delete 
- Testing
- Create Endpoint Documentation

### 🏁 API Usage

Added a [Postman collection](https://elements.getpostman.com/redirect?entityId=1716130-7fde645f-5468-4b91-9e3a-1b1443cdb18f&entityType=collection) to easily use API endpoints and query parameters combinations.
Also contains examples of expected responses.

### Endpoint: /api/v1/users/
#### HTTP Method: GET

Get a list of users (paginated)

**Pagination query parameters:**

- id: Optional. Search users by given id  
- ### Endpoint: /api/v1/users/{id}

**Filtration query parameters:**

- username: Optional. User's username. Filter exact coincidence. Case sensitive.
- lastname: Optional. User's last name. Filter exact coincidence. Case sensitive.
- email: Optional. User's email address. Filter exact coincidence. Case sensitive.
- birth_date: Optional. User's birth_date. Filter exact coincidence.

**Pagination and filtration could be used in same request.**


### Endpoint: /api/v1/users/create_customer/
#### HTTP Method: POST

Create a customer.

Required json body:
  ```json
    {
            "first_name": "Ahmed",
            "username": "ahmed",
            "last_name": "Mohammed",
            "email": "ahmed@gmail.com",
            "mobile_number": "07829182",
            "birth_date": "2003-02-28"
        }
  ```

### Endpoint: /api/v1/policy/

#### HTTP Method: GET
Get a list of policies (paginated)
**Filtration query parameters:**

- name: Optional. policy's name. Filter exact coincidence. Case sensitive.
- status: Optional. Policy's status. 


### Endpoint: /api/v1/policy/quote/

#### HTTP Method: GET
Get a list of all quotes (paginated)

- id: Optional. Search users by given id  
- ### Endpoint: /api/v1/users/{id}

### Endpoint: /api/v1/policy/quote/create_quote/
#### HTTP Method: POST

Create a new quote.

Required json body:
  ```json
    {
    "customer": 2,
    "policy": 2,
    "cover": "10001",
    "paid": false
     }
  ```

### Endpoint: /api/v1/policy/quote/{id}/confirm_quote/
#### HTTP Method: GET

### Endpoint: /api/v1/policy/quote/{id}/pay_quote/
#### HTTP Method: GET


### ✨ Local environment set up

**To be able to get this project to your local machine**
***Using virtualenv***

``` sh
    $  git@github.com:BethMwangi/inventory-beth.git
    $  pip install virtualenv venv
    $ . venv/bin/activate
    $  cd /insurance
    $  pip install -r requirements.txt
```

- Create .env file and 

- Copy .env.example items to .env and set up a secret key



**To test successfully set up visit: http://localhost:8000**

### ☁️ Production environment - TODO

Have a nice coding, Pythonizate!

---
⌨️ with ❤️ by [Beth Mwangi](https://github.com/BethMwangi) 😊