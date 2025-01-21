def compare_current_to_historical(current_performance, historical_performance):
    """
    Compare current quiz performance with historical performance.
    :param current_performance: Performance summary of the current quiz.
    :param historical_performance: Historical performance data.
    :return: Comparison results.
    """
    comparison = {}

    for topic, current_stats in current_performance.items():
        historical_stats = historical_performance.get(topic, {})
        historical_accuracy = historical_stats.get('accuracy', 0)
        current_accuracy = current_stats['accuracy']

        if current_accuracy > historical_accuracy:
            comparison[topic] = "Improved performance in the current quiz."
        elif current_accuracy < historical_accuracy:
            comparison[topic] = "Performance declined in the current quiz."
        else:
            comparison[topic] = "Consistent performance with historical trends."

    return comparison
