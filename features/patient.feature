Feature: Patient Management in Browser Using Flask

Scenario: Get list of all Patients from Browser
	Given request for all patients
	Then have all patients from Browser available from the application

Scenario: Add a Patient through Browser
	Given post request with patient details with Browser
	|name		|age	|area	|gender	|dob		|
	|Patient A	|40		|Leeds	|male	|10/10/1996	|
	Then patient from Browser count will increase

Scenario: Delete Patient through Browser by id
	Given delete request with patient id with Browser
	|patient_id	|
	|11			|
	Then patient from Browser count will decrease by 1