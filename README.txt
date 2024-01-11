# Wikipedia Search API

This Flask application serves as a simple Wikipedia search API. It allows users to query Wikipedia for information on a specific search term in a chosen language.

## Usage

### Installation

1. Ensure you have Python 3.11 installed on your system.
2. Install the required dependencies by running:


### Running the Application

Run the following command in the terminal:
python api.py

By default, the application will be accessible at `http://127.0.0.1:5000/`.

### API Endpoint

- **Endpoint:** `/wiki/<string:search_term>`
- **Method:** `GET`

#### Request Parameters

- `search_term` (required): The search term to look up on Wikipedia.
- `lang` (optional): The language for the Wikipedia search (default is 'cs').

#### Response

- If the exact article is found, it returns the first paragraph of the article with a status code of 200.
- If the article is not found, it returns a 404 status with a JSON response indicating that the article was not found.
- If the search term exists in other articles, it returns a 303 status with a redirection to the Wikipedia search results for that term.

## Error Handling

- In case of an internal server error during processing, it returns a JSON response with a 500 status code.

## Note

- This application uses the Wikipedia API for searching and extracting information.