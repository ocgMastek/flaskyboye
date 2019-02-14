Feature: Patient Management in API Using Flask

Scenario: Get list of all Patients from API
	Given request for all patients
	Then have all patients from API available from the application

Scenario: Add a Patient through API
	Given post request with patient details with API
	|name		|age	|area	|gender	|dob		|
	|Patient A	|40		|Leeds	|male	|10/10/1996	|
	Then patient from API count will increase

Scenario: Delete Patient through API by id
	Given delete request with patient id with API
	|patient_id	|
	|11			|
	Then patient from API count will decrease by 1