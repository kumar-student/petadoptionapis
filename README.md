# Pet Adoption RESTAPIs
This repository provides basic API endpoints for client app ex: Android app

Features:
1. Pet CRUD (Create-Read-Update-Delete) operations
2. Pet Search ex: `GET /api/pets/?species=cat&age=2.0`

## Initial setup
### Softwares
Required softwares:
1. [Python](https://www.python.org/downloads/)
2. [Git](https://git-scm.com/downloads/win)
### Cloning repository
1. Open Git Bash
2. Navigate to a folder where you want to clone the repository
    ```shell
    cd Documents/workspace
    ```
    Make sure you have `workspace` folder inside `Documents` folder
3. Clone the repository
    ```shell
    git clone https://github.com/kumar-student/petadoptionapis.git
    ```
    This will clone the repository into `petadoptionapis-main`
4. Navigate to cloned repository folder
    ```shell
    cd petadoptionapis-main
    ```
### Creating virtual environment
Before creating virtual environment make sure you have installed python. You can check by typing `python` in Git Bash
```shell
python
```

And also make sure you are in `petadoptionapis-main` folder. You can check it by typing `cwd` in Git Bash
```shell
cwd
```
#### Virtual Environment
Let's create virtual environment by typing the following command in you Git bash
```shell
python -m venv venv
```
#### Activating Virtual Environment
Enter the following command to activate the virtual environment
```shell
source venv/Scripts/activate
```
After executing above command you can see (venv) in your Git Bash
#### Installing Dependencies
Dependencies required for this project are listed in `requirements.txt`

To install dependencies run the following command
```shell
pip install -r requirements.txt
```
## Up and running the project
Run the backend apis server by entering the following command
```shell
python manage.py runserver
```

You can check whether the server running or not by visiting [http://127.0.0.1:8000](http://127.0.0.1:8000) address in your browser

## Admin Dashboard
This project provides default admin interface to mange databse record. Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to login into admin interface. 

You can user `admin` as username and `Admin@123` as password for the admin account.