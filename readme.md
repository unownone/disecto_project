# Disecto Project

### Invoice Generation

## [Heroku](https://disecto-inv.herokuapp.com/)

# Routes

- `api/token/` - Get API Token
  - Request TYPE : `POST`
  - Request Body : `{ "email": "email", "password": "password" }`
  - Response : Access and refresh Token
- `api/token/refresh/` - Refresh Token

  - Request TYPE : `POST`
  - Request Body : `{ "refresh_token": "refresh_token" }`
  - Response : Get Refreshed Access Token

- `api/user` : User fetching,creation,deleting, updating

  - Request TYPE : `GET`
  - Response : User Object
  - Request TYPE: `POST`
  - Request Body :

                {
                    "full_name":<fullname>,
                    "email":<email>,
                    "password":<password>,
                    "phone":<phone>,
                    "address":<address>
                }

  - Response : User Object created
  - Request TYPE: `PUT`
  - Request Body :

                {
                    "full_name":<fullname>,[optional]
                    "email":<email>,[optional]
                    "phone":<phone>,[optional]
                    "address":<address>[optional]
                }

  - Request TYPE: `DELETE` # Delete the user

- `api/admin/` - Django Admin Panel
- `api/items/` - List of items
  - Request TYPE : `GET`
  - Params : `None`
  - Response : Returns paginated list of items
- `api/purchase/` : Purchase an item

  - Request TYPE : `GET`
  - Params : `None`
  - Response : returns a list of all purchases

  - Request TYPE : `POST`
  - Params : `item_id`
  - Response : Returns a new purchase object with it's ID

- `api/purchase/<pk>/` - Update Delete Get invoice

  pk is the primary key of the Purchase

  - Request TYPE : `GET`
  - Params : `None`
  - Response : Returns an invoice
  - Request TYPE : `PUT`
  - Params : `None`
  - Body : `{"is_placed":True}`
  - Response : Returns an updated invoice
  - Request TYPE : `DELETE`
  - Params : `None`
  - Response : Returns a 204

- `api/add-items/<pk>/` - Add items / Get items
  - Request TYPE : `GET`
  - Params : `None`
  - Response : Returns a list of items purchased under 1 purchase
  - Request TYPE : `POST`
  - Params : `None`
  - Body : `{"item":<item id>, "count":<count of items>}`
  - Response : Item created
