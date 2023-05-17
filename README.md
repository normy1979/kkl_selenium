This is a base flask application with an sqllite database with a pytest file and home page.  To add another route, just create it in the 'modules' folder and register the blueprint in __init__.py. To configure it to run another database, add information to ProductionConfig in config.py and change __init.__.py accordingly.  Instruction to run below:


1. Create Virtual Environment
  $ cd app/application
  $ virtualenv venv
  $ source venv/bin/activate

2. Install requirements
  $ pip install -r requirements.txt

3. Test
  $ cd tests
  $ pytest -rP test_app.py

4. Run app
  $ flask run

5. Go to localhost:5000 to view