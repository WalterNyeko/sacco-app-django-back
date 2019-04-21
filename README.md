# Sacco Application
This is a sacco api for VasTech

The following are the different endpoints that shall be available for consumption in this repository

| Endpoint                   | Description                                           |
| -------------------------- | ----------------------------------------------------- |
| `/api/v1/users/register`   | This is a user registration endpoint                  |
| `/api/v1/users/login`      | This is a user login enpoint                          |
| `/api/v1/users/logout`     | This is a user logout endpoint                        |
| `/api/v1/users/:id/edit`   | This is an endpoint for editing users details         |
| `/api/v1/users/:id/upload` | This is an endpoint that allows profilepicture upload |
| `/api/v1/users/:id/delete` | This is an endpoint that allows deleting a user       |

## The data consumed by each endpoint and the responses are as below;

1.  `/api/v1/users/register`: Registration/User Signup Endpoint

(a). Consumed

```
{
  "username": "some username",
  "first_name": "some first name",
  "last_name": "some last name",
  "email": "some email",
  "password": "some password",
  "created_at": "some date",
  "is_active": "true/false---default is false until email is verified",
  "image": "user image"
}
```

(b). Response

```
{
  "message": "some success/error message",
}
```

2.  `/api/v1/users/login`: Login Endpoint

(a). Consumed

```
{
    "username/email": "username or email is accepted",
    "password": "the password"
}
```

(b). Response

```
{
    "username": "username",
    "email": "email",
    "token": "access token"
}
```

3.  `/api/v1/users/logout`: Logout Endpoint

```
{
    "username/email": "username or email is accepted",
}
```

(b). Response

```
{
    "message": "successfully logged out",
    "token": ""
}
```

4.  `/api/v1/users/:id/edit`: Edit Users Profile Endpoint

(a). Consumed

```
{
  "username": "some username",
  "first_name": "some first name",
  "last_name": "some last name",
  "email": "some email",
  "password": "some password",
  "created_at": "some date",
  "is_active": "true/false---default is false until email is verified",
  "image": "user image"
}
```

(b). Response

```
{
  "message": "some success/error message",
}
```

5.  `/api/v1/users/:id/upload`: Upload Profile Picture Endpoint

(a). Consumed

```
{
  "username/email": "username/email",
  "image": "user image"
}
```

(b). Response

```
{
  "message": "some success/error message",
}
```

6.  `/api/v1/users/:id/delete`: Delete User Endpoint

(a). Consumed

```
{
  "username/email": "username/email",
}
```

(b). Response

```
{
  "message": "some success/error message",
}
```
