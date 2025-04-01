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

                          User Authentication
1. Create a User
   Method: POST
   URL: http://127.0.0.1:8000/api/users/register/
   Body (JSON, raw):

   {
    "email": "testuser@example.com",
    "username": "testuser",
    "password": "testpassword"
}
   Expected Response:

   201 Created with user details.



2. Log in to Get Token
   Method: POST
   URL: http://127.0.0.1:8000/api/users/login/
   Body (JSON, raw):

   {
    "email": "testuser@example.com",
    "password": "testpassword"
}

Expected Response:

200 OK with access and refresh tokens.

Copy the access token for authentication in the next requests.


                   Movies Endpoints

4.  Create a Movie
    Method: POST
     URL: http://127.0.0.1:8000/api/movies/
     Headers:

    Authorization: Bearer <access_token>
    Body (JSON, raw):

{
    "title": "Mission: Impossible – Dead Reckoning Part Two",
    "description": "An action thriller movie.",
    "release_date": "2025-05-10"
}

Expected Response:

201 Created with movie details.


5. View All Movies
   Method: GET
   URL: http://127.0.0.1:8000/api/movies/

   Expected Response:

   200 OK with a list of movies.



6. Update a Movie
   Method: PUT
   URL: http://127.0.0.1:8000/api/movies/{movie_id}/
   (Replace {movie_id} with the actual movie ID.)
   Headers:

   Authorization: Bearer <access_token>
   Body (JSON, raw):

{
    "title": "Mission: Impossible – Dead Reckoning Part Two (Updated)",
    "description": "Updated description.",
    "release_date": "2025-05-10"
}

   Expected Response:

   200 OK with updated movie details.


7. Delete a Movie
   Method: DELETE
   URL: http://127.0.0.1:8000/api/movies/{movie_id}/
   
   Headers:

   Authorization: Bearer <your_access_token>
   
   Expected Response:

204 No Content (Movie deleted).


            Reviews Endpoints
8. Create a Review for a Movie
   Method: POST
   URL: http://127.0.0.1:8000/api/reviews/
   
   Headers:

   Authorization: Bearer <your_access_token>
   Body (JSON, raw):

{
    "movie": 4, 
    "content": "An amazing action thriller!",
    "rating": 5
}

(Note: movie should be the ID of the movie you're reviewing.)
Expected Response:

201 Created with review details.

9. View All Reviews
   Method: GET
   URL: http://127.0.0.1:8000/api/reviews/
   Expected Response:

   200 OK with a list of reviews.


10. Update a Review
    Method: PUT
    URL: http://127.0.0.1:8000/api/reviews/{review_id}/
    (Replace {review_id} with the actual review ID.)
    
    Headers:

    Authorization: Bearer <your_access_token>
    Body (JSON, raw):

    {
    "movie": 4,
    "content": "Updated review: Absolutely thrilling!",
    "rating": 4
}

Expected Response:

200 OK with updated review details.


11. Delete a Review
    Method: DELETE
    URL: http://127.0.0.1:8000/api/reviews/{review_id}/
    
    Headers:

    Authorization: Bearer <your_access_token>
    Expected Response:

    204 No Content (Review deleted).




the above are endpoints of my project. 
