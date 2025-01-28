# TMHCC Insurance Underwriting Project - Senior Software Developer Exercise

## Background, Objectives and Requirements

In this exercise, you will design a backend application for retrieving insurance policy data, with an emphasis on code clarity, scalability, and maintainability.

You may assume that you have already been given some data for insurance policies, prepopulated in a database.

The application you design must expose this data via an API whilst providing a flexible structure for switching between choice of database as requirements evolve.

The technical product owner has expressed interest in the principles of Domain-Driven Design (DDD) and has asked for them to be used throughout the codebase. Additionally, they have provided you with several requirements (listed below) that you should observe:

## Requirements

### 1. Domain Modeling & Application Layers

- Implement DDD by defining the core domain model around an &#39;Insurance Policy&#39; entity and its related operations.
- Establish a domain layer that includes entities, value objects, and aggregates, with the
Insurance Policy as the primary aggregate.
- Create an application layer that orchestrates operations on the Insurance Policy entity,
focusing on reading policy data.

### 2. Web Service

- Choose a lightweight Python web framework to build a RESTful API.
- Implement a read-only endpoint for retrieving &#39;Insurance Policy&#39; data.
- Expose only the necessary details via the API, maintaining encapsulation of domain logic
within the domain layer.

### 3. Database

- Select any database of your choice for data storage.
- Implement enough abstraction so that we can swap out the database whenever required.

### 4. Testing

- Implement unit tests and integration tests for critical parts of the codebase.
- Include instructions on running the tests and demonstrate the effectiveness of the tests.

### 5. Documentation

- Include comprehensive documentation for setting up and running the project.
- Clarify the endpoints, data models, and any other relevant details.


## Submission Guidelines

- Please aim to spend no more than 2 hours on this. You can document what you could have done if given more time. An incomplete solution is also fine.
- [ ] Provide a GitHub repository containing the entire project.
- [ ] Include a README file explaining how to set up and run the application.
- [ ] If applicable, mention any additional considerations or improvements that the candidate
would make if given more time.

## Evaluation Criteria

- [ ] How the candidate approaches the assessment and considers assumptions, dependencies, etc.
- [ ] How the candidate structures the application using DDD principles and considers maintainability.
- [ ] Clarity in the separation of concerns between domain, application, and infrastructure layers.
- [ ] Code quality, readability, and adherence to DDD principles.
- [ ] Use of dependency injection to keep infrastructure components, like databases, separate from domain logic.
- [ ] Clarity and completeness of documentation, especially around design decisions.
- [ ] Demonstrated test coverage for critical parts of the codebase.