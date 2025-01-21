import matplotlib.pyplot as plt
import seaborn as sns

# Example data
historical_performance = {
    'Math': {'accuracy': 70, 'avg_difficulty': 3.2},
    'Physics': {'accuracy': 50, 'avg_difficulty': 4.0},
    'Chemistry': {'accuracy': 85, 'avg_difficulty': 2.8}
}

current_performance = {
    'Math': {'accuracy': 60, 'avg_difficulty': 3.5},
    'Physics': {'accuracy': 55, 'avg_difficulty': 3.8},
    'Chemistry': {'accuracy': 90, 'avg_difficulty': 3.0}
}

response_accuracy = {'correct': 80, 'total': 100, 'accuracy': 80}

# 1. Historical Performance by Topic
def plot_historical_performance(historical_performance):
    topics = list(historical_performance.keys())
    accuracies = [v['accuracy'] for v in historical_performance.values()]
    
    plt.figure(figsize=(8, 6))
    sns.barplot(x=topics, y=accuracies, palette='viridis')
    plt.axhline(50, color='red', linestyle='--', label='Weak Threshold (50%)')
    plt.title("Historical Performance by Topic")
    plt.ylabel("Accuracy (%)")
    plt.xlabel("Topic")
    plt.legend()
    plt.show()

# 2. Current vs Historical Performance Comparison
def plot_current_vs_historical(historical_performance, current_performance):
    topics = list(historical_performance.keys())
    historical_accuracies = [v['accuracy'] for v in historical_performance.values()]
    current_accuracies = [current_performance[topic]['accuracy'] for topic in topics]

    x = range(len(topics))
    plt.figure(figsize=(8, 6))
    plt.bar(x, historical_accuracies, width=0.4, label='Historical', align='center')
    plt.bar([p + 0.4 for p in x], current_accuracies, width=0.4, label='Current', align='center')
    plt.xticks([p + 0.2 for p in x], topics)
    plt.title("Current vs Historical Performance")
    plt.ylabel("Accuracy (%)")
    plt.xlabel("Topic")
    plt.legend()
    plt.show()

# 3. Response Accuracy Pie Chart
def plot_response_accuracy(response_accuracy):
    labels = ['Correct', 'Incorrect']
    sizes = [response_accuracy['correct'], response_accuracy['total'] - response_accuracy['correct']]
    colors = ['#66b3ff', '#ff9999']
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Response Accuracy")
    plt.show()

# Generate the plots
plot_historical_performance(historical_performance)
plot_current_vs_historical(historical_performance, current_performance)
plot_response_accuracy(response_accuracy)
