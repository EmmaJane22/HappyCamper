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
#### Hero Image
#### Nav Bar
The nav bar is displayed on all pages and allows users to easily navigate the site. The nav bar has a brand name on the left to increase brand identity throughout the site. 
Unregistered/Logged out users will only be able to see links for 'Home', 'Find campsite', 'Sign up', 'Log in' and 'Contact us'.

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

#### Footer

### Future Features

[Back to top](#table-of-contents)
___

## 3. Technologies
### Languages
### Frameworks, Libraries and Programs Used
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
