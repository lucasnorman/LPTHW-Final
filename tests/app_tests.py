from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_Index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp)


def test_SayHello():
    # test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # make sure default values work for the form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Idiot")

    # test that we get expected values
    data = {'name': 'Lucas', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Lucas")

class MyFile:
    def __init__(self, filename, ):
        self.filename = filename
