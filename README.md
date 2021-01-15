# Data Centric Development - Milestone Project - Food Search


## UX
 
Food search is an online, free-to-use recipe directory. Using Food search you will be able to find recipes crreated by community members (registered accounts), create, edt and delete your own recipes. 

I have created a simple yet sleek style and layout to ensure all user-types can use the website without errors. The navigation is very easy to use and I have included many call-to-actions to help users get to where they need to be quicker. All forms are created with guidence on what to enter. For example, I have asked that people enter new ingredients one per line. 

I created mockups using my preffered prototyping software, Adobe XD. The mockups can be found in PDF format here - https://github.com/cobyfoster/data-centric-dev-milestone/tree/master/static/media/mockup.pdf
If the above link returns GitHub errors, refer to this dropbx link - https://www.dropbox.com/s/yctaq48sgbqcxzz/mockup.pdf?dl=0

I used the mockups as guidence and then futher edited the layout in code to make it more user friendly and responsive. 

## Features

Create account:
I have added the functionality for users to create an account. Once they have an account, they can create, edit and delete their own recipes as well as still having the ability to access other user's recipes.

Login:
The login functuinality allows people to return to their account after leaving the site / loggin out. Without ths eature, they would not be able to edit or delete their recipes. 

Logout:
This feature allows members that are logged-in to log-out. By loggin out, it removed the session cookie therefor going back to the log-in page. 

Add Recipe:
This feature allows logged-in members to create recipes and add them to the database. Once they do this, they are then able to edit and delete the entry. It also creates a dedicated page for the recipe and displays for the community.

Edit Recipe:
Logged-in users can edit their own recipes. The 'edit_recipe' form auto-fills with the current data then pushes the new data to the database on submit. 

Delete Recipe:
This does what it says on the tin, It allows members to DELETE their own recipes from the database. 

Search:
A custom search bar on the 'community_recipes' page allows members to search for recipes names, description or origin. It also allows you to reset the search.

View Recipe:
On both the 'my_recipes' and 'community_recipes' pages, you are able to view all recipes on the site. This takes you to a dedicated page (with a dedicated URL) to view the recipe content.

Password security:
All Passwords are hashed when users register.

Navigation:
Some list-items in the navigation will appear and dissapear depending on if you are logged in. This is to stop anyone from creating recipes, only logged in users can do this. 

Flash messages:
Flash messages are used to notify the user of a change. For e.g, if you login or register, you will recieve a welcome message. This message will then dissapear and be recplaced by the original content. The flash messages can be seen in the 'slim-banner' section of most pages below the header.

Logic:
Overall, an extensive amount of logic is being used. It's used to search the database for usernames and passwords, as well as displaying relevant contnt dependig on who is logged in. 

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- Python
- HTML5
- CSS / Materialize
- JS / JQuery
- Mongodb
- Flask
- Heroku (for deployement)
- Adobe XD (for mockups)

## Testing


## Deployment



## Credits

### Content


### Media


### Acknowledgements
