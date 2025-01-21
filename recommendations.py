def generate_recommendations(performance_data):
    """
    Generate recommendations to improve preparation.
    :param performance_data: Dictionary of topic-wise performance stats.
    :return: List of recommendations.
    """
    recommendations = []

    for topic, stats in performance_data.items():
        if stats['accuracy'] < 50:
            recommendations.append(f"Focus on practicing more questions in '{topic}' to improve accuracy.")
        elif stats['avg_difficulty'] > 3.5:
            recommendations.append(f"Review foundational concepts in '{topic}' to tackle harder questions effectively.")
        else:
            recommendations.append(f"Keep practicing in '{topic}' to maintain strong performance!")

    return recommendations
