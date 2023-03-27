# Orchid Shop data automation application

This is a terminal application to track shop sales, calculate expenses and profit, figure out recommended amount to have in stock. 

All data provided through the terminal input goes into a google spreadsheet.

This is the link to the live app:

/link/

## How to use the app

The app is based on the data the user provides in inputs.
There are 2 inputs:

1. Numbers of items bought to the stock of each type. In total 4 numbers must be provided.
2. Numbers of items sold of each type. In total 4 numbers.

According to the data provided the application calculates:
* the recommended ammount of items to have in stock with additional 5% to increase sales (according to last week sales);
* the expenses and income according to the trade (7 euros) and retail (9 euros) prices;
* the profit gained from every item and in total for the day.

Then the results are inserted into google spreadsheet in relevant worksheets.

## Features

### Accepts user input.

 <img src="img/1-input.png">

### Validates input.
    1. Checks if there are exactly 4 numbers separated by commas.
    2. Checks if the data provided is a number.
    3. If there's a mistake an error is raised. And the input request repeats.

 <img src="img/empty-input.png">

### Calculates recommended stock, day expenses, income, and profit.

 <img src="img/money.png">
 
 ### Data is uploaded to the google spreadsheet.

 <img src="img/worksheet.png">

## Testing

I have tested this application manually.

* Used PEP8 linter and confirmes that there no errors.

<img src="img/python-check.png">

* Tested in my gitPod terminal and Heroku terminal.
* Tested invalid inputs:
    * Empty input - Invalid data error is raised and data is requested again.
    <img src="img/empty-input.png">

    * Too many or not enough numbers - Invalid data error is raised, it shows how many the user entered and reminds to enter 4 numbers, then data is requested again.
    <img src="img/number-error.png">

    * A letter instead of a number - Invalid data error is raised, it shows what the user entered and reminds to enter numbers, then data is requested again.
    <img src="img/letter-error.png">

    *  A symbol instead of a number - Invalid data error is raised, it shows what the user entered and reminds to enter numbers, then data is requested again.
    <img src="img/symbol-error.png">

## Bugs

No bugs remaining

## Deployment

## Credits
Code Institute for student template.


