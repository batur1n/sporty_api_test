## Test Cases

| Test Case ID | Description                     | Steps                                     | Expected Result                                              | Validation Method                                                                                       |
|--------------|---------------------------------|-------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| TC1          | Get Random Poem                | GET /poem/random                         | JSON with poem details                                      | Check status code 200, validate JSON structure, ensure fields exist and are not empty                  |
| TC2          | Get Poems by Author            | GET /author/{author_name}               | JSON array of poems by author                               | Check status code 200, validate JSON array structure, ensure fields exist in each poem                  |
| TC3          | Invalid Author Request          | GET /author/NonexistentAuthor            | JSON with error message                                     | Check status code 404, validate JSON structure for error message                                       |
| TC4          | Get Poems by Title             | GET /title/{poem_title}                 | JSON array of poems matching the title                      | Check status code 200, validate JSON array structure, ensure fields exist in each poem                  |
| TC5          | Invalid Title Request           | GET /title/NonexistentTitle              | JSON with error message                                     | Check status code 404, validate JSON structure for error message                                       |

## Validation Methods Used
### Response Status Code Validation
Why Used: Checking the status code ensures that the API call was successful or failed as expected. A 200 status indicates success, while 404 indicates that the requested resource was not found.

### JSON Structure Validation:
Why Used: Validating the response format ensures that the API returns data in the expected JSON format, which is crucial for clients consuming the API. This validation checks if the response can be correctly parsed as JSON.

### Field Existence and Content Validation:
Why Used: Ensuring that specific fields (like title, author, lines) exist and are populated guarantees that the API provides meaningful and complete data. This is essential for any application using the API to display the content properly.
