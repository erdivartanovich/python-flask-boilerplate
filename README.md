# Flask Restful App Boilerplate

Composed by: @erdivartanovich.

## Setup Dev Environment On Ubuntu

- Make sure we have python3 installed, by checking the version
    ```sh
    $ python3 -V
    ```

    Output
    ```sh
    $ Python 3.6.3
    ```

- Install Python3 if not available yet

    If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6 with the following commands:

    ```sh
        $ sudo apt-get update
        $ sudo apt-get install python3.6
    ```

    If you’re using another version of Ubuntu (e.g. the latest 16.04 LTS release), you can try using the deadsnakes PPA to install Python 3.6:

    ```sh
        $ sudo apt-get install software-properties-common
        $ sudo add-apt-repository ppa:deadsnakes/ppa
        $ sudo apt-get update
        $ sudo apt-get install python3.6
    ```
    
    These commands should install the latest python 3 available in ubuntu repository.
    There are a few more packages and development tools to install to ensure that we have a robust set-up for our programming environment:

    ```sh
       $ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
    ```

- Install Python3 Package Management (PIP3) 
    ```sh
        $ sudo apt-get install -y python3-pip
    ```sh

    We can confirm if pip3 is succesfully installed by this command

    ```sh
        $ pip3 -V
    ```

    the output should looked like this:

    ```sh
        pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
    ```

- Install Python3 virtual environment (using Python3 standard library)

    ```sh
        $ sudo apt-get install -y python3-venv
    ```

Now we are Set to go , for Python 3 app development.

## Configure Flask Application

- Create Project Folder (you can named it anything)

    ```sh
        $ mkdir flask-app
    ```

- First step we need to create a virtual-environment inside our project folder

    ```sh
        $ cd flask-app
        $ python3 -m venv env
    ```

    Now everytime we want to work with our flask app, just cd to the project folder and activate the virtual-environment:

    ```sh
        $ cd flask-app
        $ . env/bin/activate
    ```

    The shell cursor of your terminal should now display a sign that virtual env is activated.

    ```sh
        (env) username $
    ```

    To deactivate the virtual env just fire this command:

    ```sh
        $ deactivate
    ```

- Install Flask Package. Remember to cd to your project folder and activate the virtual-environment

    ```sh
        $ pip install flask
    ```

