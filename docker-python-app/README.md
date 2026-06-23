# Dockerized Python Application

## Project Description
This project is a simple Python application containerized using Docker.  
It prints the current Python version and the current date & time when the container runs.

---

## Python Script Output
- Python version inside container
- Current date and time

---

## Docker Image Base
- python:3.12-slim

---

## How to Build the Image

```bash
docker build -t python-version-app .