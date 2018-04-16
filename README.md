# Apitest
RedCarpetUp internship assignment

### API Details
For details on API check [API Documentatiom](api.md)

## Database Structure
Check [Database Documentation](database.md) to know about database structure.

## Prerequisites
- python 2.7
- pip
#### Postgresql extension prerequisites
- cube
- earthdistance

## Instructions
Follow the instructions to run the assignment


### Adding Dependencies
To add the dependencies run the following command
```
pip install requirements.txt
```

### Create Database
In order to create the database **configure the postgresql password** on line 3 in createtable.py and execute
```
python createtable.py
```

### Import CSV Data
To import data from IN.csv go to importcsv.py and configure the path to IN.csv in line 15.**Change the postgresql database password** on line 11 and run
```
python importcsv.py
```

### Import GeoJson Data
To import data from geojson.json file go to importgeojson.py and **configure the postgresql database password** on line 9 and run
```
python importgeojson.py
```

### Run Server
To run the server execute the following in command line
```
python api.py
````

### Run tests
To run the tests go to /test_files and execute the following code
#### Stage 1 Test
```
nosetests --verbosity=2 stage1_test.py
```
#### Stage 2 Test
```
nosetests --verbosity=2 stage2_test.py
```
#### Stage 3 Test
```
nosetests --verbosity=2 stage3_test.py
```
