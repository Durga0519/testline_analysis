def generate_insights(performance_data, response_accuracy):
    """
    Generate insights from performance data, including improvement trends and strengths/weaknesses.
    :param performance_data: Dictionary of topic-wise performance stats.
    :param response_accuracy: Overall response accuracy data.
    :return: List of insights.
    """
    insights = []

    if response_accuracy['accuracy'] < 50:
        insights.append(f"Overall accuracy is low ({response_accuracy['accuracy']:.2f}%). Focus on fundamentals.")
    else:
        insights.append(f"Good overall accuracy ({response_accuracy['accuracy']:.2f}%). Keep up the good work!")

    for topic, stats in performance_data.items():
        if stats['accuracy'] < 50:
            insights.append(f"Weak in '{topic}' (Accuracy: {stats['accuracy']:.2f}%). Practice more questions.")
        elif stats['avg_difficulty'] > 3.5:
            insights.append(f"'{topic}' involves high-difficulty questions. Consider foundational revisions.")
        else:
            insights.append(f"Strong in '{topic}'! Accuracy: {stats['accuracy']:.2f}%.")

    return insights
