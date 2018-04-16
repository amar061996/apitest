# API Details

## Stage 1

**Add new Location to database**

- Method: POST
- Url: /post_location
- Content-Type: application/json
- Paramaters: 
    1. latitude
    2. longitude
    3. pincode
    4. address
    5. city

## Stage 2

### Get using Postgres

**To get the pincode within 5km around a given coordinates(lat/lng)**

- Method: GET
- Url: /get_using_postgres
- Content-Type: application/json
- Paramaters: 
    1. latitude
    2. longitude
    3. radius(in kms)

### Get using Self

**To get the pincode in the given radius around a given coordinates(lat/lng) using the self calculated radius.**

- Method: GET
- Url: /get_using_self
- Content-Type: application/json
- Paramaters: 
    1. latitude
    2. longitude
    3. radius(in kms)

## Stage 3

**To get the place in which the given coordinates(lat/lng) lies in.**

- Method: GET
- Url: /get_geo_location
- Content-Type: application/json
- Paramaters: 
    1. latitude
    2. longitude
   