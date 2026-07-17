# Contributing to Healthy Dietary Recommendation System

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome diverse perspectives
- Focus on constructive feedback
- No harassment or discrimination

## Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/dietary-recommendation-system.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow PEP 8 for Python code
   - Add comments for complex logic
   - Write clear commit messages

4. **Test your changes**
   ```bash
   python -m pytest tests/
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Describe your changes clearly
   - Reference related issues
   - Include screenshots if applicable

## Development Setup

```bash
# Clone repository
git clone https://github.com/Skyjhay/dietary-recommendation-system.git
cd dietary-recommendation-system

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies with dev tools
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
pytest tests/

# Format code
black .

# Lint code
flake8 .
```

## Coding Standards

### Python
- Follow PEP 8
- Use type hints where applicable
- Write docstrings for all functions
- Keep lines under 100 characters

### Example:
```python
def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index.
    
    Args:
        weight: Weight in kilograms
        height: Height in centimeters
        
    Returns:
        Calculated BMI value
    """
    return weight / ((height / 100) ** 2)
```

### JavaScript
- Use ES6+ features
- Use meaningful variable names
- Add JSDoc comments for functions
- Keep functions small and focused

### CSS
- Use BEM naming convention
- Group related styles
- Use CSS variables for colors
- Mobile-first approach

## Commit Messages

Write clear, descriptive commit messages:

```bash
# Good
git commit -m "Add KNN algorithm implementation with feature normalization"

# Avoid
git commit -m "Fix stuff"
git commit -m "WIP"
```

Format:
```
<type>: <subject>

<body>

<footer>
```

Types: feat, fix, docs, style, refactor, perf, test, chore

## Testing

- Write tests for new features
- Maintain >80% code coverage
- Test edge cases
- Include integration tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test
pytest tests/test_knn_recommender.py
```

## Documentation

- Update README.md for major changes
- Add docstrings to new functions
- Include code examples where helpful
- Document API changes

## Issues

### Reporting Bugs
- Use clear, descriptive title
- Describe expected vs actual behavior
- Include steps to reproduce
- Add error messages/screenshots
- Specify OS and Python version

### Feature Requests
- Explain the use case
- Describe the expected behavior
- Provide examples if possible
- Discuss alternatives

## Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Ensure all tests pass**
4. **Update CHANGELOG** if maintaining one
5. **Follow commit message guidelines**
6. **Request review** from maintainers
7. **Address feedback** promptly

## Areas for Contribution

### Priority
- [ ] Expand training dataset
- [ ] Improve accuracy metrics
- [ ] Add more dietary recommendations
- [ ] Enhance UI/UX

### Open Issues
- See GitHub Issues for current needs
- Comment on issues to express interest
- Ask questions if unclear

### Documentation
- Fix typos
- Improve clarity
- Add examples
- Translate documentation

## Questions?

- Open a GitHub Discussion
- Email: your-email@example.com
- Check existing issues/PRs first

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🙏
