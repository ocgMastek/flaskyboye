import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("request for all Reports")
def fetch_Reports_from_Browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/lab-manager")
    context.countText = context.driver.find_element_by_id("report-count").text
    print(context.countText)
    
@then("have all Reports from Browser available from the application")
def check_Reports_fetched_from_Browser(context):
    ok_(len(context.countText)>0, "Employee Count Found")

@given("post request with Report details with Browser")
def post_Report_from_Browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/lab-manager")
    context.count_text = context.driver.find_element_by_id("report-count").text
    context.driver.get("http://localhost:5000/patient/report")
    for row in context.table:
        context.driver.find_element_by_id("patient_id").send_keys(row["patient_id"])
        context.driver.find_element_by_id("report_text").send_keys(row["report_text"])
        context.driver.find_element_by_id("add-report").click()
    context.driver.get("http://localhost:5000/lab-manager")
    context.count_text_after_add = context.driver.find_element_by_id("report-count").text


@then("Report from Browser count will increase")
def check_count_increase(context):
    ok_(not (context.count_text == context.count_text_after_add), "Count not Changed")

@given("delete request with Report id with Browser")
def delete_Report_with_Browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/lab-manager")
    context.count_text = context.driver.find_element_by_id("report-count").text
    for row in context.table:
        context.driver.find_element_by_id("delete-report-"+row['report_id']).click()
    context.driver.get("http://localhost:5000/lab-manager")
    context.count_text_after_delete = context.driver.find_element_by_id("report-count").text

@then("Report from Browser count will decrease by 1")
def check_count_decrease(context):
   ok_(not (context.count_text == context.count_text_after_delete), "Count not Changed") 













