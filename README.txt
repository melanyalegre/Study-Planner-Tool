📚 Study Planner Tool  
A simple and interactive study planning tool that helps students allocate their study hours efficiently based on subject difficulty and time remaining until exams.

This tool was created as part of the *Minor Data-Driven Decision Making* individual assignment.  
It applies data-driven logic and user-centered design to create a functional Minimum Viable Product (MVP).

---

🚀 Live App  
Use the app here:  
👉 https://study-planner-tool-hanstudentdemo.streamlit.app/

---

🎯 Features

- Add subjects with **difficulty sliders (1–5)**  
- Input **days until exam** for each subject  
- Select **which days of the week** you can study  
- Enter **total study hours** available for the week  
- Automatically generates:
  - A recommended hour allocation per subject  
  - A bar chart visualization  
  - A daily study schedule  

---

🧠 How It Works (Logic)

The app calculates a priority score for each subject.

Then it distributes your weekly study hours proportionally based on these scores.

This keeps the tool:
- Simple  
- Transparent  
- Fair  
- Easy to adjust  



🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy

---

📦 Folder Structure
Study-Planner-Tool/
│── app.py # Main application file
│── requirements.txt # Dependencies for Streamlit Cloud
│── README.md # Project description and documentation