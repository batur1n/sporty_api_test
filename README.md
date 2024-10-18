## Test Cases
### Test Case 1: Get Random Poem
Step 1: Send a GET request to the endpoint /poem/random.
Expected Result: A JSON response containing a poem with fields like title, author, lines, etc.
Validation: 
  Check that the response status code is 200.
  Validate that the response is a JSON object.
  Ensure that the fields title, author, and lines exist in the response and are not empty.

### Test Case 2: Get Poems by Author
Step 1: Send a GET request to the endpoint /author/{author_name} (e.g., /author/Emily%20Dickinson).
Expected Result: A JSON response containing an array of poems by the specified author.
Validation:
  Check that the response status code is 200.
  Validate that the response is a JSON array.
  Ensure that each poem in the array has the fields title, author, and lines.

### Test Case 3: Invalid Author Request
Step 1: Send a GET request to the endpoint /author/{author_name} with a non-existent author (e.g., /author/NonexistentAuthor).
Expected Result: A JSON response with an error message indicating that the author is not found.
Validation:
  Check that the response status code is 404.
  Validate that the response is a JSON object containing an error message.
  
### Test Case 4: Get Poems by Title
Step 1: Send a GET request to the endpoint /title/{poem_title} (e.g., /title/Hope).
Expected Result: A JSON response containing an array of poems matching the title.
Validation:
  Check that the response status code is 200.
  Validate that the response is a JSON array.
  Ensure that each poem in the array has the fields title, author, and lines.

### Test Case 5: Invalid Title Request
Step 1: Send a GET request to the endpoint /title/{poem_title} with a non-existent title (e.g., /title/NonexistentTitle).
Expected Result: A JSON response with an error message indicating that no poems are found with the given title.
Validation:
  Check that the response status code is 404.
  Validate that the response is a JSON object containing an error message.
