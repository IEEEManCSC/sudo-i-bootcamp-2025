# **🚀 CI/CD Session Documentation**

## **📌 Introduction to CI/CD**
### **What is CI/CD?**
CI/CD (Continuous Integration & Continuous Deployment) automates the software development lifecycle (SDLC) by integrating, testing, and deploying code changes efficiently.

🔹 **Continuous Integration (CI):** Developers push code frequently, triggering automated testing and builds.
🔹 **Continuous Deployment (CD):** Successfully tested code is deployed automatically, reducing manual effort and errors.

📌 **Why is CI/CD Important?**
✅ Speeds up software development.
✅ Reduces deployment failures.
✅ Ensures consistent and reliable releases.
✅ Improves collaboration between developers and operations teams.

📜 **Resources to Learn More:**
🎥 [Jenkins CI/CD Course](https://youtube.com/playlist?list=PLQ5OGqigB8Vk4A8xEDJCU-HN_7XizU9FO&si=2eKkCj_x5rJveBK7)
🎥 [GitHub Actions for CI/CD](https://youtu.be/QDlIo97ibxY?si=tc22LmNz1ysxh49M)
🎥 [GitHub Actions Advanced](https://youtube.com/playlist?list=PLArH6NjfKsUhvGHrpag7SuPumMzQRhUKY&si=HBmGK2rIEYp3x9TY)
📜 [Jenkins Documentation](https://www.jenkins.io/doc/)
📜 [GitHub Actions Docs](https://docs.github.com/en/actions)

---

## **🛠️ Task 1: Setting Up CI/CD for a Personal Portfolio Website**
### **1️⃣ Create a GitHub Repository**
- Go to GitHub and create a **new repository** named `portfolio-website`.
- Choose **Public** and **Initialize with a README**.
- Clone the repository:
  ```bash
  git clone https://github.com/your-username/portfolio-website.git
  cd portfolio-website
  ```

### **2️⃣ Build the Portfolio Website**
📄 **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My Portfolio</h1>
    </header>
    <footer>
        <p>© 2025 Your Name</p>
    </footer>
</body>
</html>
```
📄 **styles.css**
```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f4f4f4;
}
```
📄 **script.js**
```js
console.log("Portfolio website loaded successfully!");
```

### **3️⃣ Configure GitHub Actions for CI/CD**
📄 **.github/workflows/deploy.yml**
```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Deploy to GitHub Pages
        uses: JamesIves/github-pages-deploy-action@v4
        with:
          branch: gh-pages
          folder: .
```

### **4️⃣ Push Changes to GitHub**
```bash
git add .
git commit -m "Initial commit - Portfolio Website"
git push origin main
```

### **5️⃣ Enable GitHub Pages**
- Go to **Settings → Pages** in GitHub.
- Under **Branch**, select `main` and click **Save**.
- Your site is now live at: `https://your-username.github.io/portfolio-website/`

✅ **Now, every push to `main` automatically updates your portfolio!**

---

## **🛠️ Task 2: CI/CD for Flutter App with GitHub Actions & Firebase**

### **1️⃣ Create a Simple Flutter App**
📄 **lib/main.dart**
```dart
import 'package:flutter/material.dart';
void main() {
  runApp(const MyApp());
}
class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Flutter CI/CD with Firebase')),
        body: const Center(
          child: Text('Deployed via GitHub Actions 🚀'),
        ),
      ),
    );
  }
}
```

### **2️⃣ Setup Firebase**
- Register your app in Firebase.
- Download `google-services.json` and place it inside `android/app/`.
- Install dependencies:
  ```bash
  flutter pub add firebase_core
  ```

### **3️⃣ Configure GitHub Actions for CI/CD**
📄 **.github/workflows/flutter-ci.yml**
```yaml
name: Flutter CI/CD with Firebase
on:
  push:
    branches:
      - main
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: 3.29.0
      - name: Install Dependencies
        run: flutter pub get
      - name: Build APK
        run: flutter build apk --release
      - name: Upload to Firebase
        run: |
          export GOOGLE_APPLICATION_CREDENTIALS="$HOME/firebase-service-account.json"
          firebase appdistribution:distribute build/app/outputs/flutter-apk/app-release.apk \
            --app ${{ secrets.FIREBASE_APP_ID }}
```

✅ **Now, every push to `main` triggers a build & deploy to Firebase!**

---

## **🛠️ Task 3: CI/CD for a Web App Using Jenkins on AWS**

### **1️⃣ Install Jenkins on Amazon Linux**
```bash
sudo yum update -y
sudo amazon-linux-extras enable corretto8
sudo yum install -y java-1.8.0-amazon-corretto-devel
wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

### **2️⃣ Set Up a Jenkins Pipeline**
📄 **Jenkinsfile**
```groovy
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building Application...'
            }
        }
        stage('Deploy') {
            steps {
                sh 'scp -r * ec2-user@YOUR_EC2_IP:/var/www/html/'
            }
        }
    }
}
```
✅ **Now, every commit triggers a Jenkins build & deploy to AWS EC2!**

---

## **🎯 Summary**
✅ **GitHub Actions automates Web & Mobile App CI/CD.**
✅ **Jenkins automates deployments on AWS.**
✅ **CI/CD ensures efficient, error-free software releases.**

🚀 *"Now you have fully automated CI/CD pipelines for Web & Mobile Apps!"* 🎯

