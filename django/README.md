GAP Django Boilerplate template ([Clean Verion Confluence](https://confluence.tools.jadeuc.com/display/GP/GAP+Django+Boilerplate+template))

STILL UNDER CONSTRUCTION "NOT FOR USE"

NOTE TO ME : go edit all web links and add libraries to static in app

Contents
Application Overview
Design Requirements
Local Requirements and Set Up
SSH Key Gitlab Set Up
Generate a personal access token
Create your Gitlab project
Set up your IDE & Project: (Using Visual Studios code)
Modify and link your own data table
Application Overview







Design Requirements

Django Framework

Database integration

Role Based Access Controls RBAC

Keycloak (All-Auth)

Local Development










Local Requirements and Set Up

SSH Key Gitlab Set Up:

Create GitLab SSH Keys with ssh-keygen




Both Ubuntu and Windows machines support SSH out of the box.

Updated versions of Windows 10 and Windows Server have built-in support since 2018, so there is no need to download Putty, PuttyGen or Plink to create RAS keys or to SSH in to GitLab. Just open PowerShell in Windows or a Linux terminal window on Ubuntu  or Mac OSx terminal and issue the following command:

C:\gitlab\ssh\example> ssh-keygen -o -t rsa -b 4096 -C "ssh-keygen@gitlab.jadeuc.com"

The options provided to the ssh-keygen command force the tool to create an RSA compatible key using the latest OpenSSL standards. The -C switch simply adds a comment to the end of the public file.

Accept all of the defaults when prompted for a passphrase or a special storage location. By default, all GitLab SSH keys must go in an .ssh folder under the user’s home directory. Furthermore, a blank passphrase is acceptable unless your organization’s compliance rules state otherwise.

This operation will create Git SSH keys named id_ras.pub and id_rsa respectively.

Copy the public SSH key

You must configure the value of the public key in GitLab. Open the public key in a text editor and copy the value to the clipboard:

Copy the .pub key produced from the GitLab SSH key generation operation and configure it into GitLab.

Configure GitLab SSH keys

Log into GitLab and click on your account preferences.

Click the SSH Keys link and paste the copied value into the text field.

Set an expiration date, and then click the blue button to persistently add the GitLab SSH key.

Configure GitLab SSH keys under your account preferences.

Generate a Personal Access Token

Continue under preferences and select access tokens on the left hand side

 I would name the token based on the IDE you are using. Also notice that you can chose an expiration date for the token. I would also give the token full permissions as shown below. Then I would click generate personal access token.

Next copy and save that token temporarily to a local .txt . You will need it later

Create your Gitlab project

Go to https://gitlab.jadeuc.com/gap/bza/ and click new sub group. 

Recommend naming it with the following convention <"your project name">.I would leave the project private until your ready to share it with the rest of the Gitlab teams. Then Click create sub group




Then fork the 

Click create blank project. Recommend naming it using  the following convention <app_"your project name">

Click create project then go back to your 

Then create another new project with that subgroup. Recommend naming it with the following convention <keycloak_"your project name">

Click create blank project. Recommend naming it using  the following convention <keycloak_"your project name">

Click create project




Now you need to fork the app_django_boilerplate into the subgroup you created above

got to https://gitlab.jadeuc.com/gap/bza/gap_django_boilerplate/app_django_boilerplate.git and click fork

change the project name using the following format "app_<your project  name>" Then Change the name space to the location of your project sub group. Project slug will auto populate when you create the project name. Select your visibility level. ( you can always change it later )

Now you need to fork the keycloak_django_boilerplate into the subgroup you created above

got to  https://gitlab.jadeuc.com/gap/bza/gap_django_boilerplate/keycloak_django_boilerplate and click fork

change the project name using the following format "keycloak_<your project  name>" Then Change the name space to the location of your project sub group. Project slug will auto populate when you create the project name. Select your visibility level. ( you can always change it later )

Set up your IDE & Project: (Using Visual Studios code)

Install visual studios code (download and install the proper version for your OS)

Install all of the following extension

Also add:

Clone your keycloak_<your_app_name>  from the fork you created earlier

copy the git link for your keycloak_<your_app_name>

############edit photo to demo

 then open VS Code and click "clone git repository" 

then paste the git link into the clone from url bar and click enter

next create and select a parent folder for all of your applications. I created a folder called  "Visual_Studio_Code_Projects" in my home directory. Make sure you select this folder as the location you want to clone your keycloak application to.

click enter  and select open in "new window"




Clone your app_<your_app_name> from the fork you created earlier

Repeat. the same process you used for  "Clone your keycloak_<your_app_name>" This time you will use the same folder you selected in the step above.

your final directory should look like this:

Django setup with pyenv + Poetry on macOS (Original Cited Material from Jason Yee)

Install pyenv and a specific version of Python for python version management which ensures you’ve got python the required python environment
Install poetry for dependency management which ensure you’ve got the right packages installed in your environment like django.
Test our dev setup by starting & launching your django app
Prerequisite

1/5: Install homebrew (https://mac.install.guide/homebrew/index.html, you may have to install Xcode command line tools)
2/5 Install pyenv and a specific version of python

Go to your dev project directory and create a folder for your project. In this example, my dev dir is ~/Visual_Studio_Code_Projects/<project_name>.

Install pyenv with homebrew.

open Terminal using the Visual studios code Upper toolbar

$ cd ~/Visual_Studio_Code_Projects/<project_name>

$ brew install pyenv

Once this is complete, update your ~/.zshrc to include the lines that pyenv init instructs you to do and restart your shell.

$ pyenv init

Modify .zprofile]

$ cd ~
$ vim .zprofile

scroll down past the initial text and press(i) to insert the following text:

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"  

Then save and exit vim by pressing escape twice and then type ":wq" and enter

$ touch ~/.zshrc

Modify .zprofile

$ cd ~
$ vim .zshrc

scroll down past the initial text and press() to insert the following text:

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"  

Then save and exit vim by pressing escape twice and then type ":wq" and enter

Next you need to Initiate your pyenv and install the proper python version for your project

$ pyenv init
$ pyenv install 3.10.2

Exit terminal
Open new terminal

$ cd ~/Visual_Studio_Code_Projects/<project_name>
$ pyenv local 3.10.2
$ ls -la

-rw-r--r--   1 username  staff    7 Jun 28 15:09 .python-version


Notice that after I create run the pyenv command, it creates a .python-version file that notes the version of python I want. This has the effect of ensuring that running python in any subfolder of this will run the specific python version unless other pyenv settings are set. Read more about pyenv here: https://github.com/pyenv/pyenv#how-it-works

3/5 Install poetry and dependencies

Install poetry with homebrew.

$ brew install poetry

Now, update the poetry env by specifying the pyenv — this is a very important step. When you installed poetry, it installed python 3.10.5 as your system python so you need to override this by specifying the right env to poetry with 

$ poetry env use $(pyenv which python). You only need to do this once

$ poetry env info 

Virtualenv
Python:         3.10.2
Implementation: CPython
Path:           /Users/CyberSlayer/Library/Caches/pypoetry/virtualenvs/django-boilerplate-gap-gDsY__FE-py3.10
Executable:     /Users/CyberSlayer/Library/Caches/pypoetry/virtualenvs/django-boilerplate-gap-gDsY__FE-py3.10/bin/python
Valid:          True

System
Platform:   darwin
OS:         posix
Python:     3.10.2
Path:       /Users/CyberSlayer/.pyenv/versions/3.10.2
Executable: /Users/CyberSlayer/.pyenv/versions/3.10.2/bin/python3.10

Now you can create the environment with poetry install and add the dependencies you want with the poetry add command. 

$ poetry install

Updating dependencies
.

Note: if you see an error message like the below, delete your poetry env with poetry env remove 3.10.2and make sure you ran poetry env use $(pyenv which python)

The currently activated Python version 3.10.5 is not supported by the project (3.10.2).
Trying to find and use a compatible version.

4/5 Run Local Keycloak 

Make sure Docker is running on your system.

Then return to your keycloak project in VS Code

Open a new terminal and enter the following command:

$ docker-compose up

when it is loaded you should see something similar to the following

"You now have a local running keycloak"

5/5 Run Your Application

Start a shell with poetry shell and note the change to your prompt and the location of your dependencies.

$ cd ~/Visual_Studio_Code_Projects/<project_name>

$ poetry shell

$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...System check identified no issues (0 silenced).
Run 'python manage.py migrate' to apply them.
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Success! screenshot courtesy of author

Pausing

When you’re doing developing locally and want to exit the poetry shell, exit the shell/virtualenv context as normal or close the terminal window to end the session. Once this is done, the prompt won’t have the virtualenv in parentheses above it and you’ll see that you don’t have any of your dependencies available to pip.

$ exit
$ pip freeze 
# nothing here

Resuming

When you want to do dev in this project again, navigate to the folder or a subfolder of where you created the .python-version file and pyproject.toml files and re-run poetry shell. pyenv will make sure that right version of python is available.

$ cd ~/code/django-mozilla
$ poetry shell

Spawning shell within /Users/jyee/Library/Caches/pypoetry/virtualenvs/django-mozilla-aI61n14v-py3.10

$ python -V

Python 3.10.2

Modify and link your own Data Table

In order to modify and add fields you will need to open two files:

App_Data_Table/models.py & db.sqlite3 (found in the root of the project folder)

In your App_Data_Table/models.py App_Data_Table_<your new class> "For demonstration purposes I will name mine App_Data_Table_member2"

copy your the original class an and past it in the lines bellow:

Make sure to modify and add the field names you want to include.




Next you will see the database explorer in your sidebar

click the data base icon.

Then select your database for this demonstration  I will select sqLite and add copy the directory link and past it into the path field box . 

once you past the link into the path field click save and a new view should pop up  in the same area where your file explore was click the first drop down arrow and then click the drop down for tables and select tables an click the + icon to add a new table:

then rename the highlighted text App_Data_Table_<your new class> (make sure you lowercase the first letter regardless of the case of the class in model.py

click the play button in the upper right corner:




Click the plus icon to add new column make sure the new column is spelled and capitalized exactly the same as your model.py:

when you have edited the alter-template.sql to include one of those columns click the play button. Repeat this for each column you want to add.

Open up App_Data_Table/views2.py and modify the following:

 change all instances of Member to Member2 and change column names to your new column names:

 Then open App_Data_Table/templates/datatables/base.html and modify the old tags of 

address & phone and replace them with eyecolor and height 

You can do this my doing a control F on the active window  select the down arrow and use find and replace.

repeat this process for App_Data_Table/templates/datatables/index.html




Test it in browser and verify changes have taken effect.




If the step above was successful then you should go back and clean up old artifacts in the models.py and remove "member" Not "Member2"

Then go to the database and drop the old "Member" table:

For more info on additional modification or updating the jquery.dataTables.min.js file see 

