import json


def load_data(current_submission_path, current_endpoint_path, historical_path):
    """Load current quiz and historical data from JSON files."""
    with open(current_submission_path, 'r') as f:
        current_submission = json.load(f)

    with open(current_endpoint_path, 'r') as f:
        current_endpoint = json.load(f)

    with open(historical_path, 'r') as f:
        historical_data = json.load(f)

    return current_submission, current_endpoint, historical_data


def analyze_performance(historical_data):
    """
    Analyze historical performance to extract insights, including response accuracy.
    :param historical_data: List of past quizzes with question responses and response maps.
    :return: Dictionary summarizing performance per topic and overall response accuracy.
    """
    topic_performance = {}
    response_accuracy = {'correct': 0, 'total': 0}

    for quiz in historical_data:
        for question_id, response in quiz['response_map'].items():
            topic = response.get('topic', 'Unknown')
            is_correct = response.get('is_correct', 0)
            difficulty = response.get('difficulty', 0)

            # Update topic-level performance
            if topic not in topic_performance:
                topic_performance[topic] = {'correct': 0, 'total': 0, 'difficulty': []}

            topic_performance[topic]['total'] += 1
            topic_performance[topic]['correct'] += is_correct
            topic_performance[topic]['difficulty'].append(difficulty)

            # Update overall response accuracy
            response_accuracy['total'] += 1
            response_accuracy['correct'] += is_correct

    # Calculate accuracy and average difficulty for each topic
    for topic, stats in topic_performance.items():
        stats['accuracy'] = (stats['correct'] / stats['total']) * 100
        stats['avg_difficulty'] = sum(stats['difficulty']) / len(stats['difficulty'])

    response_accuracy['accuracy'] = (response_accuracy['correct'] / response_accuracy['total']) * 100

    return topic_performance, response_accuracy


def analyze_current_quiz(quiz_submission, quiz_endpoint):
    """
    Analyze performance in the current quiz.
    :param quiz_submission: User's responses for the current quiz.
    :param quiz_endpoint: Metadata about the current quiz.
    :return: Dictionary summarizing performance in the current quiz.
    """
    # Check if 'responses' key exists
    if 'responses' not in quiz_submission:
        raise KeyError("'responses' key not found in quiz_submission data. Please check the input structure.")

    topic_performance = {}

    # Loop through all questions in the quiz
    for question in quiz_submission['responses']:
        topic = question.get('topic', 'Unknown Topic')
        is_correct = question.get('is_correct', 0)
        difficulty = question.get('difficulty', 0)

        if topic not in topic_performance:
            topic_performance[topic] = {'correct': 0, 'total': 0, 'difficulty': []}

        topic_performance[topic]['total'] += 1
        topic_performance[topic]['correct'] += is_correct
        topic_performance[topic]['difficulty'].append(difficulty)

    # Calculate accuracy and average difficulty for each topic
    for topic, stats in topic_performance.items():
        stats['accuracy'] = (stats['correct'] / stats['total']) * 100
        stats['avg_difficulty'] = sum(stats['difficulty']) / len(stats['difficulty'])

    return topic_performance
