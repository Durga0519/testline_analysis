# Testline Analysis API

## Overview
This Python-based solution analyzes student quiz performance data, generates insights, and provides personalized recommendations to improve their preparation. It focuses on highlighting weak areas, tracking improvement trends, and suggesting actionable steps to enhance preparation.

---

## Features

### 1. Data Analysis
- **Schema Exploration**: Processes current quiz data and historical quiz data to identify patterns.
- **Performance Metrics**:
  - Accuracy by topic.
  - Average difficulty levels.
  - Overall response accuracy.

### 2. Insights Generation
- Identifies weak areas, strong areas, and improvement trends.
- Provides an overview of performance gaps.

### 3. Personalized Recommendations
- Suggests topics, question types, and difficulty levels to focus on.
- Tailored recommendations based on user performance.

### 4. Bonus Features
- **Student Persona**: Classifies students with creative labels (e.g., "Accuracy Champion" or "Growth Needed").
- Highlights specific strengths and weaknesses.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or above
- Required Python libraries (install via `requirements.txt`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-link
   cd your-repo-link
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the Flask server:
   ```bash
   python main.py
   ```
2. The API will be available at `http://127.0.0.1:5000/analyze`.

### Testing with Postman
Use the following sample JSON payload to test the API:

#### Input JSON
```json
{
  "current_quiz": {
    "quiz_submission": {
      "responses": [
        {"topic": "Math", "is_correct": 1, "difficulty": 3},
        {"topic": "Physics", "is_correct": 0, "difficulty": 4},
        {"topic": "Chemistry", "is_correct": 1, "difficulty": 2}
      ]
    },
    "quiz_endpoint": {
      "quiz_id": "12345",
      "metadata": "Sample metadata about the current quiz."
    }
  },
  "historical_quiz": [
    {
      "response_map": {
        "Q1": {"topic": "Math", "is_correct": 1, "difficulty": 3},
        "Q2": {"topic": "Physics", "is_correct": 0, "difficulty": 4}
      }
    },
    {
      "response_map": {
        "Q1": {"topic": "Chemistry", "is_correct": 1, "difficulty": 2},
        "Q2": {"topic": "Math", "is_correct": 0, "difficulty": 3}
      }
    }
  ]
}
```

#### Sample Output
```json
{
  "historical_performance": {
    "Math": {"accuracy": 50.0, "avg_difficulty": 3.0},
    "Physics": {"accuracy": 0.0, "avg_difficulty": 4.0},
    "Chemistry": {"accuracy": 100.0, "avg_difficulty": 2.0}
  },
  "response_accuracy": {"correct": 3, "total": 4, "accuracy": 75.0},
  "current_performance": {
    "Math": {"accuracy": 100.0, "avg_difficulty": 3.0},
    "Physics": {"accuracy": 0.0, "avg_difficulty": 4.0},
    "Chemistry": {"accuracy": 100.0, "avg_difficulty": 2.0}
  },
  "insights": {
    "weak_areas": ["Physics"],
    "strong_areas": ["Chemistry"],
    "trends": "Consistent performance in Math; improvement needed in Physics."
  },
  "recommendations": [
    "Focus on Physics questions with moderate difficulty.",
    "Maintain consistency in Chemistry and Math."
  ],
  "comparison": {
    "Math": "Improved in accuracy.",
    "Physics": "Consistently weak; needs focus.",
    "Chemistry": "Maintained strong performance."
  },
  "persona": {
    "label": "Consistent Performer",
    "description": "Strong in many topics but with room for improvement."
  }
}
```

---

## Project Structure

```
├── main.py                 # Flask application entry point
├── analyze_data.py         # Functions for data analysis
├── insights.py             # Functions for generating insights
├── recommendations.py      # Functions for generating recommendations
├── comparison.py           # Functions for comparing current vs historical performance
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and setup instructions
```

---

## Approach Description
1. **Data Loading and Processing**:
   - Load JSON data for current and historical quizzes.
   - Parse and structure data for analysis.

2. **Performance Analysis**:
   - Analyze historical data for accuracy, difficulty, and trends.
   - Analyze the current quiz for immediate performance feedback.

3. **Insights and Recommendations**:
   - Identify strong and weak areas.
   - Provide actionable recommendations to address weak areas.

4. **Comparison and Persona Definition**:
   - Compare current quiz performance with historical trends.
   - Define the student persona for a personalized learning experience.

---

## Future Enhancements
- Add interactive visualizations using Plotly or Dash.
- Include additional metrics like time spent per question.
- Expand persona categories for better personalization.

---


