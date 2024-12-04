# Movies library management application using Python and Angular
- Install Python 3.13.1 which includes Python and PIP.
- Check installed versions of python and pip using:
  ```
    python --version
    pip --version
  ```
- When installing Python make sure to select "use admin user" and "add python to path env variable".
- Install pipenv as it brings the best of all packaging worlds (bundler, composer, npm, etc.) to Python developers. `Pipenv is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and the good old requirements.txt.`
  ```
    pip install pipenv
  ```
- Flask SQLAlchemy is the most popular ORM for flask applications.
  ```
    # to create a new virtual environment for the project
    # this will create Pipfile in the project directory
    pipenv shell
    
    #installs the ORM and MySQL client
    pipenv install sqlalchemy mysqlclient 
  ```
