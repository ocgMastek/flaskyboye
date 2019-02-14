Feature: Patient Management in API Using Flask

Scenario: Get list of all Patients from API
	Given request for all patients
	Then have all patients from API available from the application

Scenario: Get Patient by Id from API
	Given request for patient using Id with API
	|patient_id	|
	|1			|
	Then have patient from API available from the application

Scenario: Add a Patient through API
	Given post request with patient details with API
	|name		|age	|area	|gender	|dob		|
	|Patient A	|40		|Leeds	|male	|10/10/1996	|
	Then patient from API count will increase

Scenario: Update Patient through API
	Given update request with new patient area with API
	|patient_id	|area	|
	|1			|Leeds	|
	Then patient from API area before update NOT equal to area after update

Scenario: Delete Patient through API by id
	Given delete request with patient id with API
	|patient_id	|
	|6			|
	Then patient from API count will decrease by 1