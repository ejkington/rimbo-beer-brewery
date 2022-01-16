# Rimbo Beer Brewery events

[Link to Live Website](#)

[GitHub Repo](#)


### PIC OF RESPONSIVE SITE


## About 

Rimbo beer brewery is a business concept created for my MS4 project with Code Institute.

Rimbo beer brewery is a business dedicated to brewing the best craft beer in the north. Rimbo beer brewery offers both craft made beers and brewery tours  
Currently they do not offer sales directly from the website.
but they offer events created by the brewery

Rimbo beer brewery would need to have a website to tell users a little about the business, show potential clients what services they offer and showcase some of their current or existing work. Rimbo beer brewery is a small company with a small range of website needs. there is scope for the business to grow. As the business grows the website can be adapted to the growing business and additional features implemented.
Events booking is added for user to book events created by the brewery. and registration is used to validate costumers to book events, this will in the future be used to 
have users book and order products from the site, and to store information about the user


## User Experience (UX)

## Strategy
### User Stories  

#### Reasons a user may visit the website
* A user looking for a craft made beer locally.
* A user looking to ordering beer too their resturant or bar.
* A user doing research on what we offer.
* A user interested in beer and beer making.
* A user wants to view and book an event held by the brewery

#### Reasons for the website
* Increase clients
* Showcase work
* Provide a way for new and existing clients to contact us.
* Getting customers to the events

## Scope
#### What a user may expect
* Easy to navigate website 
* Good presentation and visually appealing regardless of screen size.
* Links and functions work as expected.
* Information about what Rimbo beer brewery does.
* A way to get in contact with Rimbo beer brewery.
* New events that can be booked

#### What a user may want 
* To be able to find links to social media pages.
* To see examples of previous work carried out.
* To be able to chat with someone online.
* How it works - from start to finish.


#### As a developer / business I expect
* To provide information about Rimbo beer brewery.
* To provide an easy way for new and existing clients to contact us.
* To provide an easy to navigate website with links that work as expected.
* To encourage clients to contact us. 
* Customers to book events 


## Structure
The website will consist of 4 separate pages, not including the register/logg in and logg out pages
* A home page with the brewery moto and appealing pictures of beer styles.
* A our beers page showing what kind of beers the brewery makes, and what to expect when tasting it.
* A events page and appealing pictures of the event
* A events detail page, showing the details of the event clicked
* A Form too book an event


## Features across all pages.

### Navigation Bar

![navbar](https://github.com/ejkington/rimbo-beer-brewery/blob/93ec6f9f27101f70fd435db49048d216c474eb58/Readme/Images/Navbar.png)

The navigation bar.
The navigation links directs the user to the correct page of the website.
When the rimbo beer brewery logo is pressed it takes the user to the main page.
On larger screens the navigation bar is horizontal and too the left. on smaller screens it displays as a hamburger button with a list of all pages.

### Responsiveness
The page is scaled up and down for different screen resolutions to help the content stay neat. This has been done using of media queries.


### Accessibility
All images and navigation have an alt attributes. This is to make the site easier to use for people with visual impairments by allowing them to navigate the site easily. There is high contrast used throughout the design. Header elements have been used in sequence so that the site makes semantic sense to screen readers. Links are consistent when hovered over. I have also set the font to rem so that if someone has their font settings higher for visibility the font size will increase accordingly.


### Footer

![footer](https://github.com/ejkington/rimbo-beer-brewery/blob/8e365d8a232e409f71d2a2dc00467f3ff66436f9/Readme/Images/footer.png)

The footer consists of social media links and will open in a new tab.


### Meta data
I have included descriptions, author, and keywords into the head element to increase traffic to the website. I have also labelled each page differently so that if the user has multiple tabs open it is easy to recognise each tab.


## Features specific to page

###### Homepage.

![index1](https://github.com/ejkington/rimbo-beer-brewery/blob/8e365d8a232e409f71d2a2dc00467f3ff66436f9/Readme/Images/index1.png)
![index2](https://github.com/ejkington/rimbo-beer-brewery/blob/8e365d8a232e409f71d2a2dc00467f3ff66436f9/Readme/Images/index2.png)

A image charrosel pictures from the brewery.
The brewery motto.
Text that shows the love for beer and beer making above footer

###### Our beers.

### PIC OF OURBEERS PAGE

Showcasing pictures of the beers.
The names of the different beers.
and a taste review when clicked used jQuery.

###### Events.

### PIC OF EVENS PAGE

Showing the current events that the brewery has and when clicked redirects user to a detailed page of the event.
paginated by 6


###### Events Detail.

### PIC OF EVENT DETAILS PAGE

* Showing the details of the event clicked.
* If not logged in a text is displaying prompting the user to logg in or register.
* Booking form if the user wants to book an event all fields is required.
* Text diplaying "your booking is waiting approval if form is valid.
* Submit button in the form

### Logg in and Out

### PIC OF LOGIN PAGE

###### Login / Logout

Allauth is used to fast and easy rendering of user regristraion, login and logout
Once registered a user can sign in and will have access to extra functionality, namely :

can book events

To sign in the user must provide a) a registered username and b) the password for the username


User Sign out

### PIC OF LOGOUT
A signed in user can sign out by clicking on the Sign out link on the navigation bar. The user simply needs to confirm the action by clicking on the Sign out button on the page. and an message is displayed that the user has signed out.

## Admin page

#### PIC OF ADMINS PAGE

* This page is for the admin to manage the bookings made by user and to create and manage events
* Can be used to approve and disapprov bookings
* Can be used to see how many users that have regristred too the site


## Technologies Used 

* HTML5 - Mark-up language using semantic structure.
* CCS3 - Cascading style sheet used to style.
* jQuery - To get logic in the our beers page
* Django/Python - For easy and fast development 
* Gitpod.io - for writing the code. Using the command line for committing and pushing to Git Hub
* GitHub - Used to host repository
* Heroku - Too host the page
* GIT - for version control of the project. 

## Design, Librarys, Frameworks

* [Google fonts](https://fonts.google.com/) - For styling the typography (roboto)
* [Font Awesome](https://fontawesome.com/) - for social media icons
* [Beautifer](https://beautifier.io/) - Allowing me beautify my code.
* [Bootstrap](https://getbootstrap.com/) - For fast and easy css styling
* [jQuery](https://jquery.com/) - For easy and nice looking animation
* [Django](https://www.djangoproject.com/) - Framework
* [https://gunicorn.org/] - was used as the Web Server to run Django on Heroku
* [https://pypi.org/project/dj-database-url/] - library used to allow database urls to connect to the postgres db
* [https://pypi.org/project/psycopg2/] - database adapter used to support the connection to the postgres db
* [https://cloudinary.com/] - used to store the images used by the application
* [https://pypi.org/project/django-summernote/] - used to provide WYSIWYG editing on the event editing screen
* [https://django-allauth.readthedocs.io/en/latest/index.html] - used for account registration and authentication
* [https://django-crispy-forms.readthedocs.io/en/latest/] - used to simplify form rendering
* [https://jquery.com/] - used to fade out alert messages and displaying text in ourbeers page


## Testing

### Validator Testing

* HTML Validating

* CSS Validating

* JavaScript Validation

* Python Validation


### Automated Testing

#### Jest

#### Jest results 

#PIC OF JEST TEST


# Browser Compatibility

* Chrome DevTools was used to test the responsiveness of the application on different screen sizes. In addition, testing has been carried out on the following browsers :
Google Chrome version 9.0.4606.81 (64-bit)
Firefox version 93.0 (64-bit)
Microsoft Edge 94.0.992.38 (64-bit)

# Deployment 

Deployment
Detailed below are instructions on how to clone this project repository and the steps to configure and deploy the application. Code Institute also provides a summary of similar process steps here : CI Cheat Sheet

How to Clone the Repository
Create Application and Postgres DB on Heroku
Configure Cloudinary to host images used by the application
Connect the Heroku app to the GitHub repository
Executing automated tests
Final Deployment steps
How to Clone the Repository
Go to the https://github.com/ejkington/rimbo-beer-brewery repository on GitHub

Click the "Code" button to the right of the screen, click HTTPs and copy the link there

Open a GitBash terminal and navigate to the directory where you want to locate the clone

On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process

To install the packages required by the application use the command : pip install -r requirements.txt

When developing and running the application locally set DEBUG=True in the settings.py file

Changes made to the local clone can be pushed back to the repository using the following commands :

git add filenames (or "." to add all changed files)
git commit -m "text message describing changes"
git push
N.B. Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku

Create Application and Postgres DB on Heroku
Log in to Heroku at https://heroku.com - create an account if needed.

From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.

On the Create New App page, enter a unique name for the application and select region. Then click Create app.

On the Application Configuration page for the new app, click on the Resources tab.

In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list - click the "Submit Order Form" button on the pop-up dialog.

Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up.

Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.

Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.

The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

SECRET_KEY = os.environ.get('SECRET_KEY')

In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate

Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt

Commit and push any local changes to GitHub.

In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py

Configure Cloudinary to host images used by the application
Log in to Cloudinary - create an account if needed. To create the account provide your name, email and set up a password. For "primary interest" you can choose "Programmable Media for image and video API". Click "Create Account" and you will be sent an email to verify your account and bring you to the dashboard.
From the dashboard, copy the "API Environment variable" value by clicking on the "Copy to clipboard" link.
Log in to Heroku and go to the Application Configuration page for the application. Click on Settings and click on the "Reveal Config Vars" button.
Add a new Config Var called CLOUDINARY_URL and assign it the value copied from the Cloudinary dashboard, but remove the "CLOUDINARY_URL=" at the beginning of the string.
In order to be able to run the application on localhost, also add the CLOUDINARY_URL environment variable and value to env.py
Connect the Heroku app to the GitHub repository
Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://github.com/ejkington/rimbo-beer-brewery) and click on Connect to link up the Heroku app to the GitHub repository code.
Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
The application can be run from the Application Configuration page by clicking on the Open App button.
The live link for this project is (#HEROKU)

#Final Deployment steps

Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows :

Set DEBUG flag to False in settings.py
Ensure this line exists in settings.py to make summernote work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt
Push files to GitHub
In the Heroku Config Vars for the application delete this environment variable : DISABLE_COLLECTSTATIC
On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch


# Credits
Code
Much of the coding and testing relies heavily on information in the "Hello Django" and "I Think Therefore I Blog" walkthroughs in the Code Institue Full Stack Frameworks module.

[https://getbootstrap.com/docs/4.0/components/carousel/] - Information on how to implement charosel images
[https://www.w3.org/]
[https://getbootstrap.com/]
[https://docs.djangoproject.com/en/4.0/]
The Slack comunity
Tutor support
Brian macharia - my mentor
Google - What would i do without it


## Media

All pictures for the site was taken from [https://unsplash.com/]
The logo in the nav bar was created on [https://www.logomaker.com/]

#Acknowledgments

Thank you to my mentor Brian Macharia for his continuing help and feedback. His advice and tips have been very beneficial, especially in the area of coding standards and best practice.
My friends and family that suports me the best they can


