# Easy Recipe

The aim of the project was to build a website using the Django framework. This is my fourth portfolio project. I chose to build a recipe website as I felt I would be able to design a high-quality website and could implement the features that I wanted to. I created a website called Easy Recipe. This website was designed to be a simple and user friendly website. The website's objective is to create a database of recipes that can be shared among users. The website is aimed at anyone who loves cooking and wants to learn about and share recipes. The website can also be useful for someone who is just learning how to cook.&nbsp;

![amiresponsive](https://user-images.githubusercontent.com/91072896/176175582-3c050314-42f4-4145-b0dc-b92506eacc34.png)


# Table of Contents
1. [UX](#id-ux)
2. [Structure](#id-structure)
    * [Wireframe](#id-wireframe)
    * [Database Schema](#id-Database-Schema)
3. [Features](#id-features)
    * [Navigation-bar ](#id-nav)
    * [Features left to implement](#id-implement)
4. [Testing](#id-testing) 
5. [Bugs](#id-bugs) 
6. [Technologies Used](#id-technologies)
7. [Deployment](#id-deployment)
8. [Credits](#id-deployment)
9. [Acknowledgements](#id-technologies)





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

### Wireframe <div id='wireframe'>

![Screenshot 2022-06-28 13 32 24](https://user-images.githubusercontent.com/91072896/176179862-bd053d41-5468-4798-a442-8f3e70aa9b7b.png)
![Screenshot 2022-06-28 13 32 34](https://user-images.githubusercontent.com/91072896/176179861-84dd805a-7de7-4aff-b78a-1a57b6718b62.png)
![Screenshot 2022-06-28 13 33 01](https://user-images.githubusercontent.com/91072896/176179857-1b7a4fa1-45fa-4818-9e41-76d3a05577ac.png)
![Screenshot 2022-06-28 13 33 11](https://user-images.githubusercontent.com/91072896/176179850-f2b2313f-f069-4086-a6e0-cdfcb3a3b951.png)
![Screenshot 2022-06-28 13 33 31](https://user-images.githubusercontent.com/91072896/176179841-c1d4918d-13d9-4e27-b39c-8458644fb1d2.png)
![Screenshot 2022-06-28 13 33 18](https://user-images.githubusercontent.com/91072896/176179849-87a2ad60-fd35-4a12-994f-0f283c3ce4f2.png)

# Database Schema<div id='Database-Schema'>
![Database Schema](https://user-images.githubusercontent.com/91072896/176322366-e91262a5-08d5-4414-a403-23a1e3a8fe61.png)


# Features<div id='id-features'>

## Navigation-bar(#id-nav)

The navigation bar is at the top of the website. This includes the website name which appears at the left of the nav bar. It also includes links to different pages that the user can visit. The navbar is simple and I believe that it is easy for the user to use. The navbar links change format to hamburger format if the website is viewed on smaller devices. The text is easy to read on the offwhite background. Images of each navigation bar are provided below.&nbsp;

![navbar](https://user-images.githubusercontent.com/91072896/176243638-21130cfe-0e03-4159-accd-3332882433ff.png)
![navbar1](https://user-images.githubusercontent.com/91072896/176243630-737ead99-6d3c-4564-9e33-45aa62b3d15c.png)

## Banner and about sections 

The banner image appears under the navbar with some text that transitions. The about section of the website discusses the website's purpose and goal in a paragraph following the banner.&nbsp;

![Banner](https://user-images.githubusercontent.com/91072896/176245284-e4932381-1633-4bf8-a38d-88f2d2265b15.png)

This section is about the websites purpose.&nbsp;

![WWD](https://user-images.githubusercontent.com/91072896/176274425-11370ef5-3b5c-41cb-ba2b-f4d6b1ff2a5a.png)

## How it works

At the end of the page there are three linked images. Above the images is a heading explaining how it works. This is to show the user with the linked images, what they need to do to start using the website. The first image is the registration page, as this is the first step the user undertakes. The next image is creating a recipe and the final image is the recipe link. This communicates to the users that they first have to sign up to the website and then they can create and view recipes.&nbsp;

![HIW](https://user-images.githubusercontent.com/91072896/176275423-4611f935-1c64-4ea9-b7da-88f7e3d28a45.png)

## Recipes 

The recipes page is where the user's recipes are displayed. Once a recipe is created on the create recipe page the user can view it on the recipes page. On the recipes page you can find limited information, cook time, prep time, and the number of servings per recipe. However the user can see more details about each recipe by clicking on recipetails. The recipe page is paginated and can hold six recipes per page.&nbsp;

![Recipes](https://user-images.githubusercontent.com/91072896/176276742-9fc44f5a-ca3b-4db1-b886-beab396bff72.png)

## Edit/delete recipe.  

This is located on the recipe detail page. This can only be actioned if the user was the one who had created the recipe they cannot edit or delete recipes left by other users. If they are not authorized the option will not appear on the page for that user. If the user wants to edit the page they will be brought to a form where they can change any of the information, they put in. If they choose delete, they will be brought to another page to confirm that they want to delete the recipe.&nbsp;

![edit delete](https://user-images.githubusercontent.com/91072896/176322923-dc4883d8-834a-4e8e-8439-11f578d6e64e.png)

## Comments

You can find the comments section on the recipe detail page below the instructions for the recipe. A user can post a comment below, but must be authorized to do so. Those who do not register can see comments left below, but will not be able to post a comment until registering an account.&nbsp;

![comments](https://user-images.githubusercontent.com/91072896/176325102-949b646e-6ba5-4583-ac1b-fc2fe053488b.png)

# Testing
## User Stories

### As a User 

1. As a user I can register an account so that I can post comments, recipes and interact with users posts.
   * Users can register an account by going to the sign up page and once this process has been complete they can the interact with other users.

2. As a user I can post and read comments so that So I can give feedback and read feedback from others. 
    * Users that register an account through the sign up page can visit the view_recipe page and can commentg on recipes

3. As a user I can access the recipe page so that I can find recipes that I am interested in using. 
4. As a site admin I can approve comments on the website so that content is posted is relevant related to the website.                                                         									
5. As a user I can I can upload images with the recipes so that it will give users a visual representation of the 
recipe. 
6. As a user I can log out of my account when I'm done using the website. so that if I used a public computer my account is safe. 
    * The user can create an account with a unique pasword and id this will ensure that the users information is safe and if they are useing a 
      public computer there is no chance that anyone can acess his/her account

7. As a user I can easily navigate around the website so that I can view the information that I want. 

### As a Site admin

8. As a site admin I can delete, edit and update the recipes on the website so that content is posted is relevant related to the website. 
9. As a site admin I can approve comments on the website so that content is posted is relevant related to the website. 

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



# Deployment<div id='deployment'>
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
