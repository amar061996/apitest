import requests
import json

from nose.tools import assert_true
import requests

def test_stage1():

    url = 'http://127.0.0.1:5000/post_location'
    header = {"content-type": "application/json"}
    data = {"pincode" : "474015", "latitude" : "26.2488", "longitude" : "78.1791", "address" : "ABV IITM", "city" : "Gwalior",}
    response=requests.post(url,data=json.dumps(data),headers=header)
    assert_true(response.ok)


   
