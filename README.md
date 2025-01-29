# 📧 Spam Email Detector - Kubernetes Deployment

## 🚀 Project Overview
This project provides a **Spam Email Detection API** using a **Hugging Face Transformer model**. The API is containerized with **Docker** and deployed using **Kubernetes**.

---

## 📂 Project Structure
```
spam-detector/
│── app/                  # FastAPI Application
│   ├── main.py           # FastAPI app (API endpoints)
│   ├── model.py          # Loads the Hugging Face model
│   ├── schemas.py        # Defines request/response schemas
│   ├── telegram_bot.py   # Connects the telegram bot to the project
│── k8s/                  # Kubernetes Deployment Configs
│   ├── deployment.yaml   # Deployment for the API
│   ├── service.yaml      # Exposes the API as a service
│── requirements.txt      # Python dependencies
│── Dockerfile            # Docker container setup
│── .dockerignore         # Ignore unnecessary files in Docker build
│── .gitignore            # Ignore unnecessary files in GitHub
│── README.md             # Project documentation
```

---

## 🐳 Docker Setup
### **1. Build & Push Docker Image**
```sh
docker build -t your-dockerhub-username/spam-detector:latest .
docker push your-dockerhub-username/spam-detector:latest
```

---

## ☸️ Kubernetes Deployment
### **2. Deploy to Kubernetes**
```sh
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### **3. Check Status**
```sh
kubectl get pods
kubectl get svc spam-detector-service
```

---

## 🔥 API Usage
### **4. Test the API**
```sh
Postman 'POST' \
  localhost:8000/predict \
  -H 'Content-Type: application/json' \
  -d '{"text": "Win a free iPhone now!"}'
```
### **Example Response:**
```json
{
    "label": "Spam",
    "score": 0.9997568726539612
}
```

---

## 📌 Next Steps
✅ **Add autoscaling** (`HorizontalPodAutoscaler`)
✅ **Deploy to a managed Kubernetes service** (AWS EKS, GKE, AKS)
✅ **Implement monitoring with Prometheus & Grafana**

🚀 Happy Deploying! 🎉

