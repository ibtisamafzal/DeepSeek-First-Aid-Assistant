# 🚑 Emergency First Aid Assistant  

### **🔹 Overview**  
The **Emergency First Aid Assistant** is an **AI-powered web application** designed to provide **instant first-aid guidance** based on user-reported symptoms. It enhances **emergency preparedness** by offering:

✅ **Real-time medical advice**  
✅ **Step-by-step first-aid procedures**  
✅ **Relevant YouTube video tutorials**  
✅ **Country-specific emergency numbers**  
✅ **One-click emergency call button**  

The app ensures **quick, reliable, and context-aware responses** to medical emergencies, helping users take immediate action before professional medical help arrives.

---

## 🚨 **Problem Statement**  
Medical emergencies happen **unexpectedly**, and most people:

- **Panic** due to lack of first-aid knowledge.  
- **Perform incorrect actions** that worsen the condition.  
- **Waste time searching online** for reliable medical advice.  
- **Don’t know emergency numbers** for different countries.  

⚠️ **In emergencies, every second counts!** This app aims to provide **instant AI-driven first-aid recommendations** to save lives.

---

## 🏥 **Solution**  
The **Emergency First Aid Assistant** is an intelligent AI agent that:

✔️ **Analyzes symptoms** to predict the possible medical condition.  
✔️ **Provides structured first-aid recommendations** (Do’s & Don’ts).  
✔️ **Fetches relevant first-aid videos** for visual guidance.  
✔️ **Displays emergency contact numbers** based on user’s country.  
✔️ **Includes an Emergency Call Button** for instant help.  

This **AI-powered assistant** reduces panic, improves response time, and ensures **users get the right first-aid steps immediately**.

---

## 🔹 **Key Features**  
### 🔍 **1. AI-Powered Symptom Analysis**  
- Uses **Mistral-7B** AI model to **analyze symptoms** and provide **accurate first-aid instructions**.  
- Classifies the condition into **Mild, Moderate, or Severe**.  

### 🎥 **2. Context-Aware Video Recommendations**  
- Uses **YouTube API** to fetch **relevant first-aid tutorials**.  
- Ensures the **recommended video matches** the user's symptoms.  

### 📍 **3. Country-Specific Emergency Contact Finder**  
- Retrieves **correct emergency numbers** based on the user’s location.  
- Covers emergency services like **Ambulance, Fire, and Police**.  

### 📞 **4. One-Tap Emergency Call Button**  
- Allows users to **quickly dial emergency services** directly from the app.  
- Ensures users can get **immediate help when needed**.  

### 🖥️ **5. User-Friendly Interface**  
- Developed using **Streamlit** for an **interactive and accessible UI**.  
- Simple, intuitive design with a **focus on emergency usability**.  

---

## 🏗️ **Technology Stack**  
| **Component**      | **Technology Used**  |
|--------------------|---------------------|
| **Frontend**       | Streamlit (Python)  |
| **AI Model**       | Mistral-7B (Hugging Face API)  |
| **APIs**           | YouTube API, Country Info API  |
| **Backend**        | Python (Flask for API integrations)  |
| **Deployment**     | Hugging Face / Streamlit Cloud  |

---

## 🔹 **How It Works**  
### **1️⃣ User Inputs Symptoms**  
- The user enters **symptoms** (e.g., "Severe headache, nausea").  

### **2️⃣ AI Analyzes & Provides First-Aid**  
- The **Mistral-7B model** generates a structured **first-aid response** with:
  - ✅ Possible medical condition  
  - ✅ Severity level (Mild, Moderate, Severe)  
  - ✅ Step-by-step first-aid instructions  
  - ✅ Common mistakes to avoid  
  - ✅ When to seek medical help  

### **3️⃣ Context-Based Video Recommendation**  
- The app **searches YouTube** for a **relevant first-aid video** based on symptoms.  

### **4️⃣ Emergency Contact Retrieval**  
- The app detects **user’s country** and **displays emergency numbers**.  

### **5️⃣ Emergency Call Button**  
- **One-click call** option for **instant connection** to local emergency services.  

---

## 🛠️ **Setup & Installation**  
### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/emergency-first-aid-assistant.git
cd emergency-first-aid-assistant
```

### **2. Create a Virtual Environment**  
```bash
python -m venv env
source env/bin/activate   # For macOS/Linux
env\Scripts\activate      # For Windows
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Set Up API Keys**  
Create a **.env** file in the root directory and add:  
```
HUGGINGFACE_API_KEY=your_huggingface_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

### **5. Run the App**  
```bash
streamlit run app.py
```

---

## 🎯 **Business Value & Real-World Impact**  
### 🔹 **For General Users**  
- Get **instant first-aid guidance** in emergencies.  

### 🔹 **For Travelers**  
- **Find correct emergency numbers** in foreign countries.  

### 🔹 **For Workplaces & Schools**  
- Serves as a **first-aid assistant** for employees and students.  

### 🔹 **For Emergency Services & Hospitals**  
- Can be **integrated with healthcare chatbots** for **quick medical assistance**.  

---

## 🚀 **Future Enhancements**  
🔹 **Voice Input Support** – Hands-free emergency assistance.  
🔹 **Real-time Doctor Consultation** – Connects users with medical professionals.  
🔹 **Offline Mode** – Saves essential first-aid guides for offline access.  
🔹 **Wearable & IoT Integration** – Sync with smartwatches for **real-time health monitoring**.  

---

## 👥 **Team - GenAI-Innovators**  
| Name                   | Role                         |
|------------------------|-----------------------------|
| **Muhammad Adnan Tariq**  | AI/ML Expert               |
| **Muhammad Khaqan Nasir** | API & Backend Developer    |
| **Muhammad Ibtisam**     | Frontend & UI/UX Developer |

---

## 📜 **License**  
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it.  

---

## 📎 **Links & Resources**  
🔹 **GitHub Repository**: [GitHub](https://github.com)  
🔹 **Live Demo**: [Streamlit App](https://your-live-demo-link.com)  

---

## ⭐ **Support & Contribution**  
🤝 **Contributions are welcome!** If you’d like to contribute:
1. **Fork the repository**  
2. **Create a feature branch** (`feature-new-improvement`)  
3. **Submit a pull request**  

🔔 **For any issues or suggestions, open an issue on GitHub!**
