# Happy Camper Campsite Review Website - Emma Scott
## Backend Development Milestone Project

## Testing

## Table of Contents

4. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Accessibility](#accessibility)
    - [Tools Testing](#tools-testing)
    - [Manual Testing](#manual-testing)
    - [Bugs & Fixes](#bugs-&-fixes)

### Code Validation
### W3C Markup Validator
    - All .html files were checked with the [W3C HTML Validator](https://validator.w3.org/) using the 'direct input' method.
    - These checks showed three pages with a missing closing div tag where I had copied and pasted the same snippet of code. This was fixed by moving the closing div tag from after the endif to the end of each card div.

    ![W3C image](/documentation/profile_div.jpg)

    - The validator also highlighted missing head elements, illegal characters, missing lang attributes and no-space characters however these are due to use Jinga templating (see example below).

    ![W3C error image](/documentation/index_error.jpg)

### CSS Validator
    -  All CSS code was checked with the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) using the 'direct input' method.

### JSHint Validator
    - This showed two warnings linked to the Materialize script on script.js
    ![jshint error image](/documentation/jshint_error.jpg)
    
    - It also showed two erros with two variables being used to call functions in sendEmail.js
     ![jshint email error image](/documentation/sendEmail_error.jpg)