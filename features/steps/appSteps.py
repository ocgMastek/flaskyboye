import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("request for all patients")
def fetch_patients_from_API(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/lab-manager")
    context.countText = context.driver.find_element_by_id("count").text
    print(context.countText)
    
@then("have all patients from API available from the application")
def check_patients_fetched_from_API(context):
    ok_(len(context.countText)>0, "Employee Count Found")

@given("post request with patient details with API")
def post_patient_from_API(context):
    """context.currentCount = len(requests.get("http://localhost:5000/lab-manager").json()) #DONE insert api to get all patients
    for row in context.table:
        new_patient = requests.post("http://localhost:5000/patient/register", #DONE: insert api to add a patient
                                     data={"patient_id":row["patient_id"],
                                            "name":row["name"],
                                             "age":row["age"],
                                              "area":row["area"]})"""
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


@then("patient from API count will increase")
def check_count_increase(context):
    ok_(not (context.count_text == context.count_text_after_add), "Count not Changed")

@given("delete request with patient id with API")
def delete_patient_with_API(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/lab-manager")
    context.count_text = context.driver.find_element_by_id("count").text
    for row in context.table:
        context.driver.find_element_by_id("delete-patient-"+row['patient_id']).click()

@then("patient from API count will decrease by 1")
def check_count_decrease(context):
   ok_(not (context.count_text == context.driver.find_element_by_id("count").text), "Count not Changed")














