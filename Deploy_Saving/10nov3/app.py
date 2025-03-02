from flask import Flask, render_template, jsonify,request

import pandas as pd
import os

app=Flask(__name__)

excel_file="data.xlsx"
@app.route('/add_data', methods=['POST', 'GET'])
def add_data():
    try:
        if request.method == 'GET':
            return jsonify({"message": "Send data using POST method"}), 200
        
        # get json data from request
        data = request.get_json()

        # convert to dataframe
        df = pd.DataFrame([data])

        # check if file exists, then append or create new
        if os.path.exists(excel_file):
            existing_df = pd.read_excel(excel_file)
            final_df = pd.concat([existing_df, df], ignore_index=True)
        else:
            final_df = df

        # Save data to Excel
        final_df.to_excel(excel_file, index=False)

        return jsonify({"message": "Data added successfully", "data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
if __name__ == '__main__':
    app.run(debug=True)
