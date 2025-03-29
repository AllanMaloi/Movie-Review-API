# Movie-Review-API
OVERVIEW
The Movie Review API is a RESTful web service built using Django REST Framework (DRF). It allows users to register, log in, add movies, write reviews, rate movies (1-5), and view reviews. The API supports authentication, permissions, filtering, sorting, and pagination to enhance user experience and data retrieval.

FEATURES
User Authentication (Registration & Login with JWT tokens)

Movie Management (Add, Update, Delete, List Movies)

Review Management (CRUD for reviews, rating system from 1 to 5)

Users Management (CRUD. Users can register, retrieve their details, update their details, delete their account)

Permissions (Only authenticated users can create, update, and delete reviews)

Filtering & Sorting (Search movies by title, filter reviews by rating, sort reviews)

Pagination (Handles large datasets efficiently)

TECHNOLOGIES USED
Python (Programming Language)

Django (Web Framework)

Django REST Framework (API Development)

SimpleJWT (Authentication)

SQLite / PostgreSQL (Database)

Postman (API Testing)

SETUP INSTRUCTIONS 
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/AllanMaloi/movie-review-api.git  
cd movie-review-api  
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv  
source venv/bin/activate  # On Windows use: venv\Scripts\activate  
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt  
4. Apply Migrations
bash
Copy
Edit
python manage.py migrate  
5. Run the Server
bash
Copy
Edit
python manage.py runserver 

API ENDPOINTS
"Authentication"
Endpoint	Method	Description
/api/users/register/	POST	Register a new user
/api/users/login/	POST	Login and get access/refresh tokens
"Movies"
Endpoint	Method	Description
/api/movies/	GET	List all movies
/api/movies/	POST	Add a new movie (Auth required)
/api/movies/<id>/	GET	Retrieve a specific movie
/api/movies/<id>/	PUT/PATCH	Update a movie (Auth required)
/api/movies/<id>/	DELETE	Delete a movie (Auth required)
"Reviews"
Endpoint	Method	Description
/api/reviews/	GET	List all reviews
/api/reviews/	POST	Add a review (Auth required)
/api/reviews/<id>/	GET	Retrieve a specific review
/api/reviews/<id>/	PUT/PATCH	Update a review (Only review owner)
/api/reviews/<id>/	DELETE	Delete a review (Only review owner)
/api/reviews/movie/<movie_id>/	GET	Get reviews for a specific movie

TESTING ON POSTMAN 
Open Postman

Set Authorization to Bearer Token and paste the access token

Test endpoints using the provided routes.