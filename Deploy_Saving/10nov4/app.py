from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

EXCEL_FILE = "data.xlsx"

@app.route('/')
def index():
    return render_template('index.html')  # Load HTML form

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        # Get form data
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']

        # Convert to DataFrame
        df = pd.DataFrame([[name, age, city]], columns=['Name', 'Age', 'City'])

        # Check if file exists, then append or create new
        if os.path.exists(EXCEL_FILE):
            existing_df = pd.read_excel(EXCEL_FILE)
            final_df = pd.concat([existing_df, df], ignore_index=True)
        else:
            final_df = df

        # Save to Excel
        final_df.to_excel(EXCEL_FILE, index=False)

        return jsonify({'message': 'Data added successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
