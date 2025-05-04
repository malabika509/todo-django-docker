# TODO Django Docker Project
This is a simple **TODO List** application built with **Django**, using **Docker** for containerization.

## Project Setup
To run the project locally, follow the steps below:

### Prerequisites
Make sure you have **Docker** and **Docker Compose** installed. You can download them from:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Steps to Run the Project
1. **Clone the Repository**:
   
   If you haven’t already, clone the repository:

   ```bash
   git clone https://github.com/malabika509/todo-django-docker.git
   cd todo-django-docker

2. **Build the Docker Containers in the VS Code terminal**
        docker-compose up --build

3. **Access the Application**
    Once the containers are up, navigate to the application in your browser:
    
        Frontend (UI): http://localhost:8000
        Admin Panel: http://localhost:8000/admin

4. **Create Superuser and run the below command in the VS Code terminal**
    If you need to access the Admin Panel to manage tasks, create a superuser account:

        docker-compose exec web python manage.py createsuperuser

    Then follow the prompts to set up a username, email, and password.

#### Admin Panel Access
To access the Django Admin Panel for managing tasks, follow these steps:

    1. Open the admin panel at http://localhost:8000/admin.
    2. Log in using the superuser credentials you just created.
    3. From the admin dashboard, you can add, edit, or delete tasks.

##### API Access 
If you want to interact with the TODO List via the API using Postman, the following endpoints are available:

    GET /tasks/: Fetch the list of tasks
    POST /tasks/: Create a new task
    GET /tasks/{id}/: Get details of a specific task
    PUT /tasks/{id}/: Update a specific task
    DELETE /tasks/{id}/: Delete a specific task

###### Testing
    You can test the application by running the following command in the terminal:
        docker-compose exec web python manage.py test

    Troubleshooting
        If you face any issues, check the following:
        Ensure Docker is running.
        Ensure all necessary Docker containers are up and running.
        Check the logs for any errors with the following command:
            docker-compose logs


