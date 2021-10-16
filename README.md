# fetch-api


Fetch Points API mimics a rewards program API that accounts for the date, partner company, and point amount for transactions created by the user.

The backend of this application is constructed with the use of Flask framework. The frontend UI is simulated with the use of basic HTML and Jinja statements.

The application is routed to a Postgres relational database originally housed in PGAdmin during development, and is now deployed via Heroku.


Links in the navbar bring the user to the following pages:

- Partner Balances --- routes to a separate tab that shows all partners that have been entered into the database, with the sum of point totals for all transactions related to each unique partner, displayed in JSON style format

- Add Transactions --- form that allows users to enter partner names & point totals for an individual transaction; transaction timestamps are accounted for on the backend but not displayed anywhere in the UI

- Spend Points* --- form that allows users to input a point total that will be deducted from partner balances

- Github --- links to this repository


*At this time, the Spend Points functionality is not complete. The form accepts inputs but does not return any data, nor does it update the rows within the database to reflect points being deducted from the partners' totals. This functionality could be later introduced upon further investigation into how to sort items with Flask-SQLAlchemy while simultaneously updating those specified rows. Furthermore, deducing how much each transactions' point totals would be reduced in order to prevent any from falling below zero would require more logic to be inserted into the backend routing.


I enjoyed this project because it gave me an opportunity to construct an API with Flask and handle data in a new scenario I had not before encountered. Typically I have utilized Flask for handling data such as user authentication & other string-based items. Working with integers creates a new set of obstacles, and verifying that types are consistent with the implemented logic was an important factor to consider throughout the development of this project.

Consulting Flask-SQLAlchemy documentation was a necessity for determining the process of utilizing SQL statements within my backend routing, and will be necessary for troubleshooting the final task of completing the Spend Points functionality.
