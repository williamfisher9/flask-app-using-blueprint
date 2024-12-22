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

- A virtual environemnt can also be created using:
  ```
    # in the project directory run the below command
    py -m venv .venv

    # to activate the virtual environment profile run the below command
    # on windows
    source .venv/Scripts/activate
    # on linux
    source .venv/bin/activate

    # to deactivate the profile run
    deactivate

    # install the following packages after activating the profile
    pip install flask flask_restful flask_sqlalchemy

    # to store all dependencies in a requirements.txt file for sharing
    pip freeze > requirements.txt

    # create a .gitignore file and add
    .venv

    # to install dependencies from requirements.txt file
    pip install -r requirements.txt

    # create api.py in the project directory and add the following
    from flask import Flask
    app = Flask(__main__)
    @app.route('/')
    def home():
      return '<h1>Flask REST API home</h1>'

    if __name__ === '__main__':
      app.run(debug=true) # use debug for test env only
                          # in debug mode, hot reload is on

    # then run the file using the command
    py api.py
  ```

- When you create a Flask application, you start by creating a Flask object that represents your application, and then you associate views to routes. 
- Flask takes care of dispatching incoming requests to the correct view based on the request URL and the routes you’ve defined.
- In Flask, views can be any callable (like a function) that receives requests and returns the response for that request. Flask is responsible for sending the response back to the user.
- The default project layout is great for very small applications, but it doesn’t scale well. As your code grows, it can become harder for you to maintain everything in a single file. So, when your application grows in size or complexity, you may want to structure your code in a different way to keep it maintainable and clear to understand.
  - `Flask Blueprints` encapsulate functionality, such as views, templates, and other resources.
    - Create a Blueprint object and give it a name.
    - Add views to the blueprint using the route decorator.
    - When you register a Flask Blueprint in an application, you’re actually extending the application with the contents of the Blueprint.
    - The Blueprint object has methods and decorators that allow you to record operations to be executed when registering the Flask Blueprint in an application to extend it. One of the most used decorators is route. It allows you to associate a view function to a URL route. The following code block shows how this decorator is used:
      ```
      @example_blueprint.route('/')
      def index():
          return "This is an example app"
      ```
    - .errorhandler() to register an error handler function 
    - .before_request() to execute an action before every request
    - .after_request() to execute an action after every request
    - .app_template_filter() to register a template filter at the application level
