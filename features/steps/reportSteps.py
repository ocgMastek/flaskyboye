import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("request for all reports with API")
def fetch_reports_from_API(context):
    context.reports = requests.get("").json() #insert api get all reports
    pass

@then("have all reports from API available from the application")
def check_reports_fetched_from_API(context):
    ok_(len(context.reports)>0, "reports not Available")
    pass

@given("request for report using Id with API")
def fetch_report_by_Id_API(context):
    for row in context.table: 
        context.id_report = requests.get(""+row["report_id"], #insert api to get report by ID
                                           )
    pass

@then("have report from API available from the application")
def check_report_fetched_by_ID_API(context):
    ok_(len(context.id_report)>0, "report not Available")

@given("post request with report details with API")
def post_report_from_API(context):
    context.currentCount = len(requests.get("").json()) #insert api to get all reports
    for row in context.table:
        new_report = requests.post("", #insert api to add a report
                                     data={"report_id":row["report_id"],
                                            "description":row["description"],
                                             "date":row["date"]})

@then("report from API count will increase by 1")
def check_count_increase(context):
    ok_((context.currentCount + 1) == len(requests.get("").json())) #insert api to get all reports
    
@given("update request with new report area with API")
def update_report_from_API(context):
    for row in context.table:
        context.pre_update_report = requests.get(""+row["report_id"] #insert api to get report by ID
                                           )
        context.updated_report = requests.patch(""+row["report_id"], #insert api to patch report
                                                 data={"date":row["date"]})

@then("report from API area before update NOT equal to area after update")
def check_report_updated(context):
    ok_((context.pre_update_report != context.updated_report), "report not Updated")

@given("delete request with report id with API")
def delete_report_with_API(context):
    context.countBeforeDelete = len(requests.get("").json()) #insert api to get all reports
    for row in context.table:
        deleted_report = requests.delete("", #insert api to delete report
                                          data={"report_id":row["report_id"]})

@then("report from API count will decrease by 1")
def check_count_decrease(context):
    ok_((context.countBeforeDelete - 1) == len(requests.get("").json())) #insert api to get all reports














