# REQUIREMENT

#### Objective:
Develop a RESTful API using Python's Flask framework that interacts with a local MongoDB database to manage employee records. The API should support the following HTTP methods: GET, POST, PUT, and DELETE for performing CRUD operations.

#### Requirements:

1. **API Base Endpoint**:
   - The base endpoint for the API will be `/api/employee`.

2. **Database**:
   - Use a local instance of MongoDB.
   - The database should contain an `employees` collection where employee records are stored.
   - Each employee record will have the following structure:
     ```json
     {
       "empid": <integer>,
       "name": <string>,
       "designation": <string>
     }
     ```

3. **HTTP Methods**:

   - **GET**:
     - When a request is made to `/api/employee`, the API should return a list of all employees stored in the MongoDB database.
     - When a request is made to `/api/employee?empid=<id>`, the API should return the details of the employee with the specified `empid`.
     - If no employee is found with the given `empid`, return an appropriate error message with a `404 Not Found` status.

   - **POST**:
     - The API should accept requests to `/api/employee` with a JSON body containing employee data.
     - The API must support the ability to add either a single employee or multiple employees at once. For multiple employees, the JSON body should be an array of employee objects.
     - Upon successful insertion, return a success message with a `201 Created` status.

   - **PUT**:
     - The API should accept requests to `/api/employee?empid=<id>` for updating employee details.
     - The request body should contain the updated data in JSON format.
     - The API should find the employee with the given `empid` and update the record with the new information.
     - If the `empid` does not exist, return an appropriate error message with a `404 Not Found` status.

   - **DELETE**:
     - The API should handle DELETE requests to `/api/employee?empid=<id>`.
     - The API must delete the employee record with the specified `empid`.
     - If the deletion is successful, return a success message with a `200 OK` status.
     - If the employee with the specified `empid` is not found, return an appropriate error message with a `404 Not Found` status.

4. **Error Handling**:
   - Implement appropriate error handling for invalid requests, including:
     - Missing or incorrect parameters.
     - Incorrect JSON format in request bodies.
     - Nonexistent employee records.
     - Return `400 Bad Request` for any malformed request.

5. **Response Format**:
   - All responses should be returned in JSON format.
   - Successful responses should include the appropriate status code and any relevant data or success messages.
   - Error responses should include an error message and the corresponding HTTP status code.

6. **Running the Application**:
   - Provide clear instructions for running the application, including setting up MongoDB locally, installing required dependencies, and running the Flask API server.

#### Deliverables:
- A Python application that fulfills the above requirements.
- A brief README file that explains how to set up and run the application locally.

