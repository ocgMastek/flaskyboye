Feature: Patient Management in API Using Flask

Scenario: Get list of all Patients from API
	Given request for all employees
	Then have all employees available from the application

Scenario: Get Patient by Id from API
	Given request for patient using Id
	|patient_id	|
	|1			|
	Then have employee available from the application

Scenario: Add a Patient through API
	Given post request with patient details
	|patient_id	|name		|age	|area	|
	|1			|Patient A	|40		|Leeds	|
	Then patient count will increase by 1

Scenario: Update Patient through API
	Given update request with new patient area
	|patient_id	|area	|
	|1			|Leeds	|
	Then patient area before update NOT equal to area after update

Scenario: Delete Patient through API by id
	Given delete request with patient id
	|patient_id	|
	|1			|
	Then patient count will decrease by 1