Feature: Report Management in API Using Flask

Scenario: Get list of all Reports from API
	Given request for all reports with API
	Then have all reports available from the application

Scenario: Get Report by Id from API
	Given request for Report using Id with API
	|report_id	|
	|1			|
	Then have report from API available from the application

Scenario: Add a Report through API
	Given post request with Report details with API
	|report_id	|description		|date 	 |
	|1			|symptomA, symptomB	|10/10/19|
	Then Report from API count will increase by 1

Scenario: Update Report through API
	Given update request with new Report date with API
	|report_id	|date	 |
	|1			|10/10/19|
	Then Report from API date before update NOT equal to date after update

Scenario: Delete Report through API by id
	Given delete request with Report id with API
	|report_id	|
	|1			|
	Then Report from API count will decrease by 1