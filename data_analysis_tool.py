import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def analyze_data(csv_content):
    # Read CSV file into a Pandas DataFrame
    df = pd.read_csv(BytesIO(csv_content))

    # Perform data analysis - you can add your own analysis steps here
    analysis_results = df.describe()

    # Generate charts
    charts = []
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            chart = sns.histplot(df[column])
            plt.title(f'Distribution of {column}')
            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            charts.append((column, base64.b64encode(img.getvalue()).decode('utf-8')))
            plt.close()

    return analysis_results, charts
