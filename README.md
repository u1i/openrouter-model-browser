# Openrouter Model Browser

Model Browser is a web application built using Flask that allows users to browse, sort, and view details about different models fetched from a remote API endpoint.

## Features

- Fetch model data from a predefined API endpoint.
- Display model data in a tabular format using an HTML template.
- Sort models by name, date created, or context length in ascending or descending order.
- Provide human-readable date formatting for model creation dates.

## Requirements

- Python 3.x
- Flask
- Requests

Ensure you have these dependencies installed. You can install them using pip:

```bash
pip install flask requests
```

## Installation and Usage

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the Flask application:

```bash
python app.py
```

4. Open a web browser and go to `http://localhost:8080` to view the Model Browser.

## Project Structure

- `app.py`: The main Flask application file that contains routes and logic to fetch and display model data.
- `templates/model_browser.html`: HTML template that displays the data in a table format and provides options to sort it.

## How It Works

- The app fetches model information from the `https://openrouter.ai/api/v1/models` endpoint.
- Data is processed and displayed in a user-friendly format.
- Users can choose to sort the data by different criteria, and the client-side template will reflect these changes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.