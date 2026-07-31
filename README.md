#  Image Dataset Analyzer

##  Project Overview

Image Dataset Analyzer is a Python-based application that analyzes a dataset of images and generates a report containing useful information such as:

- Total number of files
- Number of valid images
- Number of invalid images
- Image format count (JPEG, PNG, etc.)
- Processed images
- Report generation
- Logging support
- Exception handling

The project is fully containerized using Docker and can be executed either locally or inside a Docker container.

---

##  Features

- Analyze image datasets automatically
- Supports JPEG and PNG image formats
- Counts valid and invalid images
- Generates a detailed report
- Saves processed images
- Logging for application execution
- Exception handling for invalid files
- Dockerized for easy deployment

---

##  Technologies Used

- Python 3.12
- Pillow
- Docker
- Docker Compose
- Git
- GitHub

---

##  Project Structure

```
ImageAnalyzer/
│
├── dataset/
├── processed/
├── report/
│
├── main.py
├── image_analyzer.py
├── image_handler.py
├── image_utils.py
├── base_imagehandler.py
├── report_generator.py
├── logger.py
├── exceptions.py
├── constants.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── README.md
```

---

##  Installation

### Clone the repository

```bash
git clone https://github.com/indra112284/ImageAnalyzer.git
```

### Move into the project

```bash
cd ImageAnalyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Run the Project

```bash
python main.py
```

---

##  Docker

### Build Docker Image

```bash
docker build -t image-analyzer .
```

### Run Docker Container

```bash
docker run --name image-project image-analyzer
```

---

##  Docker Compose

### Start

```bash
docker compose up --build
```

### Stop

```bash
docker compose down
```

---

##  Sample Output

```
============================================================
IMAGE DATASET ANALYZER
============================================================

BaseImageHandler initialized

Analysis Completed Successfully!

Total Files : 18
Valid Images : 18
Invalid Images : 0

JPEG : 17
PNG : 1

Report Saved At
/app/report/report.txt

Project Completed Successfully.
```

---

##  Output

The application generates:

- Processed Images
- Analysis Report
- Application Logs

---

##  Docker Hub

Docker Image:

```
docker pull indra11596/image-analyzer:latest
```

---

##  GitHub Repository

https://github.com/indra112284/ImageAnalyzer

---

##  Author

**Indra Sena Chittiboina**

---

##  License

This project is created for learning and internship purposes.