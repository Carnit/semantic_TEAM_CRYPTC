import pandas as pd
from flask import Flask, render_template, request, send_file, redirect, url_for
import base64
import io
import matplotlib

matplotlib.use("Agg")
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder="D:\\program file\\semantic_research\\templates")


def generate_correlation_matrix_image(data):
    if data.isnull().sum().sum() > 0:
        return (
            None,
            "Data contains missing values. Please handle missing values before generating the correlation matrix.",
        )

    try:
        fig, ax = plt.subplots(figsize=(8, 8))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Correlation Matrix for All Columns")
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format="png")
        correlation_image = base64.b64encode(img_buffer.getvalue()).decode()
        img_buffer.close()
        plt.close(fig)
        return correlation_image, None

    except Exception as e:
        return None, f"An error occurred: {str(e)}"


def generate_line_graph(data):
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        data.plot(kind="line", ax=ax)
        ax.set_title("Line Graph")
        ax.set_xlabel("X-axis Label")
        ax.set_ylabel("Y-axis Label")
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format="png")
        line_graph_image = base64.b64encode(img_buffer.getvalue()).decode()
        img_buffer.close()
        plt.close(fig)
        return line_graph_image, None
    except Exception as e:
        return None, f"An error occurred: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            try:
                data = pd.read_csv(file)
                correlation_image, correlation_error = (
                    generate_correlation_matrix_image(data)
                )
                if correlation_error:
                    return correlation_error
                line_graph_image, line_graph_error = generate_line_graph(data)
                if line_graph_error:
                    return line_graph_error
                return render_template(
                    "index.html",
                    correlation_image=correlation_image,
                    line_graph_image=line_graph_image,
                )
            except Exception as e:
                return f"An error occurred while processing the file: {str(e)}"
        else:
            return "Please upload a valid CSV file."
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
