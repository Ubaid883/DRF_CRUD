# Django REST API for Student CRUD Operations

This project is a simple Django-based API that performs **CRUD (Create, Read, Update, Delete)** operations for student data using **Django REST Framework**. The API is built using **function-based views**, making it beginner-friendly and easy to understand.

---


## 📌 Features

- ✅ View all student records
- 🔍 Retrieve individual student details by ID
- 📝 Update a student's information by ID
- ❌ Delete a student record by ID

---

## 🚀 Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **SQLite3** (default, easily switchable to PostgreSQL or MySQL)

---



---

## 🔧 Setup Instructions

### 1. Clone the Repository

    git clone https://github.com/Ubaid883/DRF_CRUD.git

### 2. Create a Virtual Environment

   
    python -m venv .ven
    source .venv/bin/activate       # On Mac
    .venv\Scripts\activate         # On Windows: 

### 3. Install Dependencies
    
    pip install -r requirements.txt
### 4. Run Migrations

    
    python manage.py migrate

### 5. Start the Server
    
    python manage.py runserver

---
## 📡 API Endpoints

|Method| Endpoint| Description|
|------|---------|------------|
|GET| api/student/ | Get all student records|
|GET| api/student/id/ | Get a specific student by ID|
|PUT| api/student/id/ | Update student info by ID|
|DELETE | api/student/id/ | Delete student record by ID|

## 🙌 Acknowledgements
This project is built using the amazing tools provided by:
- [Django](https://www.python.org/)
- [Django REST Framework](https://www.django-rest-framework.org)

## 📬 Contact
For any queries or contributions, feel free to contact me or open an issue!

💼 GitHub: https://github.com/Ubaid883

📧 Email: ubaidsaleem825@gmail.com

---
![Student View](source\images\student_view_01.png)
![Student-details](source\images\student-details.png)
![Model code](source\images\model_code.png)
![View code](source\images\view_code.png)
