import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("request for all patients")
def fetch_patients_from_Browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/lab-manager")
    context.countText = context.driver.find_element_by_id("count").text
    print(context.countText)
    
@then("have all patients from Browser available from the application")
def check_patients_fetched_from_Browser(context):
    ok_(len(context.countText)>0, "Employee Count Found")

@given("post request with patient details with Browser")
def post_patient_from_Browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/lab-manager")
    context.count_text = context.driver.find_element_by_id("count").text
    context.driver.get("http://localhost:5000/patient")
    for row in context.table:
        context.driver.find_element_by_id("name").send_keys(row["name"])
        context.driver.find_element_by_id("age").send_keys(int(row["age"]))
        context.driver.find_element_by_id("area").send_keys(row["area"])
        context.driver.find_element_by_xpath("//input[@value='"+row["gender"]+"']").click()
        context.driver.find_element_by_id("dob").send_keys(row["dob"])
        context.driver.find_element_by_id("add-patient").click()
    context.driver.get("http://localhost:5000/lab-manager")
    context.count_text_after_add = context.driver.find_element_by_id("count").text


@then("patient from Browser count will increase")
def check_count_increase(context):
    ok_(not (context.count_text == context.count_text_after_add), "Count not Changed")

@given("delete request with patient id with Browser")
def delete_patient_with_Browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/lab-manager")
    context.count_text = context.driver.find_element_by_id("count").text
    for row in context.table:
        context.driver.find_element_by_id("delete-patient-"+row['patient_id']).click()
    context.driver.get("http://localhost:5000/lab-manager")
    context.count_after_delete = context.driver.find_element_by_id("count").text

@then("patient from Browser count will decrease by 1")
def check_count_decrease(context):
   ok_(not (context.count_text == context.count_after_delete), "Count not Changed")














