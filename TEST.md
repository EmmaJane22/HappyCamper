# Happy Camper Campsite Review Website - Emma Scott
## Backend Development Milestone Project

## Testing

## Table of Contents

4. [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Manual Testing](#manual-testing)
    - [Accessibility](#accessibility)
    - [Tools Testing](#tools-testing)
    - [Testing User Stories](#testing-user-stories)
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

The site has been run through the Lighthouse test on Google Developer Tools and achieved the following results:

Desktop - Home Page
![desktop home](/documentation/index.jpg)

Mobile - Home Page
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

### Manual Testing on Mobile and Desktop Devices

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
    - testers resported that they found signing up easy and quick.
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



### Footer

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| --- | --- | --- | --- | --- |

### Footer

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| --- | --- | --- | --- | --- |