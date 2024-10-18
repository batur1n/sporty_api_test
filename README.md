## Test Cases

| Test Case ID | Description                     | Steps                                     | Expected Result                                              | Validation Method                                                                                       |
|--------------|---------------------------------|-------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| TC1          | Get Random Poem                | GET /poem/random                         | JSON with poem details                                      | Check status code 200, validate JSON structure, ensure fields exist and are not empty                  |
| TC2          | Get Poems by Author            | GET /author/{author_name}               | JSON array of poems by author                               | Check status code 200, validate JSON array structure, ensure fields exist in each poem                  |
| TC3          | Invalid Author Request          | GET /author/NonexistentAuthor            | JSON with error message                                     | Check status code 404, validate JSON structure for error message                                       |
| TC4          | Get Poems by Title             | GET /title/{poem_title}                 | JSON array of poems matching the title                      | Check status code 200, validate JSON array structure, ensure fields exist in each poem                  |
| TC5          | Invalid Title Request           | GET /title/NonexistentTitle              | JSON with error message                                     | Check status code 404, validate JSON structure for error message                                       |

