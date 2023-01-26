# Happy Camper Campsite Review Website - Emma Scott
## Backend Development Milestone Project

![mockup image](/documentation/mockup.jpg)

## Introduction
Welcome to my Milestone Project 3. Happer Camper is a website that allows users to find campsites and share their own opinions of campsites. The site allows users to search for campsite reviews, submit their own reviews, and edit and delete reviews they have created. In addition, the admin account enables the admin user to create, edit and delete reviews and locations. Furthermore, users can submit a message to the site creator via the contact form, which uses the EmailJS API.

View the live project [here.](https://happy-camper.herokuapp.com/ "View the Live game here")


___

## Table of Contents

1. [User Experience (UX)](#ux)
    - [User Stories](#user-stories)
        - [Target Audience](#target-audience)
        - [First Time User Goals](#first-time-user-goals)
        - [Frequent User Goals](#frequent-user-goals)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
2. [Features](#features)
    - [Design](#design)
    - [Wireframes](#wireframes)
    - [Features](#features)
    - [Future Features](#future-features)
3. [Technologies](#technologies)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
4. [TEST.md](TEST.md)
5. [Deployment](#deployment)
    - [Heroku](#heroku)
6. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

___

## 1. User Experience (UX)

## User Stories

### Target Audience

The target audience for Happy Camper is anyone who likes camping and wants to share their experience of a campsite. It is also for people who want to find out what other people think of a campsite. Campsite owners might also use it to discover what visitors think of their site.

### First Time User Goals

As a first time user, I want to:
* be able to view the site clearly on any device.
* be able to easily navigate around the site.
* be able to search for campsite reviews.
* be able to sign up to the site quickly.
* be able to submit a review of a campsite.
* know that my reviews are protected from other people editing or deleting them.
* be able to send the site owner a message.
* be able to sign out of my account.


### Frequent User Goals

As a returning user, I want to 
* be able to view the site clearly on any device.
* be able to sign back into my account quickly.
* be able to search for campsite reviews.
* be able to view my reviews in one place.
* be able to edit my own reviews.
* be able to delete my own reviews.
* know that my reviews are protected from other people editing or deleting them.
* be able to sign out of my account.


### Administrator Goals

As an administrator of the site, I want to be able to:
* view the site clearly on any device.
* sign back into my account quickly.
* edit all reviews if necessary.
* delete all reviews if necessary.
* add new locations categories.
* edit locations categories.
* delete locations categories.
* receive email messages from site users.
* email messages from site users.


### Colour Scheme

[Coolors](https://coolors.co) was used to create a calming colour scheme that would not distract from the content.

![colour chart](/documentation/colours.jpg)


### Typography
The main font used for the Nav Bar heading is Poppins and the rest of the site uses Raleway. Both have Sans-Serif as a fall-back font and are easy to read.

[Back to top](#table-of-contents)
___

## 2. Features

### Design

Site Map 

![site map](/documentation/sitemap.jpg)

Database

The tables for the data have been created on MongoDB which is a non-relational database.

![flow chart](/documentation/flowchart.jpg)

### Wireframes

[Balsamiq](https://balsamiq.com/) was used to create wireframes of the design of the site for mobile phones, tablets and dekstop devices.

Home Page

![homepage](/documentation/wireframes/1home.png)

Sign Up page

![sign up page](/documentation/wireframes/2register.png)

Log in page

![log in page](/documentation/wireframes/3login.png)

Find a campsite page

![site page](/documentation/wireframes/4sites.png)

Submit a review

![review page](/documentation/wireframes/5review.png)

Profile Dashboard

![profile page](/documentation/wireframes/6profile.png)

Manage locations page

![manage locations](/documentation/wireframes/7locations.png)

### Features

#### Nav Bar
The nav bar is displayed on all pages and allows users to easily navigate the site. The nav bar has a brand name on the left to increase brand identity throughout the site. The brand name links back to the main page for ease of navigation. The links change colour when hovered over to signal to the user which link they have the mouse over. 
The nav bar presents differently for different user. Unregistered/Logged out users will only be able to see links for 'Home', 'Find campsite', 'Sign up', 'Log in' and 'Contact us'. 

![nav logged out](/documentation/site_images/nav_loggedout.jpg)

Once logged in, users will also see nav links for 'Add Review' and will no longer see 'Log In' or 'Register' links.

![nav logged in](/documentation/site_images/nav_loggedin.jpg)

Admin users can also see a link for 'Manage Locations' once logged in. 

![nav admin logged in](/documentation/site_images/nav_admin.jpg)

The nav bar is responsive and resizes when viewed on mobile devices as a side nav bar rather than a top one.

Logged out

![side nav logged out](/documentation/site_images/sidenav_loggedout.jpg)

Logged in

![side nav logged in](/documentation/site_images/sidenav_loggedin.jpg)

Admin

![side nav admin](/documentation/site_images/sidenav_admin.jpg)

#### Hero Image

The hero image is eye-catching and immediately conveys the context of the website. I decided to only have it display on the home page to enable a larger window for forms and reviews on subsequent pages to provide better user experience.

#### Footer

The footer contains social media links which could direct to Happy Camper social media pages in future. It also contains a copyright. Each link opens in a new browser window to allows user to keep the Happy Camper site open. The links all have an aria-label attribute to improve the experience for assistive technology users.

#### Flash Messages
Flash messages appear to provide the user with feedback on actions for example to confirm if a review has been added and to confirm when users have logged out. The style of the messages is similar to the rest of the site to provide good user experience.

#### Modals
Modals have been used on pages that involve the ability to delete something, for example on Manage Locations. The button on the page triggers the modal to open, and the delete functionality only works through the delete button on the modal. This is to reduce instances where people accidentally delete something and provides better user experience.

### Pages

The website consists of twelve pages that run from a base page:

* Home page
* Find Campsite page
* Campsite Review Page
* Sign Up page
* Log in page
* Contact page
* Profile page
* Add a review page
* Edit a review page
* Manage Locations page
* Add a location page
* Edit a location page
* 404 error page


All users can open the following pages: 

#### Home Page

The home page contains a search bar for ease of use, to allow users to begin searching for campsite reviews immediately. It also contains three card panels which convey the main features of the site - to search for a site review, submit a site review and (in future) save their favourite site reviews. It has deliberately been kept minimilistic to enable users to easily navigate the site.

![home](/documentation/site_images/home_page.jpg)

#### Find Campsite Page

The Find Campsite page also contains a search bar, again for ease of use. Site reviews are displayed in rows which are responsive depending on the device size. The card panels contain the image included by the users from the image URL or, if this is not included by the user, a placeholder image is displayed.  The cards also display the location and the username of the reviewer. Users can easily open the full review from the View button.

![find](/documentation/site_images/find_campsite.jpg)

#### Campsite Review Page

This page enables users to read the full campsite review. It includes the image again and includes the values of the keys - site name, site location, site review, image URL, members only (toggle), date visited and reviewed by. The review panel includes a back button which takes them back to the Find Campsite page, again for ease of navigation around the website, without the need to use the browswer's back button.

![review](/documentation/site_images/review.jpg)

#### Contact Page

Any user can acces the contact page and complete the contact form. This was deliberately chosen so that anyone experiencing a problem or with a question could contact the site administration. The form connects to the EmailJS API to enable the form contents to be emailed to the site admin. An auto-response has been set up to reply to the email address on the form to acknowledge the user's query. The autoresponse includes the user's name in the message.

![contact](/documentation/site_images/contact.jpg)

#### Sign Up Page

The Sign Up page comprises of a form for users to complete to create an account. The fields have icons to easily identify each field and to improve the visual effect of the form panel. Users are required to complete each field and are unable to submit the form if fields don't follow a specified format. Users are unable to create a username that already exists as this is checked against the database. Users are prompted 'Username unavailable. Please try a different username.' There is also a link to the Log in page with the prompt 'Already registered?' to avoid multiple accounts being created. The First Name and Last Name fields are listed side by side on larger displays and in blocks on smaller screen sizes to provide ease of accessibility.

![sign up](/documentation/site_images/signup.jpg)

#### Log In Page

The Log In page again is a simple form that requires both fields to be completed. This is then checked against the database and the user is then redirected to their profile page if the account matches the database, or if it does not match then a flash message is displayed that the username or password is invalid. This wording was deliberately chosen to increase security as the user will be unsure which field is incorrect thus making it harder to hack.

![login](/documentation/site_images/login.jpg)


Users who are logged in can access the following pages:

#### Profile Page

The profile page displays the sites that the user has reviewed. The card panels include three buttons: View, Delete and Edit. The Delete button triggers the modal to confirm whether the user really wants to delete the review. The Edit button takes the user to the site review page.

![profile](/documentation/site_images/profile.jpg)

#### Edit Review Page

This page displays the current site review using the site_id value to populate the fields with the values. Users can then edit the fields and have the option to either save their edited review or cancel and return to the Find Campsite page. Again, parameters have been set for the field values so they are required. The exception the this is the image URL which has been made optional as I felt some users might not want to include this information. 

![edit review](/documentation/site_images/editreview.jpg)

#### Add Review Page

Signed in users can complete the form to submit a new campsite review. The form includes the keys of site name, site location, site review, image URL, members only (toggle) and and visit date which is a Materialize date picker for ease of entry and uniformity of values in the database. All values are required exampt for image URL, as previously mentioned. The form can then be submitted and stored in the database, or the Cancel button returns the user to the Find Campsite page. This all enables ease of navigation and good user experience.

![add review](/documentation/site_images/add_review.jpg)

#### Log Out Link

When users click on the Log Out link their session ends and they are redirected to the home page. A flash message gives confirmation that they have been logged out successfully.

![log out](/documentation/site_images/logout.jpg)


The following pages are only accessible to Admin users:

#### Manage Locations Page

The locations in the database are displayed on Materialize card panels that are responsive based on device size for clear display and good user experience. The card panels contain two buttons: edit and delete. The delete button triggers the modal to confirm the user wants to delete the location. The edit button redirects the user to the edit page. The buttons have been designed to echo the site colours providing brand identity.  

![manage locations](/documentation/site_images/manage_locations.jpg)

#### Edit Locations Page

The edit page contains a very simple form which is prepopulated with the location that the user has selected to edit. Upon clicking the edit location button the user is redirected back to the Manage Locations page. A cancel button is also provided if the user changes their mind to aviod them needing to user the browser's back button.

![edit locations](/documentation/site_images/edit_location.jpg)

#### Add Locations Page

Again, this page contains a very simple form. The user is required to enter a location name that is longer than three letters. Upon clicking the Add location button the user is redirected back to the Manage Locations page. Again, the cancel button is also provided if the user changes their mind to aviod them needing to user the browser's back button.

![add locations](/documentation/site_images/add_location.jpg)

#### 404 Error Page

A custom 404 error page has been included to allow users to navigate back to the home page easily as it contains a link which changes colour when hovered over. This enables users to easily naviate the site and gives immediate user feedback.

![404](/documentation/site_images/404.jpg)

### Future Features
Ideas for future implementation include:

 - the functionality for a user to save a site as their 'favourite' and have it appear on their profile page.
 - the ability for users to change their password and a function to accomodate forgotten passwords.
 - the option for a user to delete their account.
 - inclusion of an API for users to view the campsite location such as Google Maps.
 - the option to select campsite features to broaden the search parameters, for example check boxes for electric hookup, kids play area, toilet block etc so users could then filter the sites by these values. 


[Back to top](#table-of-contents)
___

## 3. Technologies

### Languages

HTML, CSS, JavaScript & Python

### Frameworks, Libraries and Programs Used

MongoDB Atlas - database server, noSQL.
Flask - micro web framework written in Python.
mongoDB shell - command shell.
dnspython - DNS toolkit for Python.
PyMongo - Python-Mongo library. 
Pip - for installing Python packages.
Jinga - to generate markup as well as source code.
Balsamiq - to produce wireframes.
Git - for version control.
Github - to save files for the website.
Google Fonts - to import fonts.
TinyPNG - to compress files.
LucidCharts - to produce the site flow chart.


[Back to top](#table-of-contents)
___

## 4. Testing

A seperate [TEST.md](TEST.md) file has been created for the documentation of testing.
[Back to top](#table-of-contents)
___

## 5. Deployment
### Heroku
[Back to top](#table-of-contents)
___

## 6. Credits
### Content

### Media
[websitemockupgenerator](https://websitemockupgenerator.com/) for creating the multi-device mockup.  
### Acknowledgements

[Back to top](#table-of-contents)
___
