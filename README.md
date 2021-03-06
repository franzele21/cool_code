# cool_code
code/function that could be used in other project

## sqlite3_functions.py
Simple functions, that can create/connect to a sqlite database, and make queries to it

### create_connection
Create a connection to a sqlite database. If it doesn't exist, it will automatically created.
__Parameters__:
  - _path_: [str] path to / name of the database
  - _check\_same\_thread_: [bool] enable/disable the check_same_thread (default: True) explanation : https://docs.python.org/3/library/sqlite3.html#sqlite3.connect

__Return__: [sqlite3.Connection] connection to the database

__Example__:
It was designed ot be used like this:
```
conn = create_connection(DATABASE_PATH)
```
Don't forget to `conn.close()` after all operations.

### query
Make query to a sqlite database.
__Parameters__:
  - _connection_: [sqlite3.Connection] connection to the database (you can use __create\_connection__ for this)
  - _query\__: [str] query to make, in a form of a SQL query
  
 __Return__: [sqlite3.Cursor] if the query give back a response, it will be returned
 
 __Example__:
 ```
 conn = create_connection(DATABASE_PATH)
 response = query(conn, "SELECT * FROM CarDb WHERE 1;")
 ```
 A `response.fetchall()` can be used to have a list of all element in `response`.

## sql_to_json.py
### db_to_dict
A function, that returns a dict from all data in a sqlite3 database.
__Parameters__: 
  - _db\_path_: [str] path to the database
 
 __Return__: 
  - [bool] return `False` if the database doesn't have any table
  - [dict] if the database has at least one table, all data will be in the form:
```
  {
    "table1": {
      "1": {...},
      "2": {...},
      ...
    },
    ...
  }
```


    
__Requirements__:
  - it needs the _create\_connection_ and the _query_ function
