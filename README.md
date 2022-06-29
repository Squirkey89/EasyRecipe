# Easy Recipe

The aim of the project was to build a website using the Django framework. This is my fourth portfolio project. I chose to build a recipe website as I felt I would be able to design a high-quality website and could implement the features that I wanted to. I created a website called Easy Recipe. This website was designed to be a simple and user friendly website. The website's objective is to create a database of recipes that can be shared among users. The website is aimed at anyone who loves cooking and wants to learn about and share recipes. The website can also be useful for someone who is just learning how to cook.&nbsp;

![amiresponsive](https://user-images.githubusercontent.com/91072896/176175582-3c050314-42f4-4145-b0dc-b92506eacc34.png)


# Table of Contents
1. [UX](#id-ux)
2. [Structure](#id-structure)
    * [Flow Chart](#id-flow)
    * [Wireframe](#id-wireframe)
    * [Database Schema](#id-Database-Schema)
3. [Features](#id-features)
    * [Navigation-bar ](#id-nav)
    * [Banner/About](#id-banner) 
    * [How it Works](#id-works)
    * [Recipes](#id-recipes)
    * [Edit/Delete recipe](#id-edit/delete)
    * [Comments](#id-comments)
    * [Like Button](#id-like)
    * [Sign Up/Login](#id-login)
4. [Features to Implement in the future](#id-implement)
5. [Testing](#id-testing) 
6. [Bugs](#id-bugs) 
7. [Technologies Used](#id-technologies)
8. [Deployment](#id-deployment)
9. [Credits](#id-credits)
10. [Acknowledgements](#id-acknowledgements)





# UX<div id='id-ux'>
## User Stories

### As a User 

* As a user I can register an account so that I can post comments, recipes and interact with users posts. 
* As a user I can post and read comments so that So I can give feedback and read feedback from others. 
* As a user I can access the recipe page so that I can find recipes that I am interested in using. 
* As a site admin I can approve comments on the website so that content is posted is relevant related to the website.                                                         									
* As a user I can I can upload images with the recipes so that it will give users a visual representation of the 
recipe. 
* As a user I can log out of my account when I'm done using the website. so that if I used a public computer my account is safe. 
* As a user I can easily navigate around the website so that I can view the information that I want. 

### As a Site admin

* As a site admin I can delete, edit and update the recipes on the website so that content is posted is relevant related to the website. 
* As a site admin I can approve comments on the website so that content is posted is relevant related to the website. 

# Structure

## Flow Chart<div id='id-flow'>
This flow chart I created shows the structure of the application I wanted to create.&nbsp;

![flow chart](https://user-images.githubusercontent.com/91072896/176413657-9c65fe51-4a18-4fee-9671-e3c44fee1395.png)

### Wireframe<div id='id-wireframe'>

![Screenshot 2022-06-28 13 32 24](https://user-images.githubusercontent.com/91072896/176179862-bd053d41-5468-4798-a442-8f3e70aa9b7b.png)
![Screenshot 2022-06-28 13 32 34](https://user-images.githubusercontent.com/91072896/176179861-84dd805a-7de7-4aff-b78a-1a57b6718b62.png)
![Screenshot 2022-06-28 13 33 01](https://user-images.githubusercontent.com/91072896/176179857-1b7a4fa1-45fa-4818-9e41-76d3a05577ac.png)
![Screenshot 2022-06-28 13 33 11](https://user-images.githubusercontent.com/91072896/176179850-f2b2313f-f069-4086-a6e0-cdfcb3a3b951.png)
![Screenshot 2022-06-28 13 33 31](https://user-images.githubusercontent.com/91072896/176179841-c1d4918d-13d9-4e27-b39c-8458644fb1d2.png)
![Screenshot 2022-06-28 13 33 18](https://user-images.githubusercontent.com/91072896/176179849-87a2ad60-fd35-4a12-994f-0f283c3ce4f2.png)

## Database Schema<div id='id-Database-Schema'>
![Database Schema](https://user-images.githubusercontent.com/91072896/176322366-e91262a5-08d5-4414-a403-23a1e3a8fe61.png)


# Features<div id='id-features'>

## Navigation-bar<div id='id-nav'>

The navigation bar is at the top of the website. This includes the website name which appears at the left of the nav bar. It also includes links to different pages that the user can visit. The navbar is simple and I believe that it is easy for the user to use. The navbar links change format to hamburger format if the website is viewed on smaller devices. The text is easy to read on the offwhite background. Images of each navigation bar are provided below.&nbsp;

![navbar](https://user-images.githubusercontent.com/91072896/176243638-21130cfe-0e03-4159-accd-3332882433ff.png)
![navbar1](https://user-images.githubusercontent.com/91072896/176243630-737ead99-6d3c-4564-9e33-45aa62b3d15c.png)

## Banner and about sections<div id='id-banner'>

The banner image appears under the navbar with some text that transitions. The about section of the website discusses the website's purpose and goal in a paragraph following the banner.&nbsp;

![Banner](https://user-images.githubusercontent.com/91072896/176245284-e4932381-1633-4bf8-a38d-88f2d2265b15.png)

This section is about the websites purpose.&nbsp;

![WWD](https://user-images.githubusercontent.com/91072896/176274425-11370ef5-3b5c-41cb-ba2b-f4d6b1ff2a5a.png)

## How it works<div id='id-works'>

At the end of the page there are three linked images. Above the images is a heading explaining how it works. This is to show the user with the linked images, what they need to do to start using the website. The first image is the registration page, as this is the first step the user undertakes. The next image is creating a recipe and the final image is the recipe link. This communicates to the users that they first have to sign up to the website and then they can create and view recipes.&nbsp;

![HIW](https://user-images.githubusercontent.com/91072896/176275423-4611f935-1c64-4ea9-b7da-88f7e3d28a45.png)

## Recipes<div id='id-recipes'>

The recipes page is where the user's recipes are displayed. Once a recipe is created on the create recipe page the user can view it on the recipes page. On the recipes page you can find limited information, cook time, prep time, and the number of servings per recipe. However the user can see more details about each recipe by clicking on recipetails. The recipe page is paginated and can hold six recipes per page.&nbsp;

![Recipes](https://user-images.githubusercontent.com/91072896/176276742-9fc44f5a-ca3b-4db1-b886-beab396bff72.png)

## Edit/delete recipe.<div id='id-edit/delete'>  

This is located on the recipe detail page. This can only be actioned if the user was the one who had created the recipe they cannot edit or delete recipes left by other users. If they are not authorized the option will not appear on the page for that user. If the user wants to edit the page they will be brought to a form where they can change any of the information, they put in. If they choose delete, they will be brought to another page to confirm that they want to delete the recipe.&nbsp;

![edit delete](https://user-images.githubusercontent.com/91072896/176322923-dc4883d8-834a-4e8e-8439-11f578d6e64e.png)

## Comments<div id='id-comments'>

You can find the comments section on the recipe detail page below the instructions for the recipe. A user can post a comment below, but must be authorized to do so. Those who do not register can see comments left below, but will not be able to post a comment until registering an account.&nbsp;

![comments](https://user-images.githubusercontent.com/91072896/176325102-949b646e-6ba5-4583-ac1b-fc2fe053488b.png)

## Like Button<div id='id-like'>

 

The like button is located below the image on the recipe detail page. The button is also accompanied by a like counter. This is visible to all users. However, the like button is only accessible to registered users once they have created an account and registered.&nbsp; 

![Like button](https://user-images.githubusercontent.com/91072896/176424001-dae37289-4c53-45b0-8b70-71794abe385d.png)

## Sign Up/Login<div id='id-login'>

The Sign up page is designed to allow new users to create an account which will give them more access to the site. They will create their profile with a username, password that needs to be repeated to ensure is correct and an optional email address if the user would like to. If users already have an account they can sign in to gain more access.&nbsp; 

![login](https://user-images.githubusercontent.com/91072896/176425682-81476035-52e6-4371-83a0-5fce58a0c9a3.png)
![sign up](https://user-images.githubusercontent.com/91072896/176425689-5a3ca789-bbed-4c35-9334-3d054f2e7c16.png)

# Features to Implement in the future<div id='id-implement'>

## Search bar
  * This feature would allow the user to type into the search bar a keyword and the result would be all recipes containing that keyword on the website. I think at the beginning it would be fine to get by without the search bar, but as the number of recipes increase over time, this feature would be very helpful. 


## Categories
  * This feature would categorize each recipe into categories based on type of food. This makes it much easier for the user to find the type of recipe they are looking for. So if I was to implement it now, I would categorize this by countries, the categories would be Italian food, Chinese food, American food etc. 

## Comment counter
   * A feature similar to the like counter would keep track of the number of comments made on a post. As more comments on a recipe mean more opinions and may play a role in influencing the user's decision to try it, this would benefit the user as well.

## Nutrional informtaion
   * This will have nutritional information about each recipe, such as the amount of protein, fats, and carbohydrates. I believe this would be helpful to the user since many people track macros, so they can identify how much of these macros they are consuming from each recipe. Also When making a recipe for their children, parents can determine whether the recipe is healthy.



## Star rating
   * While I have a like button on the recipe detail page on each recipe, I would definitely like to implement a star system. I would put this on the bottom of the cooking info card, and also on the recipe cards on the recipe page. This would be used instead of the like button. This would give better feedback to the user on of how successful they were when using the recipe.


# Testing<div id='id-testing'>
## User Stories

### As a User 

1. As a user I can register an account so that I can post comments, recipes and interact with users posts.
   * Users can register an account by going to the sign up page and once this process has been complete they can the interact with other users posts and recipes.

2. As a user I can post and read comments so that So I can give feedback and read feedback from others. 
   * Users that register an account through the sign-up page can visit the view recipe page this is where the comment field appears. The user can create a comment on the recipe and read comments left by other users. 

3. As a user I can access the recipe page so that I can find recipes that I am interested in using.
   * Recipes on the Easy Recipe website couldn’t be easier to find. There are two links on the home page one in the nav bar and another further down the page. On the recipe page, the user can click on the recipe to view this in more detail. 
 

4. As a user I can like comments so that I can interact with other users on the site.
   * On the view recipe page, below the recipe, there is a "like" button and a "like counter" that can be used once a user has signed up and is available only to authorized users. 

5. As a user I can I can upload images with the recipes so that it will give users a visual representation of the 
recipe. 
   * When creating a recipe, users can upload images to correspond with their recipe. These are then available to view on the Recipe and recipe detail pages.    Additionally, the user can modify the image on the edit recipe page. 

6. As a user I can log out of my account when I'm done using the website. so that if I used a public computer my account is safe. 
   * The user can create an account with a unique pasword and id this will ensure that the users information is safe and if they are useing a 
      public computer there is no chance that anyone can acess his/her account

7. As a user I can easily navigate around the website so that I can view the information that I want. 
   * There is a navigation bar at the top of the site that allows the user to access wherever they are on the site. The website is simple and can be easily navigated 
     by using the navigation bar. Each page is clearly titled and easy to navigate.

8. As a site admin I can delete, edit and update the recipes on the website so that content is posted is relevant related to the website. 
   * Once a recipe or comment is posted the site adminstrator has access to delete and edit the content for the admin site. This ensures that the content posted is relevant to the website.

9. As a site admin I can approve comments on the website so that content is posted is relevant related to the website. 
   * As soon as a user posts a comment, the comment must be approved by the site administrator. This enables the site administrator to ensure that the content posted is relevant to the website. 

## Manual Testing
### Pep8 Validation
I tested the folowing files on Pep8 validator and they all passed.
  * views.py
  * urls.py
  * models.py
  * forms.py
  * admin.py
  * settings.py

I also tested the folowing templates on W3C validator and they all passed.
  * base.html
  * create_recipe.html
  * delete_recipe.html
  * edit_recipe.html
  * recipe_detail.html
  * recipe.html
  * index.html

### Search Engines
  * Google Chrome
  * Safari
  * Mozilla Firefox

### Devices
  * ASUS Chromebook Flip C434
  * Apple Macbook
  * Apple Ipad
  * Samsung Galaxy A50 
  * Iphone 12 

# Technologies Used<div id='id-technologies'>
  * HTML5
  * CSS3
  * Python
  * Heroku
  * Github
  * Gitpod
  * Django
  * Summernote
  * Cloudinary
  * Crispy Forms


# Bugs<div id='id-bugs'>

# Deployment<div id='id-deployment'>
This project was developed using a GitPod workspace. The code was committed to Git and pushed to GitHub using the terminal.

## Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

Create the Heroku App:

 * Select "Create new app" in Heroku.
 * Choose a name for your app and select the location.

Attach the Postgres database:

 * In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

Prepare the environment and settings.py file:

 * In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
 * In your GitPod workspace, create an env.py file in the main directory.
 * Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
 * Add the SECRET_KEY value to the Config Vars in Heroku.
 * Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
 * Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    In settings.py add the following sections:
    * Cloudinary to the INSTALLED_APPS list
    * STATICFILE_STORAGE
    * STATICFILES_DIRS
    * STATIC_ROOT
    * MEDIA_URL
    * DEFAULT_FILE_STORAGE
    * TEMPLATES_DIR
    * Update DIRS in TEMPLATES with TEMPLATES_DIR
    * Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

Store Static and Media files in Cloudinary and Deploy to Heroku:

* Create three directories in the main directory; media, storage, and templates.
* Create a file named "Procfile" in the main directory and add the following:
    * web: gunicorn project-name.WSGI
* Log in to Heroku using the terminal Heroku login -i.
* Then run the following command: heroku git:remote -a your_app_name_here and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
* SAfter linking your app to your workspace, you can then deploy new versions of the app by running the command git push heroku main and your app will be deployed to Heroku.

# Credits<div id='id-credits'>
## Content
  * I used the Code Institutes I think therefore I blog walkthrough project asa reference.
  * I also referenced the love maths project when transfering data from python to the spreadsheet in the update_worksheet function.
  * All the question that are used in the quiz were taken from [Open Trivia Database](https://opentdb.com/api_config.php)
  * [Am I Responsive](http://ami.responsivedesign.is/) was used for the header image that appears at the top of the read me file.
  * While researching the application that I would build I took inspiration from [Mike Dane](https://www.youtube.com/watch?v=SgQhwtIoQ7o&t=179s&ab_channel=MikeDane) and also from [Bro Code](https://www.youtube.com/watch?v=yriw5Zh406s&t=513s&ab_channel=BroCode). After viewing those videos this encouraged me to make a quiz game.

## Media
  * I used Bord bia recipes page for the images and recipe content tghat was used in the website.
  * The images used in the website were [Pexels]
  * I used [lucid chart](https://lucid.app/lucidchart/9331c746-149f-43ee-99b4-f5d069569366/edit?beaconFlowId=7EBCDF6C52EB4D67&invitationId=inv_2f7a6c93-0720-4f95-821a-a505c29dcaa4&page=NfXTJ6v46zip#) to create my flow chart.

## Acknowledgments<div id='id-acknowledgements'>
  * My mentor for the useful feedback direction and guidance he has provided since the beginning of the course.
  * The online tutors help and and advice when stuck on a problem with no one else to turn too.
  * The slack community who are very helpful.
  * The Code Institite course material.