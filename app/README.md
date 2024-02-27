# Flask Application for Correlation Matrix Visualization

This Flask application allows users to upload a CSV file containing data, generates a correlation matrix for the data, and displays the correlation matrix as a heatmap using Seaborn. 
## Python Requirments
- `Python 3.6.0 and more`
## Library Requirements
- `pandas` for data manipulation
- `Flask` for web framework
- `matplotlib` and `seaborn` for plotting
- `base64` for encoding images
- `os` for file operations

## Setup

1. Import required libraries.
2. Initialize Flask app.
3. Define a function to generate a correlation matrix image.
4. Create a route for the index page.

## Functions

- `generate_correlation_matrix_image(data)`: Generates a correlation matrix heatmap image from the provided data. If there are any missing values in the data, it returns `None`. Otherwise, it saves the image, encodes it as base64, and removes the temporary file.

## Routes

- `/`: The index route handles both GET and POST requests. 
    - If a POST request is received with a CSV file, it reads the file, generates a correlation matrix image, and renders the `index.html` template with the correlation matrix image.
    - If the uploaded file is not a CSV or an error occurs during processing, it redirects to the index page.
    - If a GET request is received, it renders the `index.html` template.

## Running the Application

- If the script is executed directly (`__name__ == '__main__'`), the Flask app runs in debug mode.

## File Structure

- `templates/`: Contains HTML templates used by Flask.
# working 
this product/tool is stil incomplete and has a lot to work on, but results we got is suprising 
![image](D:\semantic_research\output\correlation matrix image .png)
