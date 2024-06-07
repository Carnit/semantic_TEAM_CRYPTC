from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

app = FastAPI()


class UploadFileModel(BaseModel):
    file: UploadFile


def generate_correlation_matrix_image(data):
    try:
        if data.isnull().sum().sum() > 0:
            raise ValueError(
                "Data contains missing values. Please handle missing values before generating the correlation matrix."
            )
        fig, ax = plt.subplots(figsize=(8, 8))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Correlation Matrix for All Columns")
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format="png")
        correlation_image = base64.b64encode(img_buffer.getvalue()).decode()
        img_buffer.close()
        plt.close(fig)
        return correlation_image
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


def generate_line_graph(data):
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        data.plot(kind="line", ax=ax)
        ax.set_title("Line Graph")
        ax.set_xlabel("X-axis Label")
        ax.set_ylabel("Y-axis Label")
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format="png")
        line_graph_image = base64.b64encode(img_buffer.getvalue()).decode()
        img_buffer.close()
        plt.close(fig)
        return line_graph_image
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a valid CSV file.")

    try:
        data = pd.read_csv(file.file)
        correlation_image = generate_correlation_matrix_image(data.copy())
        line_graph_image = generate_line_graph(data.copy())
        return {
            "correlation_image": correlation_image,
            "line_graph_image": line_graph_image,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the file: {str(e)}",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
