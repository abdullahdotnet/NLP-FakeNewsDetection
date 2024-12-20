from flask import Flask, request, jsonify
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the pickled model and vectorizer at the start of the application
with open('svm_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vector_model.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the news text from the request JSON
        data = request.get_json(force=True)
        news_text = data.get('news')

        if not news_text:
            return jsonify({'error': 'No news text provided'}), 400

        # Vectorize the input news text
        news_vector = vectorizer.transform([news_text])

        # Perform prediction
        prediction = model.predict(news_vector)

        # Map prediction to human-readable response
        result = 'Fake News' if prediction[0] == 1 else 'Real News'

        # Return the result as JSON
        return jsonify({'prediction': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
