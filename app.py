from flask import Flask, request, send_file, render_template
import pandas as pd
import os
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

app = Flask(__name__)
quantity_list = []
volume_list = []
anomaly_list = []
output_path = ''

@app.route('/', methods=['GET'])
def homepage():  
    return render_template('index.html')  

@app.route('/', methods=['POST'])
def detect_anomalies():
    global output_path, quantity_list, volume_list, anomaly_list

    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    if not file.filename.endswith('.csv'):
        return 'Invalid file format. Please upload a CSV file', 400

    file_path = os.path.join(app.root_path, file.filename)
    file.save(file_path)

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        return f'Error loading CSV file: {str(e)}', 400

    category_deviation_map = {
        1: 10,
        2: 20,
        3: 30
    }
    df['Deviation Cap'] = df['Category ID'].map(category_deviation_map)
    
   
    df['Anomaly'] = 1  
    
    df.loc[df['Deviation'] > df['Deviation Cap'], 'Anomaly'] = -1  

    selected_columns = ['close', 'volume']  
    X = df[selected_columns]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    clf = IsolationForest(contamination=0.01)  
    clf.fit(X_scaled)

    all_predictions = clf.predict(X_scaled)
    df_anomalies = df.iloc[all_predictions == -1]

    plt.figure(figsize=(7, 6))
    plt.plot(df.index, df['close'], color='blue', label='Close Price')
    plt.scatter(df_anomalies.index, df_anomalies['close'], color='red', label='Anomalies')
    plt.title('Anomalies Detected by Isolation Forest with Deviation Cap Condition (Entire Dataset)')
    plt.xlabel('Index')
    plt.ylabel('Close Price')
    plt.legend()
    plt.savefig('static/anomalies_plot.png')  
    plt.close()

    output_filename = 'anomaly_predictions.csv'
    output_path = os.path.join(app.root_path, output_filename)
    df.to_csv(output_path, index=False)   

    quantity_list = df['close'].tolist()
    volume_list = df['volume'].tolist()
    anomaly_list = df['Anomaly'].tolist() 

    return render_template('result.html')

@app.route('/download', methods=['GET'])
def download():
    return send_file(output_path, as_attachment=True)

@app.route('/scatter_plot', methods=['GET'])
def scatter():
    return render_template('scatter_plot.html', quantity_list=quantity_list, volume_list=volume_list, anomaly_list=anomaly_list)

@app.route('/anomalies_plot', methods=['GET'])
def anomalies_plot():
    return render_template('anomalies_plot.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)