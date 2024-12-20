from flask import Flask, request, jsonify, send_from_directory
import pickle
import nltk
import time
import pymysql
from datetime import datetime

nltk.download('stopwords')

# Initialize Flask app
app = Flask(__name__)

# Load the pickled model and vectorizer at the start of the application
with open('svm_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vector_model.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

DB_HOST = "db"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "Model_Logger"
def log_to_db(input_params, output, response_time):
    try:
        print("Connecting to DB")
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        print("Entering log_to_db")
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Log (Current_Date_Time, Input_Params, Output, Response_Time)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (datetime.now(), str(input_params), str(output), response_time))
        connection.commit()
        print("Data Inserted")
    finally:
        connection.close()


@app.route('/')
def home():
    return send_from_directory('.', 'index.html')  # Serve index.html from the current directory

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the news text from the request JSON
        data = request.get_json(force=True)
        news_text = data.get('news')
        start_time = time.time()
        if not news_text:
            return jsonify({'error': 'No news text provided'}), 400

        # Vectorize the input news text
        news_vector = vectorizer.transform([news_text])

        # Perform prediction
        prediction = model.predict(news_vector)

        # Map prediction to human-readable response
        result = 'Fake News' if prediction[0] == 1 else 'Real News'
        response_time = time.time() - start_time

        try:
            log_to_db(input_params=data, output=result, response_time=response_time)
        except Exception as e:
            print(f"Logging error: {e}")
        # Return the result as JSON
        return jsonify({'prediction': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)
