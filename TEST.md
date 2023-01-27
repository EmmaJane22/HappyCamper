# Happy Camper Campsite Review Website - Emma Scott
## Backend Development Milestone Project

## Testing

## Table of Contents

4. [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Testing User Stories](#testing-user-stories)
    - [Manual Testing](#manual-testing)
    - [Bugs & Fixes](#bugs-&-fixes)

## Code Validation

### W3C Markup Validator

All .html files were checked with the [W3C HTML Validator](https://validator.w3.org/) using the 'direct input' method.
These checks showed three pages with a missing closing div tag where I had copied and pasted the same snippet of code. This was fixed by moving the closing div tag from after the endif to the end of each card div.

![W3C image](/documentation/profile_div.jpg)

The validator also highlighted missing head elements, illegal characters, missing lang attributes and no-space characters however these are due to use Jinga templating (see example below).

![W3C HTML image](/documentation/index_error.jpg)


### CSS Validator

All CSS code was checked with the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) using the 'direct input' method. No errors found.

![W3C CSS image](/documentation/css.jpg)


### JSHint Validator

This showed two warnings linked to the Materialize script on script.js

![jshint error image](/documentation/jshint_error.jpg)

It also showed two errors with two variables being used to call functions in sendEmail.js

![jshint email error image](/documentation/sendEmail_error.jpg)


### PEP8 Validation

PEP8Ci was used to validate the python code used in the app.py file. No errors were linted.

![PEP8CI image](/documentation/pep8_app_clear.jpg)


## Lighthouse

Responsivity tests were carried out using Google Chrome DevTools throughout the project.
The site has been run through the Lighthouse test on Google Developer Tools and achieved the following results:

Desktop - Home Page <br>
![desktop home](/documentation/index.jpg)

Mobile - Home Page <br>
![mobile home](/documentation/mobile_index.jpg)

The first test showed that there wasn't sufficient contrast between the text colour and the background colour so this was changed to the darker colour of #263238.

It also identified that the footer text was also not high enough contrast so the styling on that was increased to a h6 so that it was more legible.

Performance on some pages was lower than hoped which seemed to be affected by the external URLs for the site reviews.


___

## Manual Testing

* The site was tested on Google Chrome and Microsoft Edge for desktop and Chrome on mobile and tablet.

* It was tested using Google Developer Tools on the following devices:
    * iPhone SE
    * iPhone XR
    * Pixel 5
    * Samsung Galaxy S8+
    * iPad Air
    * iPad mini

* The site was responsive on all browsers and all devices.

___

## Testing User Stories

As a first time user, I want to:
* be able to view the site clearly on any device. 
    - testers reported that the site was responsive on their devices.
* be able to easily navigate around the site.
    - Friends and family reported that the site was easy to navigate around.
* be able to search for campsite reviews.
    - All users can access the search tool regardless of whether they have an account. 
* be able to sign up to the site quickly.
    - testers reported that they found signing up easy and quick.
* be able to submit a review of a campsite.
    - all testers reported being able to submit a review easily.
* know that my reviews are protected from other people editing or deleting them.
    - testing showed that reviews could not be deleted by different users.
* be able to send the site owner a message.
    - the contact form sends emails and the user received the auto-reply email back.
* be able to sign out of my account.
    - testers confirmed they could sign out.


### Frequent User Goals

As a returning user, I want to 
* be able to view the site clearly on any device.
    - testers reported that the site was responsive on their devices.
* be able to sign back into my account quickly.
    - all users confirmed they could sign back in quickly. Some users suggested the ability to reset their password, which would be implemented in future.
* be able to search for campsite reviews.
    - all testers were able to search for campsites based on their key words.
* be able to view my reviews in one place.
    - the profile page was accurate for all testers.
* be able to edit my own reviews.
    - testers confirmed they could edit their reviews successfully.
* be able to delete my own reviews.
    - testers confirmed they could delete their own reviews and not those from others.
* know that my reviews are protected from other people editing or deleting them.
    - testers confirmed their reviews had not been deleted by others.
* be able to sign out of my account.
    - Testers confirmed they could sign out successfully.


### Administrator Goals

As an administrator of the site, I want to be able to:
* view the site clearly on any device.
    - testers reported that the site was responsive on their devices.
* sign back into my account quickly.
    - admin testers confirmed they could sign back in quickly.
* edit all reviews if necessary.
    - admin testers confirmed they could edit reviews.
* delete all reviews if necessary.
    - admin testers confirmed they could delete all reviews individually.
* add new locations categories.
    - admin testers confirmed they could add new locations.
* edit locations categories.
    - admin testers confirmed they could edit locations.
* delete locations categories.
    - admin testers confirmed they could delete reviews.
* receive email messages from site users.
    - admin testers confirmed they could receive messages via the form.

___

## Manual Testing on Mobile and Desktop Devices

### Nav Bar

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Happy Camper Logo | redirect user to home page when clicked | clicked title | redirected to home page | pass |
| Home page link | redirect user to home page when clicked | clicked link | redirected to home page | pass |
| Find Campsite link | redirect user to find campsite page when clicked | clicked link | redirected to Find Campsite page | pass |
| contact us link | redirect user to contact page when clicked | clicked link | redirected to contact page | pass |
| log in link | redirect user to log in page when clicked | clicked link | redirected to log in page | pass |
| sign up link | redirect user to sign up page when clicked | clicked link | redirected to sign up page | pass |
| log out link | log user out of session and redirect user to home page when clicked | clicked link | user logged out of session and redirected to home page | pass |
| profile link | redirect user to profile page when clicked | clicked link | redirected to profile page | pass |
| Add Review link | redirect user to add review page when clicked | clicked link | redirected to add review page | pass |
| manage locations link | redirect user to manage locations page when clicked | clicked link | redirected to manage locations page | pass |

### Footer

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Social media links | link open browser window and go to correct site when clicked | clicked link | New browser window opens for each link clicked. Links redirect tot he correct sites. | pass |

### Hero Image

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Hero image | Hero image resizes on mobile devices | opened site on mobile device | hero image resizes as expected | pass |


### Home Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Search bar | search is performed when user enters a search term. | searched for woodland, chocolate, space, superhero, tent | The search returned sites containing the search term. | pass |
| Search bar | Message appears to inform user there are no search results when search is performed without a matching search term. | searched for woodland, chocolate, space, superhero, tent | The search returned the error message. | pass |
| search button | Performs search when button is clicked. | clicked button | Search successfully performed | pass |
| links for search | redirect to Find a campsite page | clicked link | redirected to Find a campsite page | pass |
| links for submit | redirect to Add Review page | clicked link | redirected to Add Review page | pass |
| links for search, submit & save | hyperlink hover changes colour | hovered over link | link changed colour | pass |


### Find Campsite Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Search bar | search is performed when user enters a search term. | searched for woodland, chocolate, space, superhero, tent | The search returned sites containing the search term. | pass |
| Search bar | Message appears to inform user there are no search results when search is performed without a matching search term. | searched for woodland, chocolate, space, superhero, tent | The search returned the error message. | pass |
| search button | Performs search when button is clicked. | clicked button | Search successfully performed | pass |
| Image | displayed from url | visited page | image displayed | pass |
| Image | displayed from static if missing url | visited page | image displayed | pass |
| View button | redirects to site id review | clicked button | redirects to correct site id review | pass |
| Edit button | redirects to edit site id review | clicked button | redirects to correct site id review to edit | pass |
| Delete button | redirects to delete modal | clicked button | redirects to delete modal | pass |

### Profile Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Users site reviews | Profile page displays all of the user's reviews | clicked on Profile hyperlink on Nav Bar | redirected to Profile page, review cards displayed  | pass |
| Username  | Username displays in title  | logged in and went to Profile page | Username displayed in title | pass |
| View button | redirects to site id review | clicked button | redirects to correct site id review | pass |
| Edit button | redirects to edit site id review | clicked button | redirects to correct site id review to edit | pass |
| Delete button | redirects to delete modal | clicked button | redirects to delete modal | pass |


### View Review Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Image | displayed from url | visited page | image displayed | pass |
| Edit button | redirects to edit site id page | clicked button | redirects to correct site id to edit | pass |
| Delete button | redirects to delete modal | clicked button | redirects to delete modal | pass |
| buttons | hyperlink hover changes colour | hovered over link | link changed colour | pass |

### Add Review Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Access to page | page should not display unless user is logged in | stayed logged out | hyperlink hidden | pass |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Location input | dropdown list should appear | clicked dropdown carrat | location drop down appeared | pass |
| Date input | Should open date picker | clicked on input field | datepicker appeared | pass |
| Members only toggle | toggle switch should be able to set to on or off | clicked toggle | toggle switch can be turned on and off | pass |
| cancel button | redirect to Find Campsite page | clicked cancel button | redirected to Find Campsite page | pass |
| Add review button | add review to database | clicked add button | review added to database | pass |


### Manage Location Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Access to page | page should not display unless Admin user logged in | logged in as non-admin user | hyperlink hidden | pass |
| Add location button | redirect to Add Location page | clicked add button | redirected to Add Location page | pass |
| Edit button | redirects to edit location id page | clicked button | redirects to correct location id to edit | pass |
| Delete button | redirects to delete modal | clicked button | redirects to delete modal | pass |
| buttons | hyperlink hover changes colour | hovered over link | link changed colour | pass |

### Add Location Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Access to page | page should not display unless Admin user logged in | logged in as non-admin user | hyperlink hidden | pass |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| cancel button | redirect to Manage Locations page | clicked cancel button | redirected to Manage Locations page | pass |
| Add location button | add location to database | clicked add button | location added to database | pass |
| buttons | hyperlink hover changes colour | hovered over link | link changed colour | pass |

### Edit Location Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Access to page | page should not display unless Admin user logged in | logged in as non-admin user | hyperlink hidden | pass |
| Form input | Should be prepopulated correctly for location id | checked prepopulated correctly | Correct location prepopulated | pass |
| cancel button | redirect to Manage Locations page | clicked cancel button | redirected to Manage Locations page | pass |
| Edit location button | append location name to database | clicked edit button | location appended to database | pass |
| buttons | hyperlink hover changes colour | hovered over link | link changed colour | pass |

### Sign Up Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Form input - username & password | The field should be between 5-15 characters long  | enter less than 5 characters | tooltip indicates the field is invalid | pass |
| Form input - username & password | The field should be between 5-15 characters long  | enter more than 5 characters | tooltip indicates the field is invalid | pass |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Invalid username | Error message should display if username is already registered  | user pre-registered username | error message appeared | pass |
| Sign Up button | add user to database | clicked Sign Up button | user added to database | pass |
| Logn In hyperlink | redirect user to Log In page | clicked hyperlink | redirected to Log In page | pass |
| buttons | hyperlink hover changes colour | hovered over link | link changed colour | pass |

### Log In Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Log In button | add user to session and redirects to Profile page. Flash message to welcome user | clicked Login button | user redirected to Profile page. Flash welcome message displayed | pass |
| Sign Up hyperlink | redirect user to Sign Up page | clicked hyperlink | redirected to Sign Up page | pass |
| buttons | hyperlink hover changes colour | hovered over link | link changed colour | pass |

### Contact Us Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Send button | Should send the form to the admin email account | completed form and clicked send button, checked admin mailbox | Email received containing information from form | pass |
| auto-reply email | User completing the form should receive the auto-reply email | users checked their mailbox | Auto-reply had been received. | pass |

### Delete Modal

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| delete review | review should be deleted from database | clicked delete | review deleted from database | pass |
| cancel button | redirect to Find a Campsite page | clicked cancel button | redirected to Find a campsite page | pass |
| delete location | location should be deleted from database | clicked delete | location deleted from database | pass |
| cancel button | redirect to Manage Locations page | clicked cancel button | redirected to Manage Locations page | pass |

### 404 Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| display page | page should display when an error is made with site url | removed character from site url | 404 page displayed | pass |
| home hyperlink | redirect user to Home page | clicked hyperlink | redirected to Home page | pass |
| hyperlink | hyperlink hover changes colour | hovered over link | link changed colour | pass |


___

## Bugs & Fixes

| Bug | How I solved the issue |
| :--- | :--- |
| Werzberg error showed Log out link not working  | On inspection the redirect in app.py was set to login rather than landing_page. Changed the redirect address. |
| Contact form wasn’t sending email |  Wrong setting saved for service, changed to correct service id. |
| Linting error for app.py - PEP8 warning: Missing two blank lines | Added additional blank lines. |
| Within manage locations html, when you click on delete modal, it does not delete the selected location. | By using Dev Tools inspect and running the site in debug mode, I realised that all the modals had the same ID. This meant that when delete was pressed, regardless of which location was selected, the first location in the database was being deleted as the wrong modal was being displayed, which meant the delete link in that modal had the wrong location ID. On closer inspection the same was happening with the site modal. To resolve this, I appended the location id/site id onto the modal element id. |
| Edit review page displaying missing image icon in top left corner. | URL field was missing forward slash, added that. |
| Review page not displaying static image | Added an if statement to display static image if missing image url |
| Delete app route not working | Added the missing @ in app route |
| Not redirecting to Login page when I tried to log in as an unregistered user | Change app route to return redirect(url_for("login")) |

___

Back to [README.md](README.md)

___

