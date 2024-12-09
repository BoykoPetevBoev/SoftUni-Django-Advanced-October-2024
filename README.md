# SoftUni-Django-Advanced-October-2024

## How to Run the Project

Follow these steps to get the project up and running using Docker:

1. **Open Docker Desktop**  
   Make sure Docker Desktop is running on your machine.

2. **Navigate to the Project Folder**  
   Open a terminal and navigate to the project directory. Run the following command to 
   Navigate to correct directory:
   ```bash
   cd django_advanced

3. **Create env file**  
   Open a terminal and navigate to the project directory. Run the following command to 
   Add this content in .env file inside django_advanced:
   ```bash
   SECRET_KEY=django-insecure-b-_!c)u97$+nbv%s-cciawiqsjwdp6dvg71)4)k3&da$sx-b4y
   DEBUG=True
   DJANGO_ALLOWED_HOSTS=
   DJANGO_SETTINGS_MODULE=django_advanced.settings
   DATABASE_NAME=django_advanced_db
   DATABASE_USER=postgres
   DATABASE_PASSWORD=admin
   DATABASE_HOST=db
   DATABASE_PORT=5432
   POSTGRES_DB=postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=admin        
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_USE_SSL=True
   EMAIL_HOST_USER=testtest@gmail.com
   DEFAULT_FROM_EMAIL=testtest@gmail.com
   EMAIL_HOST_PASSWORD=testtest@gmail.com


2. **Build the Docker Images**  
   Open a terminal and navigate to the project directory. Run the following command to build the Docker images:
   ```bash
   docker-compose build

3. **Start the Docker Containers**  
    After the build process is complete, run the following command to start the Docker containers:
   ```bash
   docker-compose up

4. **Access the Application**
    Open your web browser and navigate to:
   ```bash
   http://localhost:8000