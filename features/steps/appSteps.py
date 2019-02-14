import behave
from pip._vendor import requests
from nose.tools.trivial import ok_

@given("request for all patients with API")
def fetch_patients_from_API(context):
    context.patients = requests.get("localhost:5000/lab-manager").json() #DONE insert api get all patients
    pass

@then("have all patients from API available from the application")
def check_patients_fetched_from_API(context):
    ok_(len(context.patients)>0, "Patients not Available")
    pass

@given("request for patient using Id with API")
def fetch_patient_by_Id_API(context):
    for row in context.table: 
        context.id_patient = requests.get(""+row["patient_id"], #insert api to get patient by ID
                                           )
    pass

@then("have patient from API available from the application")
def check_patient_fetched_by_ID_API(context):
    ok_(len(context.id_patient)>0, "Patient not Available")

@given("post request with patient details with API")
def post_patient_from_API(context):
    context.currentCount = len(requests.get("localhost:5000/lab-manager").json()) #DONE insert api to get all patients
    for row in context.table:
        new_patient = requests.post("localhost:5000/patient/register", #DONE: insert api to add a patient
                                     data={"patient_id":row["patient_id"],
                                            "name":row["name"],
                                             "age":row["age"],
                                              "area":row["area"]})


@then("patient from API count will increase by 1")
def check_count_increase(context):
    ok_((context.currentCount + 1) == len(requests.get("localhost:5000/lab-manager").json())) #DONE insert api to get all patients
    
@given("update request with new patient area with API")
def update_patient_from_API(context):
    for row in context.table:
        context.pre_update_patient = requests.get(""+row["patient_id"] #insert api to get patient by ID
                                           )
        context.updated_patient = requests.patch(""+row["patient_id"], #insert api to patch patient
                                                 data={"area":row["area"]})

@then("patient from API area before update NOT equal to area after update")
def check_patient_updated(context):
    ok_((context.pre_update_patient != context.updated_patient), "Patient not Updated")

@given("delete request with patient id with API")
def delete_patient_with_API(context):
    context.countBeforeDelete = len(requests.get("localhost:5000/lab-manager").json()) #DONE insert api to get all patients
    for row in context.table:
        deleted_patient = requests.delete("", #insert api to delete patient
                                          data={"patient_id":row["patient_id"]})

@then("patient from API count will decrease by 1")
def check_count_decrease(context):
    ok_((context.countBeforeDelete - 1) == len(requests.get("localhost:5000/lab-manager").json())) #DONE insert api to get all patients














