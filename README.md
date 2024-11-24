# Flavour Voyage


## 📖 Description  

**Flavour Voyage** is a Flask-based web application that helps users discover recipes tailored to their input ingredients. The app includes advanced filters for refining search results, ensuring users can easily find recipes that match their preferences.

The web app is built with modularity in mind, adhering to the principle of single-responsibility, where each HTML page serves a specific purpose. This design makes the project easier to manage and scale.  

### Key Features:
- **Ingredient-Based Search**: Users can input ingredients to generate recipe suggestions.
- **Filtering Options**: Further refine search results with additional filters.
- **User Accounts**: Create and log in to save favorite recipes.
- **Dynamic Interaction**: Uses JavaScript for responsive and dynamic content updates.  
- **Edamam API Integration**: Fetches recipes and nutritional data seamlessly.



## Technology Stack 🛠️

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap for responsive design

### Backend
- Python
- Flask web framework
- SQLite database for user data storage
- Edamam API for recipe data

## 🗂️ Project Structure  

The project follows Flask's standard folder hierarchy:  

```
flavour-voyage/
├── templates/          # HTML template files
├── static/            
│   ├── css/           # Stylesheet files
│   ├── js/            # JavaScript files
│   └── images/        # Image assets
├── app.py             # Main Flask application
└── database.db        # SQLite database
```
The backend leverages Flask and Python for routing and logic, while JavaScript handles DOM manipulation to present user-selected recipes dynamically. Edamam's API is integrated for fetching recipe data, with default API keys stored securely in the script for out-of-the-box functionality.



## API Integration 🔌

This project uses the Edamam Recipe API to fetch comprehensive recipe data. The integration provides:
- Detailed recipe information
- Nutritional data
- Ingredient lists and quantities
- Cooking instructions

### API Configuration

To run this project locally, you'll need to:
1. Sign up at [Edamam Developer Portal](https://developer.edamam.com/)
2. Obtain your API key and ID
3. Configure your credentials in the application



## 🎥 Demonstrations  
- **Video Demo**: [Watch Here](https://youtu.be/jkae9y8z0g4)  
- **Live Demo**: [Flavour Voyage](https://flavour-voyage.onrender.com/)  



## Future Roadmap 🗺️

### Short-term Goals
- Enhanced security features
- Additional API integrations
- Mobile-responsive design optimization
- User preference persistence

### Long-term Goals
- Recipe recommendation system
- Social sharing features
- Multiple language support
- Advanced dietary tracking



## Lessons Learned 📚

This project provided valuable insights into:
- Working with RESTful APIs and handling API documentation
- Building dynamic web applications with Flask
- Frontend-backend integration
- User authentication and session management
- Responsive web design principles


## License 📝

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
