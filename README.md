# Flask Restful App Boilerplate

Composed by: @erdivartanovich.

## Setup Dev Environment On Ubuntu

- Make sure we have python3 installed, by checking the version
    ```sh
    $ python3 -V
    ```

    Output
    ```sh
    $ Python 3.6.6
    ```

- Install Python3 if not available yet
    Ubuntu 16.04 or newer version are ship with both Python 3 and Python 2 pre-installed. To make sure that our versions are up-to-date, let’s update and upgrade the system with apt-get:

    ```sh
        $ sudo apt-get update
        $ sudo apt-get -y upgrade
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