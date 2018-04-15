import flask
import psycopg2

from flask import Flask,request,render_template,make_response,jsonify

app = Flask(__name__)
#stage 1 solution

@app.route('/try', methods=['GET','POST'])
def get_data():

    data=request.json['title']
    print(data)

@app.route('/post_location', methods=['GET','POST'])

def related():
    
    try: 	
        lat = request.json['latitude']	
        lng = request.json['longitude']
        pincode = request.json['pincode']
        address = request.json['address']
        city = request.json['city']
        print(lat,lng,pincode,address,city)
        conn = psycopg2.connect(dbname="postgres", user = "postgres", password = "password", host = "127.0.0.1", port = "5432")
        cur = conn.cursor() 

        #check if points having lat,lang withing 1km exists or same pincode exists

        cur.execute("SELECT apitest.key, apitest.latitude, apitest.longitude, earth_distance(ll_to_earth("+lat+","+lng+"), ll_to_earth(apitest.latitude, apitest.longitude)) as distance FROM apitest WHERE key='IN/"+pincode+"' OR earth_distance(ll_to_earth("+lat+","+lng+"), ll_to_earth(apitest.latitude, apitest.longitude)) <1000;")
        fetch = cur.fetchone()
        result = ""
        pin = 'IN/'+pincode
        if cur.rowcount>0:	
            result = "Entry alerady exists in database"
            print("Entry already exists in database or lat and lng nearly equal to some intial data")
        else:
            cur.execute("INSERT INTO apitest (key, place_name, admin_name1, latitude, longitude, accuracy) VALUES ('"+pin+"','"+address+"','"+city+"',"+lat+","+lng+",'')");
            result = "Data added to database"
        
        
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'task': result}),201
    except Exception as e:
        print(e)
        return jsonify({'error':'error'})


if __name__ == '__main__':

    app.run(debug=True,port=5000)