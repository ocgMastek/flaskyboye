Feature: Patient Management in Browser Using Flask

Scenario: Get list of all Patients from Browser
	Given request for all patients with Browser
	Then have all patients available from the application

Scenario: Get Patient by Id from Browser
	Given request for patient using Id with Browser
	|patient_id	|
	|1			|
	Then have patient from Browser available from the application

Scenario: Add a Patient through Browser
	Given post request with patient details with Browser
	|patient_id	|name		|age	|area	|
	|1			|Patient A	|40		|Leeds	|
	Then patient from Browser count will increase by 1

Scenario: Update Patient through Browser
	Given update request with new patient area with Browser
	|patient_id	|area	|
	|1			|Leeds	|
	Then patient from Browser area before update NOT equal to area after update

Scenario: Delete Patient through Browser by id
	Given delete request with patient id with Browser
	|patient_id	|
	|1			|
	Then patient from Browser count will decrease by 1