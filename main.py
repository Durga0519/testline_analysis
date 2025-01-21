from flask import Flask, request, jsonify
from analyze_data import load_data, analyze_performance, analyze_current_quiz
from insights import generate_insights
from recommendations import generate_recommendations
from comparison import compare_current_to_historical

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze both current and historical quiz data.
    Expected Input: JSON with 'current_quiz' and 'historical_quiz' keys.
    """
    data = request.json
    current_submission = data.get('current_quiz', {}).get('quiz_submission', {})
    quiz_metadata = data.get('current_quiz', {}).get('quiz_endpoint', {})
    historical_data = data.get('historical_quiz', [])

    try:
        # Analyze historical performance
        historical_performance, response_accuracy = analyze_performance(historical_data)

        # Analyze current quiz performance
        current_performance = analyze_current_quiz(current_submission, quiz_metadata)

        # Generate insights and recommendations
        insights = generate_insights(historical_performance, response_accuracy)
        recommendations = generate_recommendations(historical_performance)

        # Compare current quiz vs historical trends
        comparison = compare_current_to_historical(current_performance, historical_performance)

        return jsonify({
            'historical_performance': historical_performance,
            'response_accuracy': response_accuracy,
            'current_performance': current_performance,
            'insights': insights,
            'recommendations': recommendations,
            'comparison': comparison
        })
    except KeyError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f"Unexpected error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
