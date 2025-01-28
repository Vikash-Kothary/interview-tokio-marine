# TMHCC Insurance Underwriting Project - Senior Software Developer Exercise

## Background, Objectives and Requirements

In this exercise, you will design a backend application for retrieving insurance policy data, with an emphasis on code clarity, scalability, and maintainability.

You may assume that you have already been given some data for insurance policies, prepopulated in a database.

The application you design must expose this data via an API whilst providing a flexible structure for switching between choice of database as requirements evolve.

The technical product owner has expressed interest in the principles of Domain-Driven Design (DDD) and has asked for them to be used throughout the codebase. Additionally, they have provided you with several requirements (listed below) that you should observe:

## Requirements

### 1. Domain Modeling & Application Layers

- [x]  (domain) Implement DDD by defining the core domain model around an &#39;Insurance Policy&#39; entity and its related operations.
- [x] (domain.models) Establish a domain layer that includes entities, value objects, and aggregates, with the
Insurance Policy as the primary aggregate.
- [x] (application.services) Create an application layer that orchestrates operations on the Insurance Policy entity, focusing on reading policy data.

### 2. Web Service

- [x] (fastapi) Choose a lightweight Python web framework to build a RESTful API.
- [x] (api/v1/policies) Implement a read-only endpoint for retrieving &#39;Insurance Policy&#39; data.
- [.] (See Exceptions) Expose only the necessary details via the API, maintaining encapsulation of domain logic
within the domain layer.

### 3. Database

- [x] (infrastructure.repositories) Select any database of your choice for data storage.
- [x] (domain.repositories) Implement enough abstraction so that we can swap out the database whenever required.

### 4. Testing

- [.] Implement unit tests and integration tests for critical parts of the codebase.
- [x] (Readme) Include instructions on running the tests and demonstrate the effectiveness of the tests.

### 5. Documentation

- [x] (Readme) Include comprehensive documentation for setting up and running the project.
- [x] (Openapi) Clarify the endpoints, data models, and any other relevant details.


## Submission Guidelines

- Please aim to spend no more than 2 hours on this. You can document what you could have done if given more time. An incomplete solution is also fine.
- [x] Provide a GitHub repository containing the entire project.
- [x] Include a README file explaining how to set up and run the application.
- [x] If applicable, mention any additional considerations or improvements that the candidate
would make if given more time.

## Evaluation Criteria

- [x] How the candidate approaches the assessment and considers assumptions, dependencies, etc.
- [x] How the candidate structures the application using DDD principles and considers maintainability.
- [x] Clarity in the separation of concerns between domain, application, and infrastructure layers.
- [x] Code quality, readability, and adherence to DDD principles.
- [x] Use of dependency injection to keep infrastructure components, like databases, separate from domain logic.
- [x] Clarity and completeness of documentation, especially around design decisions.
- [x] Demonstrated test coverage for critical parts of the codebase.