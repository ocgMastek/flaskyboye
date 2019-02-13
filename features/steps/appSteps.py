import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("request for all patients with API")
def fetch_patients_from_API(context):
    context.patients = requests.get("").json() #insert api get request