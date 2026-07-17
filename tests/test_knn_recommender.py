"""
Example test file for the Dietary Recommendation System
Place test files in a tests/ directory
"""

import pytest
from models.knn_recommender import KNNDietaryRecommender


class TestKNNRecommender:
    """Test suite for KNN Recommender"""
    
    @pytest.fixture
    def recommender(self):
        """Create recommender instance for testing"""
        rec = KNNDietaryRecommender(k=3)
        rec.load_data('data/dietary_data.json')
        rec.train()
        return rec
    
    def test_recommender_initialization(self):
        """Test recommender initialization"""
        rec = KNNDietaryRecommender(k=5)
        assert rec.k == 5
        assert rec.is_trained == False
    
    def test_bmi_calculation(self, recommender):
        """Test BMI calculation"""
        bmi = recommender._calculate_bmi(70, 175)
        assert abs(bmi - 22.86) < 0.01
    
    def test_tdee_calculation(self, recommender):
        """Test TDEE calculation"""
        tdee = recommender._calculate_tdee(70, 175, 30, 'moderate')
        assert tdee > 0
    
    def test_feature_extraction(self, recommender):
        """Test feature extraction"""
        profile = {
            'age': 30,
            'weight': 70,
            'height': 175,
            'activity_level': 'moderate',
            'health_conditions': ['none'],
            'preferences': ['none']
        }
        features = recommender._extract_features(profile)
        assert len(features) == 7  # 7 features extracted
        assert all(isinstance(f, (int, float)) for f in features)
    
    def test_model_training(self, recommender):
        """Test that model trains successfully"""
        assert recommender.is_trained == True
        assert recommender.knn_model is not None
        assert recommender.features is not None
    
    def test_recommendation_output(self, recommender):
        """Test recommendation output format"""
        result = recommender.recommend(
            age=30,
            weight=70,
            height=175,
            activity_level='moderate',
            health_conditions=['none'],
            preferences=['none'],
            k=3
        )
        
        assert result['status'] == 'success'
        assert 'user_metrics' in result
        assert 'similar_users' in result
        assert 'recommendations' in result
        assert len(result['similar_users']) > 0
        assert len(result['recommendations']) > 0
    
    def test_invalid_input_handling(self, recommender):
        """Test handling of invalid inputs"""
        # This would require the recommender to implement validation
        # and raise exceptions or return error states
        result = recommender.recommend(
            age=-5,  # Invalid age
            weight=70,
            height=175,
            activity_level='moderate',
            health_conditions=[],
            preferences=[]
        )
        
        # Should handle gracefully
        assert result is not None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
