


# Vegan Dot Recipes:
```python
This project is a data-driven online cook book with vegan recipes. 
Website logic is mainly written in Python(Django framework),HTML,CSS, bootstrap framework, materialize framework.
SQlite DB was used to store data. In the project were used CRUD operations to Create,Read,Update and delete recipes.
Website purpose is to share information about vegan recipes in one place.
Users can buy recipes and upload/sell own ideas(sell functionality will be implemented in future)
Only users who are registered and logged can access full content of the website.
```

# UX DESIGN

[MOCKUp](https://app.moqups.com/Vau7X8SpAb/view/page/aa9df7b72)

```python
The project was created for consumers who are looking for the ideas for vegan recipes.
My plan was to create website, in which users could easily find vegan recipes and buy them, share their own vegan recipes and also keep in one place all their favorite ones.
I believe that it will make users want to come back to my website again and again.

Project design was inspared by 'Blueapron' recipes website (https://www.blueapron.com/pages/sample-recipes).
On it's main page, recipes are presented as a cards with clear description and meal image. 
It will help to create positive user experience and encourage users to interact with the website.

On main page we can also find clear navigation with particular tabs. It will help users easily navigate the page, for example: search, upload and edit recipes and also log out.
There are tabs leading to particular meals such us starters, main courses, desers, smoothies or juices. 
It helps users to find recipe fast and easy from one category to another.

There is a 'home page' tab which quickly redirect users to main page where are all recipes.

Tab named 'Upload recipe' leads users to the page where they can add their own recipes to the website.

There is also 'log out' tab and users can use it to log out from website anytime and from any page.

'My profile' tab leads users to his/her profile page where they can find recipes uploaded by his/her before. They can remove or edit recipe from there. 
There is also section where are all purchased recipes by user(they can be easy viewed and deleted from there)
 
The navigation is usefull and simple for user. It makes a user-friendy page and easy to searching through website content. 

On initial main page there are only 3 tabs: to register, login and cart(to add recipes). 
On that page user can only see general info about recipe(price, views, name,short description and picture).
User can also add recipe to cart and buy it by processing payment. To buy recipe user need to create an account and login.
After that user will have access to own profile page. Purchased recipes can be view only from user profile page. 
After login user can use navigation to find recipes by categories, logout upload recipes and buy recipes.
```


# USER'S STORIES :

```bash
As a vegan person I want to find information about vegan recipes so that I can cook my vegan food at home
 -After log in user can search recipes and also share his/her own meals ideas with others.
```

```bash
As person with intolerance and allergy for some products, I want to make sure that meals I find don't contain harmful for me allergens.
 -Each recipe has list of allergens so users can check what type of allergens are in the meal.
```

```bash
As a person on diet I want to find information about nutrition facts so I can keep ballance in my diet.
 -All recipes have nutrition info table in which users can check all nutrition facts. For example ammount of proteins in meal.
```

# FEATURES 

### Meals category tabs feature
Website has a seperate tabs for each meal category which is very helpfull for searching recipes. 
By clicking tab name, user can find recipes from particular category.
For example tab 'Desers' will return only desers meals.
After user clicks name of category tab, filter() function is executed and all recipes from that category are returned (based on query filter).


### Add recipe feature(Create)
By filling out a form in upload recipe template, user can add a recipe to the database and the website using add_recipe function(by clicking 'upload recipe' button). 
After that recipe is uploaded to DB according to Product model structure.


### Find Recipe feature(Read)
When user clicks 'view' button to see recipe, recipe_detail() function is executed to find requested recipe by primary key.
User is redirected to the recipe_details page where information from the database is presented in a readable format to the user.


### Edit recipe feature(Update)
In 'my profile' tab, user can find each uploaded recipes. By clicking edit button in particular recipe card, user can edit recipes uploaded on the website before.
It will redirect him/her to edit form on which updates can be done. After making changes and click 'update recipe' button, edit_recipe() function is executed and changes are updated in SQlite database. 
To find particular recipe and its entry SQlite uses id.


### Delete Recipe(Delete) feature
Each recipe can be deleted in 'My profile' tab, by clicking on 'X' button found at the bottom of each recipe card. 
Once it is clicked delete() function is executed on localised recipe(primary key). It delete recipe from DB based on particular model.


### My recipes(in my profile) feature
Each recipe uploaded by user can be managed in 'My profile' tab. User can view, edit or delete recipe from website and DB. 

### User profile feature
User is able to log in to his/her account to use full content of website, keep and manage recipes that she/he added or purchased.
After clicking on 'my profile' tab User is redirected to his/her profile page. In there user can see his/her details,
'recipes uploaded by me' section and 'recipes purchased by me' sections. 
In 'recipes uploaded by me' section user can view, edit or delete recipe.
In 'recipes purchased by me' section user can only view purchased recipe and delete it from that section.

User can delete added recipe in section 'uploaded by me' and by doing this, delete recipe complately from website.
User can delete each recipe that she/he bought in section 'purchased by me'.
Recipe will be deleted only from users profile not from website.

### Add to cart feature
User is able to add to cart recipes that wish to buy. It can be done without login in but 
user need to be logged in finish payment and get recipe on profile page.


### Log in/Log out feature
User is able to login and log out to the website and full authentication is added. 
To login user need to use username and password created in registration process.



# FEATURES LEFT TO IMPLEMENT

### Social media sharing feature
Let user post and share recipes on social media

### Add to favorites feature
User will be able to add recipes to favorites and then manage them in 'My recipes' tab. By clicking 'add to favorites' button.

### Add comments and rate feature
User will be able to add comment in comments section in each recipe. 
User also will be able rate recipe from 1 to 5 starts.


### Add sell recipe feature
While user uploading recipe, he/she sets price for added recipe. After someone will pay for that recipe ,
user will get money for it. Would like to create section in user's profile to track ammount of sold recipes.

### password reset feature
User is able to reset password. User is redirecting to password reset form and after form validaton user 
gets email with reseting link.

### Admin recipes review
It will let Admin review recipes uploaded by users before they will be added to website.
It could avoid uploading non vegan recipes to website.

# TECHNOLOGIES USED

```python
Python - To create backend and add functionalities to project. LINK https://www.python.org/

HTML - To create basic structure of the project LINK ( https://www.w3schools.com/html/ )

CSS - To add styles to the project. Also some part of responsiveness was done by css styles by adding media queries.

Bootstrap framework - To create responsive layout and add some design and components by add helpfull classes. LINK: https://getbootstrap.com/

Django framework - To create backend and add functionalities to the project. Django helps backend and front end work together as a whole LINK: https://www.djangoproject.com/

Google Fonts - To add some fonts. LINK : https://fonts.google.com/

Materialize framework  - To create responsive layout and add some design and components LINK ( https://materializecss.com/ )

JavaScript - To add interaction to project LINK: https://www.javascript.com/

Stripe API - To add payment functionality to website and let users to process payments for choosen recipes.
```

# TESTING

```python

Application was tested manually by pretending to be a user.

Testing registration functionality - Expected that user after fill registration form is redirected from registration page to home page,
succes message is presented and user is able to use website in full.

Testing log in / log out functionality - Expected that user is redirected from log in page to home page, after fill out and submit a log in form.
Expecting that user name typed in login form is presented in my profile page after log in. Check if user can use website fully 


Testing add recipe functionality - Making sure that when click on 'upload recipe' tab, user is redirected to add_recipe page.
Expected that after fill out and submit add recipe form, all data is presented on recipe's page as planned. Also cancel button on add_recpe page was tested, by clicking and checking if user is redirected to previous page.


Testing Meals category tabs functionality - Expected that after clicking tab with particular category name, user will be redirected to that page.
Check if only recipes from that category are found and presented.


Testing 'view' button functionality - Check if after click 'view' button, user is redirected to recipe_details page. 


Testing edit recipe functionality - Go to 'My profile' and click edit button on recipe to update. Check if user is redirected to 'edit_recipe' page(edit form) and if correct data from database is presented in the form.
Check if data is correctly updated to database after refill edit form and if it is presented on recipe's page with no issues.


Testing delete recipe functionality - Check if recipe is deleted from database and also website after clicing 'X' (red button wit 'X' sign) button.
Make sure if deleting correct recipe. Also deletingfrom purchased recipe was tested in simillar way.


Testing my profile tab(recipes managing) functionality - Testing if user is redirected to 'My profile' page after clicing 'My profile' tab. 
Expected to see all uploaded by user recipes with view, delete and edit buttons(possibility). Also checking if after purchasing, 
recipes are in 'purchased by me ' section.


Testing home page tab functionality - Testing if user is redirected to 'home page' after clicking 'home' tab. By clicking 'home' from any website locations.

Project was based on Graceful degradation approach which means that desktop version was created as first then responsiveness was added for mobile and tablets. 
Media query and bootstrap responsive classes were used to achieve that. Projects responsiveness was tested by google developer tools where it was resising to particular device size(for example iphones,samsung ) 
It was tested also by changing size of browser window. Application was tested after each functionality was added to it.
```

# DATABASE SCHEMA

The database is structured with django models such as Product(recipes), Purchases(recipes bought by users),
Order(for orders) and OrderLineItem(orders in line).
Profile(will be used in future to edit user profile details and add picture) 
Each model determines how entries and items will be stored in SQlite DB.

Particular items in DB are localised by pk and id's.
Each model contains structured data with model fields that relating to each description of the entries. 
django forms are used to add and update etries in/to DB 


# DEPLOYMENT

The project was deployed on Heroku platform under link : https://vegan-dot-recipes-django.herokuapp.com/

# COMMANDS USED TO DEPLOY PROJECT TO HEROKU:


```python
git init (create empty repository)
git add ( to add files)
git commit -m'' (to commit changes and add message)
heroku login (To log in to heroku platform)
heroku ps:scale web=1 (to run app on heroku)
git push heroku master ( to push local repository to heroku)

The project was deployed to Heroku with config vars:

IP = 0.0.0.0
PORT = 5000

The development and deployed versions are the same.

```


# CREDITS

Logo was taken from instagram profile https://www.instagram.com/vegan_dot/?hl=en My project will be linked to it in future.




