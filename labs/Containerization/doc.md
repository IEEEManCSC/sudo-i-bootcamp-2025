# **📦 Containerization Session Documentation**

## **🔹 Introduction to Containerization**

### **What is Containerization?**
Containerization is a technology that allows applications to be packaged with all their dependencies, ensuring they run consistently across different environments. Unlike traditional Virtual Machines (VMs), containers are lightweight and share the same OS kernel, making them faster and more efficient.

### **What is Docker?**
Docker is the most popular containerization tool that allows developers to:
- Create lightweight, portable applications.
- Ensure consistency across different environments (local, staging, production).
- Scale applications easily using container orchestration.

🔗 **Resources to Learn More:**  
🎥 [YouTube Playlist](https://youtube.com/playlist?list=PLX1bW_GeBRhDkTf_jbdvBbkHs2LCWVeXZ&si=ByWj8P6tPSrc_8vl)  
🎥 [Docker Crash Course](https://youtu.be/PrusdhS2lmo?si=oSnMwzFONzGkGLEj)  
📜 [Official Docker Documentation](https://docs.docker.com/)  

---

## **🛠️ 1. Installing Docker & MobaXterm**

### **🔹 Install Docker Desktop**
1. Download from the [official Docker website](https://www.docker.com/products/docker-desktop/).
2. Follow the installation steps for your OS (Windows, macOS, or Linux).
3. Verify installation by running:
   ```bash
   docker --version
   ```

### **🔹 Install MobaXterm (For Windows Users)**
1. Download from the [official MobaXterm website](https://mobaxterm.mobatek.net/download.html).
2. Install and launch the application.
3. Use it as a terminal to connect to remote servers and run Docker commands.

---

## **🔹 2. Viewing Docker Containers & Images**
```bash
docker ps         # List running containers  
docker ps -a      # List all containers (including stopped ones)  
docker images     # List available Docker images  
```

---

## **🚀 3. Creating & Running Containers**
```bash
docker create --name my_container my_image  # Create a container without starting it  
docker run --name my_container my_image     # Run a container immediately  
docker run -d --name my_container my_image  # Run a container in detached mode  
docker run -d --name my_container --restart always my_image  # Ensure the container restarts after reboot  
```

---

## **🔹 4. Managing Container Resources**
```bash
docker run -d --name my_container --memory 512m --cpus 1 my_image  # Limit memory & CPU usage  
```

---

## **🛑 5. Stopping & Removing Containers and Images**
```bash
docker stop my_container    # Stop a running container  
docker rm my_container      # Remove a stopped container  
docker rmi my_image         # Remove an image  
```

---

## **🛠️ 6. Creating Custom Docker Images**

### **🔹 Example 1: Running a Web Server**
```bash
docker run -d --name my_container -p 8080:80 my_image  
```

### **🔹 Example 2: Custom Image from a Running Container**
```bash
docker commit my_container my_custom_image:v1  
```

### **🔹 Example 3: Building an Image from a Dockerfile**
**Create a `Dockerfile`**:
```dockerfile
FROM httpd
ENV var1=123 var2=mohamed
LABEL test container
WORKDIR /usr/
RUN apt update
RUN apt install -y net-tools iputils-ping
COPY index.html /usr/local/htdocs
EXPOSE 80/tcp 443/tcp
CMD ["httpd-foreground"]
```
**Build & Run:**
```bash
docker build -t my_image:v1 .  
docker run -d -p 80:80 my_image:v1  
```

---

## **📤 7. Pushing a Custom Image to Docker Hub**
```bash
docker tag my-app username/my-app:v1  # Tag the image  
docker login                           # Log in to Docker Hub  
docker push username/my-app:v1         # Push the image  
```

---

## **🖥️ 8. Example: Python Flask App in a Docker Container**
### **🔹 Dockerfile**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EXPOSE 5001
```
### **🔹 requirements.txt**
```txt
flask
flask-cors
```
### **🔹 Build & Run**
```bash
docker build -t my-app .
docker run -d -p 5001:5001 my-app
```

---

## **🛠️ 9. Deploying a Multi-Container App Using Docker Compose**

### **🔹 Example 1: Running an Nginx Server**
Create a `docker-compose.yml`:
```yaml
version: "3.8"
services:
  web:
    image: nginx
    container_name: nginx-server
    ports:
      - "8080:80"
```
Run it:
```bash
docker-compose up -d
```

### **🔹 Example 2: WordPress with MySQL**
```yaml
version: "3.8"
services:
  db:
    image: mysql:5.7
    container_name: wordpress-db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: wordpress
      MYSQL_USER: user
      MYSQL_PASSWORD: password
    volumes:
      - db-data:/var/lib/mysql

  wordpress:
    image: wordpress
    container_name: wordpress-site
    restart: always
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: user
      WORDPRESS_DB_PASSWORD: password
      WORDPRESS_DB_NAME: wordpress
    depends_on:
      - db

volumes:
  db-data:
```
Run it:
```bash
docker-compose up -d
```

---

## **📌 Final Notes**
✅ Replace placeholders like `my_container`, `my_image`, and `my_hostname` with meaningful names.  
✅ Always verify containers using:
```bash
docker ps
docker images
docker logs <container_name>
```
✅ Use `docker-compose up -d` to start multi-container applications and `docker-compose down` to stop them.

🚀 Now you're ready to master Docker! 🎯