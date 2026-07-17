"""
Healthy Dietary Recommendation System using KNN
Main Flask Application
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os
from models.knn_recommender import KNNDietaryRecommender

app = Flask(__name__)
CORS(app)

# Initialize the KNN Recommender
recommender = KNNDietaryRecommender(k=5)
recommender.load_data('data/dietary_data.json')
recommender.train()

@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Dietary Recommendation System',
        'version': '1.0.0'
    }), 200

@app.route('/api/recommend', methods=['POST'])
def get_recommendation():
    """
    Get dietary recommendations based on user health metrics
    
    Expected JSON payload:
    {
        "age": int,
        "weight": float (kg),
        "height": float (cm),
        "activity_level": str ("sedentary", "light", "moderate", "vigorous"),
        "health_conditions": list (["diabetes", "hypertension", etc.]),
        "preferences": list (["vegetarian", "vegan", etc.]),
        "k": int (number of neighbors to consider, default: 5)
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['age', 'weight', 'height', 'activity_level']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'error': f'Missing required field: {field}'
                }), 400
        
        # Extract parameters
        age = int(data.get('age'))
        weight = float(data.get('weight'))
        height = float(data.get('height'))
        activity_level = data.get('activity_level', 'moderate')
        health_conditions = data.get('health_conditions', [])
        preferences = data.get('preferences', [])
        k = int(data.get('k', 5))
        
        # Validate ranges
        if age < 1 or age > 120:
            return jsonify({'error': 'Age must be between 1 and 120'}), 400
        if weight < 10 or weight > 500:
            return jsonify({'error': 'Weight must be between 10 and 500 kg'}), 400
        if height < 50 or height > 250:
            return jsonify({'error': 'Height must be between 50 and 250 cm'}), 400
        
        # Get recommendations
        recommendations = recommender.recommend(
            age=age,
            weight=weight,
            height=height,
            activity_level=activity_level,
            health_conditions=health_conditions,
            preferences=preferences,
            k=k
        )
        
        return jsonify({
            'success': True,
            'user_input': {
                'age': age,
                'weight': weight,
                'height': height,
                'bmi': round(weight / ((height / 100) ** 2), 2),
                'activity_level': activity_level,
                'health_conditions': health_conditions,
                'preferences': preferences
            },
            'recommendations': recommendations
        }), 200
        
    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/api/health-conditions', methods=['GET'])
def get_health_conditions():
    """Get list of available health conditions"""
    conditions = [
        'diabetes',
        'hypertension',
        'heart_disease',
        'obesity',
        'anemia',
        'thyroid',
        'celiac',
        'ibs',
        'gout',
        'none'
    ]
    return jsonify({'conditions': conditions}), 200

@app.route('/api/preferences', methods=['GET'])
def get_preferences():
    """Get list of available diet preferences"""
    preferences = [
        'vegetarian',
        'vegan',
        'keto',
        'low_carb',
        'high_protein',
        'gluten_free',
        'dairy_free',
        'low_sodium',
        'none'
    ]
    return jsonify({'preferences': preferences}), 200

@app.route('/api/activity-levels', methods=['GET'])
def get_activity_levels():
    """Get list of available activity levels"""
    levels = [
        'sedentary',
        'light',
        'moderate',
        'vigorous'
    ]
    return jsonify({'levels': levels}), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('data', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
