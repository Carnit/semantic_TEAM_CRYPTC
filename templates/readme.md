1. **HTML Structure**:
    - Created an HTML document with the basic structure including `<!doctype html>`, `<html>`, `<head>`, and `<body>` tags.

2. **Title**:
    - Set the title of the HTML page to "Correlation Matrix Image" using the `<title>` tag.

3. **Upload Form**:
    - Added a heading `<h2>` "Upload a CSV file" to prompt users to upload a CSV file.
    - Created a form using the `<form>` tag with the method set to "POST" and enctype set to "multipart/form-data" to handle file uploads.
    - Inside the form, added an `<input>` tag with `type="file"` and `name="file"` to allow users to select a file to upload.
    - Also added an `<input>` tag with `type="submit"` and `value="Generate Correlation Matrix Image"` to submit the form.

4. **Conditional Rendering**:
    - Used Jinja templating syntax `{% if correlation_image %}` to conditionally render the correlation matrix image.
    - If `correlation_image` is available (i.e., not `None`), displayed the image using an `<img>` tag.
    - Set the `src` attribute of the `<img>` tag to `"data:image/png;base64,{{ correlation_image }}"`, which embeds the image data as a base64-encoded string.
    - Provided alternative text for the image using the `alt` attribute.

5. **End of HTML Document**:
    - Closed all opened HTML tags (`</body>` and `</html>`).

### Note
we did not include CSS  styling in this code snippet as it was outside the scope of time