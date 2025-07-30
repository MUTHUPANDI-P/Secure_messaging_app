# 🔐 Secure Messaging Application with Encryption

## 📌 Project Aim
To develop a basic chat application that demonstrates **secure communication** using symmetric encryption (**Fernet cipher**) in Python with a **Flask web framework**.  
The system allows two users to send and receive **encrypted messages** through a simple web interface.

---

## 🛠️ Technologies Used
- **Python (Flask Framework)** – Backend web application
- **Cryptography (Fernet Module)** – Symmetric encryption/decryption
- **HTML5, CSS, Bootstrap** – Frontend design for chat UI
- **Local Storage (In-Memory)** – Message handling during runtime

---

## 📖 Project Description
This project focuses on **data security in chat applications** by encrypting every message before storing or displaying it.  
Encryption ensures that even if someone accesses the stored data, the actual message cannot be understood without the encryption key.

### 🔑 Key Aspects
✅ Secure key generation and storage (`secret.key`)  
✅ Real-time encryption of messages on submission  
✅ Decryption only for internal processing (not shown to users)  
✅ Clean, mobile-friendly UI using Bootstrap  

---

## ⚙️ Working Principle
1️⃣ **Key Generation** – A secret key is generated and stored in `secret.key` for consistent encryption/decryption.  
2️⃣ **Message Encryption** – When a user sends a message, it is immediately encrypted using **Fernet cipher** and stored in memory.  
3️⃣ **Message Display** – Messages are shown as **encrypted strings** to maintain confidentiality.  
4️⃣ **Two-User Roles** – The system allows **User A and User B** to chat alternately in an encrypted format.

---

## ✨ Features
- 🔄 Two-user chat simulation (**User A & User B**)
- 🔐 Symmetric encryption (**AES-based Fernet**) for messages
- ⚡ Lightweight **Flask server** with **Bootstrap UI**
- 🚀 Easy to integrate and deploy as a **basic secure messaging prototype**

---

## 📸 Sample Output  

![Screenshot 1](https://github.com/MUTHUPANDI-P/Secure_messaging_app/blob/main/images/Screenshot1.png?raw=true)  
![Screenshot 2](https://github.com/MUTHUPANDI-P/Secure_messaging_app/blob/main/images/Screenshot2.png?raw=true)

---
