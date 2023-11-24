# Flavour Voyage
#### Video Demo:  https://youtu.be/jkae9y8z0g4
#### Description:

This project is a flask web app designed to display recipes that consists of ingredients that the user input. It also has filters for further refining the search results. 

The web app is separated into different HTML pages with each page doing specific tasks, this is done to micro manage the project more efficiently and as a basic software principle that one page needs to do one task. 

Since this is a flask app, it has different folder within the main folder. The templates folder has all the HTML files, these are the files that get rendered by the python script when the user selects any route/option. Furthermore the project also hosts a static folder where the CSS and Java Script files are located. This folder also contains all the images that the project depends on. Besides the app also has a database that stores user information.

The app uses the edamam api to get the recipe information. Right now inside the python script default api keys are stored as constants and all the information including user's choice gets parsed by python before sending it back to the Java Script. The Java Script later manipulates the DOM to show the information recieved. The app can be used out of the box, this is done for making the user experience convenient, however users can register and create a account in the app and later login to bookmark/favorite their desired recipes, which they can later view. 

## API Reference

### Edamam API

I have used the Edamam API to fetch recipe data and nutritional information. To use this app, you'll need to obtain your API key from Edamam. Visit [Edamam Developer](https://developer.edamam.com/) to get your API key.

## Lessons Learned

While building this project, I got to experience and learn how to interact with apis, how important it is to go through the documentation, this is especially important when working with different technologies and any small error can result in breaking down the project, as I had first hand experience with this. I also got to know a web app is developed, by first building the foundations using HTML, CSS and Java Script and slowly transforming the site to a dynamic page and then later hosting it. 

## Roadmap

- Additional security

- Add more integrations

- Making it mobile friendly


## Tech Stack

**Client:** HTML, BootStrap, CSS, Java Script

**Server:** Java Script, Python 

### Live Demo

*You can check out the live demo at:* flavour-voyage.onrender.com

## Authors

- [@Eusha425](https://www.github.com/Eusha425)

