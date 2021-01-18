# Data Centric Development - Milestone Project - Food Search

The project is deployed on Heroku here - https://data-centric-dev.herokuapp.com/

![mockup](/static/media/mockup.png)


How to use the site and check functionality:

1. Load website and navigate through the homepage
2. Create account using a username and password. 
3. Add a recipe following the form instructions.
4. View the recipe by accessing the 'my_recipes' page. 
5. Edit the recipe using the edit icon on this page. 
6. Delete said recipe.
7. Logout
8. Login using the same Username and Password
9. Navigate to the community recipes page.
10. Use search function as instructed int the paragraph text.

## UX
 
Food search is an online, free-to-use recipe directory. Using Food search you will be able to find recipes created by community members (registered accounts), create, edit and delete your own recipes. 

I have created a simple yet sleek style and layout to ensure all user-types can use the website without errors. The navigation is very easy to use and I have included many call-to-actions to help users get to where they need to be quicker. All forms are created with guidance on what to enter. For example, I have asked that people enter new ingredients one per line. 

I created wireframes using my preferred prototyping software, Adobe XD. The wireframes can be found in PDF format here - https://github.com/cobyfoster/data-centric-dev-milestone/tree/master/static/media/
If the above link returns GitHub errors, refer to this dropbox link - https://www.dropbox.com/sh/b37uwqzqgutwbt8/AAB8qQWU0wDdnCJqTbopZIn0a?dl=0

I used the wireframes as guidance and then further edited the layout in code to make it more user friendly and responsive. The design itself is naturally responsive so it did not require many updates. 

## Features

Create account:
I have added the functionality for users to create an account. Once they have an account, they can create, edit and delete their own recipes as well as still having the ability to access other user's recipes.

**Login**:
The login functionality allows people to return to their account after leaving the site / logging out. Without this feature, they would not be able to edit or delete their recipes. 

**Logout**:
This feature allows members that are logged-in to log-out. By logging out, it removed the session cookie therefor going back to the log-in page. 

**Add Recipe**:
This feature allows logged-in members to create recipes and add them to the database. Once they do this, they are then able to edit and delete the entry. It also creates a dedicated page for the recipe and displays for the community.

**Edit Recipe**:
Logged-in users can edit their own recipes. The 'edit_recipe' form auto-fills with the current data then pushes the new data to the database on submit. 

**Delete Recipe**:
This does what it says on the tin, It allows members to DELETE their own recipes from the database. 

**Search**:
A custom search bar on the 'community_recipes' page allows members to search for recipes names, description or origin. It also allows you to reset the search.

**View Recipe**:
On both the 'my_recipes' and 'community_recipes' pages, you are able to view all recipes on the site. This takes you to a dedicated page (with a dedicated URL) to view the recipe content.

**Password security**:
All Passwords are hashed when users register.

**Navigation**:
Some list-items in the navigation will appear and disappear depending on if you are logged in. This is to stop anyone from creating recipes, only logged in users can do this. 

**Flash messages**:
Flash messages are used to notify the user of a change. For e.g, if you login or register, you will receive a welcome message. This message will then disappear and be replaced by the original content. The flash messages can be seen in the 'slim-banner' section of most pages below the header.

**Logic**:
Overall, an extensive amount of logic is being used. It's used to search the database for usernames and passwords, as well as displaying relevant content depending on who is logged in. 
Each recipe has it's own page, if the recipe author is logged in, then they will also be able to edit and delete that recipe. 
The descriptions displayed in the recipes overview boxes is truncated (150).

## Technologies Used

In the development of this project, I have used the following technologies.
- Python
- HTML5
- CSS / Materialize
- JS / JQuery
- Mongodb
- Flask
- Heroku (for deployment)
- Adobe XD (for mockups)
- Jinja Templating Language

## Testing

### Code / Automatic Testing
#### Server Response - Heroku
See Line 19 of the tests.py file. Here I ran a HTTP request to my Heroku URL to check the server response. 

Outcome - (200) OK.


#### Database connection - MongoDB
See line 28 of tests.py. Here I connected to my Database and created a 'tests' collection within the DB. I then created a function that added a dict to that collection.

Outcome - I checked the Database collection and the document was there with the correct entry data. Going very well so far!


### Manual Testing
#### Visually check Heroku
To ensure the server response was correct in my automatic testing, I want to my Heroku project to confirm it was working as expected. 

Outcome - The correct data was visible and the connection to GITHUB master branch was working correctly.


#### POST mongodb data
This involves the testing of my add_recipe page and my register / login functionality. 

First I created a user without using my visual form, I then checked mongo manually to make sure that it was working as it should. I did this in my app.py the same way I did it in my tests.py file (just for the user collection). This was also how I tested the password hashing function of Werkzeug.

Outcome - on first attempt, it did not work. So I went to stack overflow to find some information on how the hashing feature works. It turns out, I was not importing the correct werkzeug.security as I should have done.

Result - I swiftly fixed this error, and re-tested. It works! I then tested my form inputs and again, it works as it should!


#### GET mongodb data
Before starting any of the UI design code, I wanted to pull data from mongo. On my home page, I created a box which got all document field "name" in the 'recipes' database. 

Outcome - The document name came up as expected. This can be found it my earlier commits to GitHub on the index page. 


#### W3C Validation & PEP-8 compliance
The GitPod IDE already has PEP-8 compliance helpers, it shows me when a line is too long or when the corret spaces are not applied. I then went to http://pep8online.com/ and entered all of my code (several checks, one for each doc). I then checked URL's using https://validator.w3.org/.

Outcome - As my IDE has PEP-8 helpers there were no issues. However, I did have a few minor issues with W3C that I resolved swiftly. 


#### UX testing
I did this in 2 stages. Then followed with 3rd party testing. 

1. I manually checked all links, buttons, triggers and forms to make sure that they were all working correctly.
2. I used a link checking tool https://www.internetmarketingninjas.com/

Outcome - The manual check showed NO incorrect links. The automatic tool did not recognise all buttons but did not come back with any errors. I then double tested manually to make sure!

3rd Party testing - I then asked my partner to test the websites functionality. I did not give her any guidance on how to use the website, instead I gave her the mouse and told her to use it as if it were BBC Good Food.

Outcome - Quote from Pinsuda "The app's styling was welcoming and strong images of food made me want to keep reading! The community recipe sharing functionality was really easy to use and a great way for sharing recipes. I like the search tool on the search page but I feel that I should be able to look for the origin of the dish as this is something you have to input into the add recipe fill out form."

my response - I added the origin to the search functionality, then I cooked dinner...


#### Responsive testing
To test the apps responsiveness, I did this 2 ways. 

1. Using Google's inspect elements device toolbar. I set it to responsive and changed between screen widths. 
2. I manually tested using my iPhone 12 Pro Max, my partners Samsung note 20 and an old iPhone 8 I had lying around. I then tested with my samsung Tab S6 and my partners iPad air. 

Outcome - There were a few minor issues on mobile, especially on the iPhone 8. These issues were on the Grey boxes on login, register and search function. Easy fixes, I increased passing in these areas.

#### Browser testing 
To check browser compatibility, I navigated and used the site on the following browsers.
1. Google Chrome
2. Mozilla Firefox
3. Microsoft Edge
4. Opera
5. IE11 (deprecated)

Outcome - All browsers were fine although I did notice a color error on IE11. I must also note, IE11 is incredibly slow but I read up on this and it is not due to the application itself. 

#### Google Lighthouse
The report as follows. 

1. Performance 66/100
This is due to me not using webP as image file type. I did not do this as WebP is not supported on all browsers and devices.

2. Accessibillity 86/100
This is due to background color and foreground color. I do not agree with this as I have used shadows to identify the different sections. I did not change my code. 

3. Best Practices 93/100 - Updated 98/100!
Great score! The report told me to add rel="noopener" to my outbound links in the footer. After doing this, it updated to 98!

4. SEO 96/100
No comments here!


## Deployment
The website was coded in GitPod, an IDE used to easily work with GitHub. I started by creating my repository in GitHub then forming an initial commit with the message "initial commit". I then used "Git Push" to push this through to GitHub.

I created a MongoDB database to store the users and recipes data. I then set this up in Heroku using the config Vars settings to keep the database information secure. A Procfile was created to run the app in Heroku. 

To keep the process automated, I had enabled Heroku to get the mater branch from GitHub everytime it was updated. This means that when I push from GitPod, it pulls that data into Heroku. 

## Credits

### Content
Recipes - Recipes were taken from the BBC Good Food website - https://www.bbcgoodfood.com/

### Media
I have used free stock images from Pexels - https://www.pexels.com/

Valeria Boltneva - https://www.pexels.com/photo/close-up-photo-of-burger-1639562/

Mike - https://www.pexels.com/photo/variety-of-spices-and-vegetables-on-black-surface-1192031/