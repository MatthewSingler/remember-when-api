# Remember When
Remember When is an application that allows users to participate in adding memories and facts to a databse. Users can sort through all the facts to jog their memories and interact with other users to compare what they remember from previous years. All users can comment on any piece of information in order to interact with others.

# Features
* Crud functionality
* Filtering database based on year and category

# Local Setup
1. Clone this repo  
  ```https://github.com/MatthewSingler/remember-when-api.git```<br/>
2. cd into directory in terminal  
`cd remember-when-api`<br/>
3. Run `pipenv install`  
4. Run `pipenv shell`  
5. Create migrations  
6. Make migrations  
7. Seed database with `python3 manage.py loaddata {table name}`  
Loaddata order shouold be users, tokens, years, facts, categories, fact_categories, comments  
8. Run server `python3 manage.py runserver`

