# Trade Sentry

Trade Sentry is a web application designed to streamline anomaly detection in bank stock data. It leverages powerful machine learning techniques to help users identify unusual patterns in their stock data, providing insights that can be critical for decision-making.

## Features
* **User Friendly Interface:** Built using Flask, Trade Sentry offers a seamless user experience.
* **Anomaly Detection:** Employs Scikit-learn's Isolation Forest model to detect anomalies in the uploaded data.
* **CSV Upload:** Users can upload their CSV files containing stock data.
* **Annotated Output:** After processing, users receive a downloadable CSV file with annotated anomalies.
* **Data Visualization:** Utilizes Plotly.js for interactive scatterplots, allowing users to visualize anomalies effectively.
* **Responsive Design:** Built with Bootstrap for a responsive and modern interface.

## Usage
* **Upload CSV:** Navigate to the upload section and select your CSV file containing bank stock data.
* **Detect Anomalies:** Click the 'Detect Anomalies' button to process the data.
* **Download Results:** After processing, download the CSV file with anomalies marked.
* **Visualize Anomalies:** Explore the scatterplots to visualize where anomalies occur in your data.

## Technologies Used
* **Flask:** A lightweight WSGI web application framework.
* **Scikit-learn:** A machine learning library for Python, used for implementing the Isolation Forest model.
* **Plotly.js:** A JavaScript library for interactive graphing, used for data visualization.
* **Bootstrap:** A front-end framework for developing responsive and mobile-first websites.
* **Frontend:** HTML5/CSS

