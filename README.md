# Shipment API

## P
A simple REST API to maintain a list of shipments.

For this, we used the Python lang. with the Django framework for the basic models and the Django Rest Framework framework for the construction of the API.


## Installation
1. Unzip the file "shipment-list". Or you can clone this repository: `git clone git@github.com:glauber-silva/shipment-list.git`.
2. `cd` into `shipment-list`: `cd shipment-list`.
3. Install [pyenv](https://github.com/yyuu/pyenv#installation).
4. Install [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv#installation).
5. Install Python 3.6.0: `pyenv install 3.6.0`.
6. Create a new virtualenv called "shipment-list": `pyenv virtualenv 3.5.1 shipment-list`.
7. Set the local virtualenv to "shipment-list": `pyenv local shipment-list`.
8. Reload the `pyenv` environment: `pyenv rehash`.

If all went well then your command line prompt should now start with `(shipment-list)`.

If your command line prompt does not start with `(shipment-list)` at this point, try running `pyenv activate shipment-list` or `cd ../shipment-list`. 

If pyenv is still not working, mail to [Glauber](mailto:glauber.lucio.silva@gmail.com) so I can help you out.

## Start application
1. While still in the same directory: `pip install -r requirements.txt` 
2. After all the dependencies installed and the terminal becomes available again: `python manage.py migrate`
3. The database will be initialized. After migrations terminate. We will create a superuser: `python manage.py createsuperuser`

After these steps the application is ready to use. Below there is a basic documentation for use.


## API SPECS

## Backend consideration using with [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)

If the backend is about to run on a different host/port than the frontend, make sure to handle `OPTIONS` too and return correct `Access-Control-Allow-Origin` and `Access-Control-Allow-Headers` (e.g. `Content-Type`).

### Authentication Header

`Authorization: Token jwt.token.here`

## JSON Objects:

Make sure the right content type like `Content-Type: application/json; charset=utf-8` is correctly returned.

### Users (for authentication)
```JSON
{
  "user": {
    "email": "example@example.com",
    "username": "example",
     "token": "jwt.token.here"
    
    }
}
```


### Single Shipment
```JSON
{
    "id": 2,
    "sender": "Sender X",
    "recipient": "Recipient X",
    "carrier": "Carrier X",
    "created_at": "2018-07-31T09:50:05.830074Z",
    "updated_at": "2018-07-31T09:50:05.830155Z",
    "expected_ship_date": "2018-08-03T09:48:55.804346Z",
    "origin": "Node 1",
    "origin_address": "Address Origin",
    "destination": "Node 3",
    "destination_address": "Address destination",
    "total_weight": "333",
    "total_volume": "333"
 }
```

### Multiple Shipments

```JSON
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "sender": "Sender Name Teste",
            "recipient": "Recipient Name",
            "carrier": "Carrier Name",
            "created_at": "2018-07-31T06:35:28.971360Z",
            "updated_at": "2018-07-31T06:35:28.971409Z",
            "expected_ship_date": "2018-08-03T06:32:16.923024Z",
            "origin": "Origin",
            "origin_address": "Address",
            "destination": "Destination",
            "destination_address": "Destination Address",
            "total_weight": "333",
            "total_volume": "333"
        },
        {
            "id": 2,
            "sender": "Sender X",
            "recipient": "Recipient X",
            "carrier": "Carrier X",
            "created_at": "2018-07-31T09:50:05.830074Z",
            "updated_at": "2018-07-31T09:50:05.830155Z",
            "expected_ship_date": "2018-08-03T09:48:55.804346Z",
            "origin": "Node 1",
            "origin_address": "Address Origin",
            "destination": "Node 3",
            "destination_address": "Address destination",
            "total_weight": "333",
            "total_volume": "333"
        }
    ]
}
```

## Endpoints:

### Authentication
`POST /api/users/login`

Example request body:
```JSON
{
  "user":{
    "email": "example@example.example",
    "password": "example"
  }
}
```

No authentication required, returns a [User](#users-for-authentication)

### Registration:

`POST /api/users`

Example request body:
```JSON
{
  "user":{
    "username": "Jacob",
    "email": "jake@jake.jake",
    "password": "jakejake"
  }
}
```

No authentication required, returns a [User](#users-for-authentication)

Required fields: `email`, `username`, `password`



### Get Current User

`GET /api/user`

Authentication required, returns a [User](#users-for-authentication) that's the current user
### Update User

`PUT /api/user`

Example request body:
```JSON
{
  "user":{
    "email": "jake@jake.jake"
  }
}
```
Authentication required, returns the [User](#users-for-authentication)

### List Shipment
`GET /api/shipments`

Returns most recent shipments globally

### Get Shipment

`GET /api/shipments/:id`

No authentication required, will return [single shipment](#single-shipment)

### Create shipment

`POST /api/shipments`

Example request body:

```JSON
{
    "sender": "Sender Name",
    "recipient": "Recipient Teste",
    "carrier": "Carrier Name",
    "origin": "Origin",
    "origin_address": "Address",
    "destination": "Destination",
    "destination_address": "Destination Address",
    "total_weight": "333",
    "total_volume": "333"
}
```

Authentication required, will return an [Shipment](#single-shipment)

Required fields: `All`



### Update Shipment

`PUT /api/shipments/:id`

Example request body:

```JSON
{
    "sender": "Another Sender"
}
```

Authentication required, returns the updated [Shipment](#single-shipment)

### Delete Shipment

`DELETE /api/shipments/:id`

Authentication required