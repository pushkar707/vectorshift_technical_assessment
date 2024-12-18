# FastAPI Project Setup

This repository contains a FastAPI project. Follow the steps below to set up the project locally.

---

## Prerequisites

Make sure you have the following installed on your system:

1. **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2. **Nodejs**
2. **Redis**
3. **Linux/Windows WSL**

---

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/pushkar707/vectorshift_technical_assessment
cd vectorshift_technical_assessment
```

### 2. Backend
```bash
cd backend
python3 -m venv myenv
pip install -r requirements.txt
source myenv/bin/activate
cp .env.example .env
```

#### Create Hubspot App
Create a developer account with hubspot here: https://developers.hubspot.com/get-started<br>
Add the scopes given in .env.example to your hubspot app<br>
Fill out credentials in .env file

``` bash
uvicorn uvicorn main:app --reload
```
You will have backend service running on `http://127.0.0.1: 8000`

### 3. Frontend
```bash
cd frontend
npm install
cp .env.example .env
npm run start
```
You will have frontend service running on `http://127.0.0.1:3000`

## Happy Hacking!