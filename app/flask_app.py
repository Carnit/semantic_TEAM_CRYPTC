import pandas as pd
from flask import Flask, render_template, request, send_file, redirect, url_for
import base64
import io  # For in-memory data handling
import matplotlib

matplotlib.use("Agg")
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(
    __name__, template_folder="D:\\program file\\semantic_research\\templates"
)


def generate_correlation_matrix_image(data):
    """Generates a correlation matrix image from the given DataFrame.

    Args:
        data (pd.DataFrame): The DataFrame for which to generate the correlation matrix.

    Returns:
        tuple: A tuple containing the base64-encoded image data (str) or None if there are errors,
               and an error message (str) or None if no errors occurred.
    """

    if data.isnull().sum().sum() > 0:
        return (
            None,
            "Data contains missing values. Please handle missing values before generating the correlation matrix.",
        )

    try:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Correlation Matrix for All Columns")

        # Use an in-memory buffer for the image data
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format="png")

        correlation_image = base64.b64encode(img_buffer.getvalue()).decode()
        img_buffer.close()  # Close the buffer after encoding
        plt.close(fig)  # Close the figure

        return correlation_image, None

    except Exception as e:
        return None, f"An error occurred: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]

        if file and file.filename.endswith(".csv"):
            try:
                data = pd.read_csv(file)

                correlation_image, error = generate_correlation_matrix_image(data)
                if error:
                    return error

                return render_template(
                    "index.html", correlation_image=correlation_image
                )
            except Exception as e:
                return f"An error occurred while processing the file: {str(e)}"
        else:
            return "Please upload a valid CSV file."

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
