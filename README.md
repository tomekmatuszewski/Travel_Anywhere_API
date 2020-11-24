#### Travel Anywhere API

REST API for travel company -> Django + Django Rest Framework

- user registration
    - http://localhost:8000/api/register
    
- user authentication (token authentication)
    - http://localhost:8000/api/login
    
- update, delete, get user profile:
    - http://localhost:8000/api/user-profile
    
- change user password:
    - http://localhost:8000/api/change-password
    
- get/update/post/delete -> trips/hotels/airport/city/country

    - http://localhost:8000/api/airports
    - http://localhost:8000/api/hotels
    - http://localhost:8000/api/trips
    - http://localhost:8000/api/cities
    - http://localhost:8000/api/countries

- get airport / hotel for particular trips

    - http://localhost:8000/api/trips/<int:pk>/hotel
    - http://localhost:8000/api/trips/<int:pk>/airport-dest  -> (destination airport)
    - http://localhost:8000/api/trips/<int:pk>/airport-dep   ->  (departure airport)


