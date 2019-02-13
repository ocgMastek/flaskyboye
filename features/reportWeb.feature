Feature: Report Management in Browser Using Flask

Scenario: Get list of all Reports from Browser
	Given request for all reports with Browser
	Then have all reports available from the application

Scenario: Get Report by Id from Browser
	Given request for Report using Id with Browser
	|report_id	|
	|1			|
	Then have report from Browser available from the application

Scenario: Add a Report through Browser
	Given post request with Report details with Browser
	|report_id	|description		|date 	 |
	|1			|symptomA, symptomB	|10/10/19|
	Then Report from Browser count will increase by 1

Scenario: Update Report through Browser
	Given update request with new Report date with Browser
	|report_id	|date	 |
	|1			|10/10/19|
	Then Report from Browser date before update NOT equal to date after update

Scenario: Delete Report through Browser by id
	Given delete request with Report id with Browser
	|report_id	|
	|1			|
	Then Report from Browser count will decrease by 1