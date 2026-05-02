# RateMyHospital

## Project Overview
RateMyHospital is a Django web application designed to allow users to view healthcare facilities (hospitals) and their associated reviews. It provides a platform to browse hospitals and see detailed feedback, including ratings, compensation information, and pros/cons from reviewers.

## Technologies Used
*   **Python**
*   **Django (v6.0.2)**
*   **PostgreSQL** (for database management) download the newest version of PostgreSQL 
*   **python-dotenv** (for environment variable management)

## Setup and Local Development

To get this project up and running on your local machine, follow these steps:

### 1. Clone the Repository (if applicable)
If you're starting from scratch or don't have the project files, you would typically clone the repository.

### 2. Set up a Python Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Install all required Python packages using the `requirements.txt` file.

```bash
pip install -r RateMyHospital/requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the `RateMyHospital/` directory (next to `manage.py`) by copying the provided example.

```bash
cp RateMyHospital/.env.example RateMyHospital/.env
```
Open `RateMyHospital/.env` and fill in your PostgreSQL database credentials and a strong `SECRET_KEY` for Django.

Example `RateMyHospital/.env` content:
```
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY=your-highly-secret-and-long-django-key
DEBUG=True
```

### 5. Run Database Migrations
Apply the database schema changes:

```bash
python manage.py makemigrations main
python manage.py migrate
```

### 6. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```
This would then run on your local.

---

If the database does not read, you may need to dump the file onto your system. So create a database in postgresql which would be named PG4ADMIN on as an app, and then psql -U postgres -d healthcare_platform < your_dump_file.sql. 
