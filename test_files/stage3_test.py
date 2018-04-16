import json
from nose.tools import assert_true
import requests

def test_stage3():

    url = 'http://127.0.0.1:5000/get_geo_location'
    header = {"content-type": "application/json"}
    response=requests.get(url,params={"latitude" : "26.2488", "longitude" : "78.1791"},headers=header)
    assert_true(response.ok)
