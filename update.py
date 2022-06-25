import sqlite3
import argparse


def del_func(keys_, table_): 	#sets up sql statement
 temp_key = ""
	
 if(table_[0] == "album"):
    temp_key = " id = '"
    temp_key = temp_key+ keys_[0] + "'"  
    print("row has been deleted.") 
 elif table_[0] == "album_instrument": #where album_id = 'x' AND instrument_id = 'x'
    temp_key = " album_id = '"
    temp_key = temp_key+ keys_[0] + "'" 
    temp_key += " AND instrument_id = '"
    temp_key = temp_key+ keys_[1] + "'"
    print("row has been deleted.")
 elif table_[0] == "instrument":
  temp_key = " id = '"
  temp_key += keys_[0] + "'" 
  print("row has been deleted.")
 elif table_[0] == "musician":
    temp_key = " ssn = '"
    temp_key += keys_[0] + "'" 
    print("row has been deleted.")
 elif table_[0] == "musician_album": #where ssn = 'x' AND album_id = 'x'
    temp_key = "ssn = '"
    temp_key += keys_[0] + "'"
    temp_key += " AND album_id = '"
    temp_key += keys_[1] + "'" 
    print("row has been deleted.")
    
 sql_ = "DELETE FROM " + table_[0]+ " WHERE" + temp_key + ";"
 print(sql_)
 return sql_

def add_func(keys_, table_):		#sets up sql statement
 temp_key = ""
 #Name,id,date,type|| INSERT INTO album VALUES('name','id','date','type');
 for x in keys_:
        temp_key = temp_key+ "'" + x + "',"
 temp_key = temp_key[:-1]
 print("row has been added.")
 
 sql_ = "INSERT INTO " + table_[0]+ " VALUES(" + temp_key + ");"
 print(sql_)
 return sql_
 

db = sqlite3.connect('database.db')	#connect to the database
cur = db.cursor()

ap = argparse.ArgumentParser()
ap.add_argument("--add", action='store_true')
ap.add_argument("--del", action='store_true')
ap.add_argument("--table", type=str, nargs=1)
ap.add_argument("--record", type=str, nargs='+')
args = vars(ap.parse_args())
list_vals = ""
args['record'] = list_vals.join(args['record']).split(",")

#print(args)
if args["del"] == True: 
   sql =""  
   sql = del_func(args["record"], args['table'])
   cur.executescript(sql)	#passing lists and connection to database
   db.commit()
   cur.close()
else:
   sql =""
   sql = add_func(args["record"], args["table"])
   cur.executescript(sql)
   db.commit()
   cur.close()

