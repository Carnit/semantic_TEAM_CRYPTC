import pandas as pd
from flask import Flask, render_template, request, send_file, redirect, url_for
import base64
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt
import os

app = Flask(__name__, template_folder='templates')

def generate_correlation_matrix_image(data):
    if data.isnull().sum().sum() > 0:
        return None, 

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Matrix for All Columns')
    fig.savefig('correlation_matrix.png')
    with open('correlation_matrix.png', 'rb') as f:
        correlation_image = base64.b64encode(f.read()).decode()
    os.remove('correlation_matrix.png')

    return correlation_image, None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']

        if file and file.filename.endswith('.csv'):
            try:
                data = pd.read_csv(file)

                if data.empty or len(data.columns) == 0:
                    return 

                correlation_image, error = generate_correlation_matrix_image(data)

                if error:
                    return error

                return render_template('index.html', correlation_image=correlation_image)
            except Exception as e:
                return 'An error occurred: {}'.format(str(e))
        else:
            return redirect(url_for('index'))

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)