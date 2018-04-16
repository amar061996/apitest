import json
from nose.tools import assert_true
import requests

def test_using_postgres():
    url = 'http://127.0.0.1:5000/get_using_postgres'
    header = {"content-type": "application/json"}
    response=requests.get(url,params={"latitude" : "26.2488", "longitude" : "78.1791","radius":"5"},headers=header)
    print(response.text)
    assert_true(response.ok)

def test_using_self():
    url = 'http://127.0.0.1:5000/get_using_self'
    header = {"content-type": "application/json"}
    response=requests.get(url,params={"latitude" : "26.2488", "longitude" : "78.1791","radius":"5"},headers=header)
    assert_true(response.ok)



