Feature: Report Management in Browser Using Flask

Scenario: Get list of all Reports from Browser
	Given request for all Reports
	Then have all Reports from Browser available from the application

Scenario: Add a Report through Browser
	Given post request with Report details with Browser
	|patient_id	|report_text|
	|8			|TEST TEXT	|
	Then Report from Browser count will increase

Scenario: Delete Report through Browser by id
	Given delete request with Report id with Browser
	|report_id	|
	|6			|
	Then Report from Browser count will decrease by 1