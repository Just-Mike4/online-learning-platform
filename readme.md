## Endpoints

### Authentication
- **POST /auth/register/instructor** - Register an instructor
- **POST /auth/register/admin** - Register an admin
- **POST /auth/register/student** - Register a student
- **POST /auth/login/instructor** - Login as an instructor
- **POST /auth/login/admin** - Login as an admin
- **POST /auth/login/student** - Login as a student

### Example JSON Requests and Responses

#### Register a Student
**Request:**
```json
{
    "username": "student1",
    "email": "student1@example.com",
    "password": "password123"
}
```

**Response:**
```json
{
    "message": "Student registration successful. You can login now."
}
```

#### Login as a Student
**Request:**
```json
{
    "username": "student1",
    "password": "password123"
}
```

**Response:**
```json
{
    "access": "your_jwt_access_token"
}
```
#### Register an Instructor
**Request:**
```json
{
    "username": "instructor1",
    "email": "instructor1@example.com",
    "password": "password123"
}
```

**Response:**
```json
{
    "message": "Instructor registration successful. You can login now."
}
```

#### Login as an Instructor
**Request:**
```json
{
    "username": "instructor1",
    "password": "password123"
}
```

**Response:**
```json
{
    "access": "your_jwt_access_token"
}
```

#### Register an Admin
**Request:**
```json
{
    "username": "admin1",
    "email": "admin1@example.com",
    "password": "password123"
}
```

**Response:**
```json
{
    "message": "Admin registration successful. You can login now."
}
```

#### Login as an Admin
**Request:**
```json
{
    "username": "admin1",
    "password": "password123"
}
```

**Response:**
```json
{
    "access": "your_jwt_access_token"
}
```