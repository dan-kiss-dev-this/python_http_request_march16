Python Notes
//
To run the project activate the vitual enviornment
$to activate the python virtual enviornment venv do
$ source project_venv_consumee_api_dk/bin/activate

we are adding enviornmental variables to the virtual enviornment using
$ export FLASK_APP=application.py
$ export FLASK_ENV=development

now to run the enviornment do
$ flask run

to solve the error when run db.create_all() we make a context by running
$ flask shell

then in the flask shell we run
>> db.create_all()

see drinks by using
>> DRINK.query.all()





--
Additional notes to make a virtual enviornment for python write
$python3 -m venv project_env_dk_marchsixteen

the the -m means modules and -m venv will say grab the venv module aka package and run it

to activate the python virtual enviornment venv do
$ source project_env_dk_marchsixteen/bin/activate

then to see which python is activated
$ which python
python: aliased to /opt/homebrew/bin/python3

to add a package
$  pip3 install pytz

go to /Users/danielkiss/Code and run
$ pip freeze
this can be used to make a text file of the enviornment similair to package.json
to have the file be in the diectory you want it in and use a > pointing arrow bracket to make it like below
$ pip freeze > requirement_dk_marchsixteen.txt

to see the file in the command line as text run
$ cat requirement_dk_marchsixteen.txt

to deactive the enviornment type
$ deactivate

to fully r=delete an enviornment run
$ mr -rf project_env_dk_marchsixteen/

to install an enviornment do
$ pip install -r requirement_dk_marchsixteen.txt

do not put project file in venv folder

to install a pip file aka npm package do
$ pip3 install requests

note python supports json natively via
import json

to see a reponse do
//
import requests
import json

response = requests.get(
    'http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

print(response.json())

//
note the returned type is class 'requests.models.Response' and to return the json encoded content of the response use .json() method which will deserialize the JSON reponse into a python object using json.loads()
















