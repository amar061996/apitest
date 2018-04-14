import psycopg2

conn = psycopg2.connect(dbname="postgres", user = "postgres", password = "password", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

cur.execute("""CREATE TABLE apitest (
		key varchar(15) NOT NULL,
		place_name varchar(35) NOT NULL,
		admin_name1 varchar(35) NOT NULL,
		latitude real,
		longitude real,
		accuracy varchar(5));""")



cur.execute("CREATE EXTENSION cube;")

cur.execute("CREATE EXTENSION earthdistance;")

print ("Created table successfully")

conn.commit()
cur.close()

