# Secure Data Hiding in Images using Steganography

## 📌 Project Overview
This project implements **steganography**, a technique used to **hide secret messages inside images** without altering their appearance. It ensures **secure communication** by embedding encrypted text within image pixels.

## ❓ Problem Statement
With the rise in cyber threats, securing sensitive information is critical. Traditional encryption leaves visible traces, making it easy to detect. **Steganography** allows us to embed messages inside images, making them invisible to outsiders.

## 🛠️ Technology Stack
- **Programming Language**: Python  
- **Libraries Used**: OpenCV, PIL (Pillow)  
- **Platform**: Windows  
- **Encryption Method**: Character-based RGB pixel manipulation  
- **Image Formats Supported**: PNG, JPG  

## ✨ Features
✔️ **Real-time encryption & decryption** of messages in images  
✔️ **Password-protected decryption** for enhanced security  
✔️ **No visible changes in the image** after encryption  
✔️ **Fully automated process** with minimal user input  
✔️ **Supports multiple image formats** (JPG, PNG, etc.)  

## 🚀 How to Install & Run
1. **Install Dependencies**  
   ```bash
   pip install opencv-python pillow
   ```
2. **Run the script**  
   ```bash
   python steganography.py
   ```
3. **Follow the prompts** to encrypt & decrypt messages in an image.

## 📸 Example Usage
```
Enter secret message: HelloEveryone
Enter a passcode: 1234

Encrypted message stored in: D:\Downloads\encrypted_image.png

Enter passcode for Decryption: 1234
Decryption message: HelloEveryone
```

## 🔮 Future Scope
- Extend the project to **audio & video steganography**  
- Implement **AI-based detection prevention**  
- Develop a **GUI-based application** for wider usability  
- Optimize for **faster encryption & decryption**  

---  
🔐 **Developed for secure communication & data protection**  

