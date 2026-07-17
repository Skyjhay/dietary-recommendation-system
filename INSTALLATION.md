# Healthy Dietary Recommendation System

## Project Structure

```
dietary-recommendation-system/
├── app.py                      # Flask application entry point
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Multi-container setup
├── README.md                   # Project documentation
├── static/
│   ├── css/
│   │   └── style.css          # Custom CSS styling
│   └── js/
│       └── script.js          # Frontend JavaScript
├── templates/
│   ├── index.html             # Main recommendation page
│   ├── about.html             # About page
│   └── base.html              # Base template (if needed)
├── models/
│   └── knn_recommender.py     # KNN algorithm implementation
└── data/
    └── dietary_data.json      # Training dataset
```

## Installation & Setup

### Option 1: Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Skyjhay/dietary-recommendation-system.git
   cd dietary-recommendation-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5000`

### Option 2: Docker (Recommended for Production)

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - Open your browser and go to `http://localhost:5000`

3. **Stop the application**
   ```bash
   docker-compose down
   ```

## API Endpoints

### Get Recommendations
```
POST /api/recommend
Content-Type: application/json

{
  "age": 30,
  "weight": 75,
  "height": 175,
  "activity_level": "moderate",
  "health_conditions": ["diabetes"],
  "preferences": ["vegetarian"],
  "k": 5
}
```

**Response:**
```json
{
  "success": true,
  "user_input": {
    "age": 30,
    "weight": 75,
    "height": 175,
    "bmi": 24.49,
    "activity_level": "moderate",
    "health_conditions": ["diabetes"],
    "preferences": ["vegetarian"]
  },
  "user_metrics": {
    "bmi": 24.49,
    "tdee": 2475.5
  },
  "similar_users": [...],
  "recommendations": [...]
}
```

### Health Check
```
GET /api/health
```

### Get Health Conditions
```
GET /api/health-conditions
```

### Get Diet Preferences
```
GET /api/preferences
```

### Get Activity Levels
```
GET /api/activity-levels
```

## How the KNN Algorithm Works

1. **Data Loading**: The system loads user profiles from `data/dietary_data.json`

2. **Feature Extraction**: User health data is converted to numerical features:
   - Age, Weight, Height, BMI
   - Activity level factor
   - Health condition severity
   - Dietary preference encoding

3. **Feature Normalization**: Features are standardized using StandardScaler for fair comparison

4. **KNN Search**: For a new user:
   - Calculate normalized features
   - Find K nearest neighbors using Euclidean distance
   - Retrieve their recommended diets

5. **Recommendation**: 
   - Aggregate diets from K similar users
   - Sort by frequency
   - Return top recommendations with confidence scores

## Extending the System

### Adding More Training Data

Edit `data/dietary_data.json` to add more user profiles:

```json
{
  "user_id": 13,
  "age": 35,
  "weight": 70,
  "height": 170,
  "activity_level": "moderate",
  "health_conditions": ["none"],
  "preferences": ["none"],
  "recommended_diet": "Balanced Diet",
  "diet_description": "A balanced mix of all food groups..."
}
```

### Adding New Diet Types

1. Update `data/dietary_data.json` with new diet recommendations
2. The system will automatically include them in recommendations

### Customizing Parameters

Edit `models/knn_recommender.py` to:
- Change K value (number of neighbors)
- Add new health conditions
- Adjust activity level mappings
- Modify feature weights

## Performance Metrics

- **Response Time**: < 100ms for recommendations
- **Accuracy**: Depends on training data quality
- **Scalability**: Can handle 1000+ user profiles efficiently

## Troubleshooting

### Port Already in Use
```bash
# Change port in app.py or docker-compose.yml
python app.py  # Modify port before running
```

### Module Not Found Errors
```bash
pip install --upgrade scikit-learn numpy pandas flask flask-cors
```

### Docker Issues
```bash
# Clean up and rebuild
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

## Deployment Options

### Heroku
```bash
heroku create your-app-name
git push heroku main
heroku open
```

### AWS
- Use EC2 instance with Docker
- Or use AWS App Runner for containerized deployment

### Digital Ocean
- Deploy using Docker Droplet
- Use `docker-machine` for setup

### Google Cloud
- Use Cloud Run for serverless deployment
- Or use Compute Engine with Docker

## Security Recommendations

1. Use environment variables for sensitive data
2. Enable HTTPS in production
3. Set CORS restrictions appropriately
4. Validate all user inputs
5. Use rate limiting to prevent abuse

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
1. Check existing GitHub Issues
2. Create a new Issue with detailed description
3. Include error messages and steps to reproduce

## Disclaimer

⚠️ **This system is for informational purposes only.** Always consult with a qualified healthcare provider, registered dietitian, or nutritionist before making significant dietary changes.

## Author

Created by Skyjhay - [GitHub Profile](https://github.com/Skyjhay)

## Technologies Used

- **Backend**: Python 3.11, Flask
- **ML**: scikit-learn, NumPy, Pandas
- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript
- **Deployment**: Docker, Docker Compose
- **Algorithm**: K-Nearest Neighbors (KNN)

---

Happy recommending! 🥗🤖
