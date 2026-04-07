# 🎓 Student Record Management System
# ScreenShots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3772533e-eef2-4dff-8980-a2d6c3aae5e3" />
<img width="1895" height="862" alt="image" src="https://github.com/user-attachments/assets/106e5016-4904-4ea3-ae39-1eba4d02c7d7" />
<img width="1799" height="810" alt="image" src="https://github.com/user-attachments/assets/26442642-e2f4-40b3-a4b3-7d8dd55ea41c" />
[Click here to watch the Student_record_management_system App demo](https://github.com/user-attachments/assets/19f78d06-d9b8-4bbf-b23c-4fe688b51d27)

## 🚀 Project Overview

The **Student Record Management System** helps in organizing academic records in a structured way.  
It allows users to manage:

- 👨‍🎓 Student records
- 📚 Course details
- 📝 Subject-wise marks
- 🔍 Search and filter student data

This project focuses on understanding **real-world backend development concepts** such as **relational database design, Django ORM, CRUD operations, and model relationships**.

---

## ✨ Features

### ✅ Core Features
- Add, view, update, and delete student records
- Add and manage courses
- Assign students to courses
- Add subject-wise marks for students
- View detailed student profiles
- Search students by name
- Filter students by course

### 🌟 Optional/Extended Features
- Attendance management
- Pass/Fail calculation
- Percentage calculation
- Student photo upload
- Better UI with Bootstrap

---

## 🧠 Concepts Learned

This project helped me strengthen my understanding of:

- Django project structure
- Django apps
- Models and database design
- **ForeignKey relationships**
- CRUD operations
- Django ORM queries
- Forms using `ModelForm`
- Template rendering
- Search and filtering
- Django admin panel

---

## 🏗️ Tech Stack

- **Backend:** Django, Python
- **Frontend:** HTML, CSS
- **Database:** SQLite3
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```bash
student_project/
│
├── manage.py
├── requirements.txt
├── student_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── records/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── records/
│           ├── student_list.html
│           ├── student_form.html
│           ├── student_detail.html
│           ├── course_list.html
│           ├── course_form.html
│           ├── mark_form.html
│           └── confirm_delete.html
```

---

## 🗃️ Database Models

### 1. Course
- `name`
- `duration`
- `description`

### 2. Student
- `name`
- `roll_number`
- `email`
- `age`
- `joined_date`
- `course` *(ForeignKey to Course)*

### 3. Mark
- `student` *(ForeignKey to Student)*
- `subject`
- `score`

---

## 🔗 Model Relationships

- **One Course → Many Students**
- **One Student → Many Marks**

This project demonstrates how Django handles **relational data** using `ForeignKey`.

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone <your-repository-link>
cd django-student-record-management
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On Mac/Linux:
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser (Optional but Recommended)
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server
```bash
python manage.py runserver
```

### 8️⃣ Open in Browser
```bash
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

To access the Django admin panel:

```bash
http://127.0.0.1:8000/admin/
```

Use the superuser credentials you created with:

```bash
python manage.py createsuperuser
```

---



## 🎯 Learning Outcome

This project helped me better understand how **real-world data is structured and managed in Django applications**.

It improved my confidence in:

- Designing relational databases
- Connecting models with `ForeignKey`
- Querying data using Django ORM
- Building backend-driven applications

---

## 🚀 Future Improvements

Some features I plan to add in future versions:

- Attendance tracking
- Student performance dashboard
- Percentage and grade calculation
- Student image upload
- Responsive UI using Bootstrap
- Authentication system for admin/staff users



## 🙌 Connect With Me
If you'd like to connect or share feedback, feel free to reach out on **LinkedIn** [www.linkedin.com/in/himasree28](https://www.linkedin.com/in/himasree28/).
---

## ⭐ Support

If you like this project, consider giving it a **star** ⭐ on GitHub!
