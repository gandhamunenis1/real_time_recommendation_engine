# Real-Time Product Recommendation Engine using Spark and Kafka

## 🚀 Project Overview
This project simulates a real-time product recommendation engine using Apache Spark, Kafka, and PySpark. It ingests user clickstream data, processes it in real-time, trains a collaborative filtering model using ALS, and outputs personalized product recommendations.

## 🛠 Tech Stack
- Apache Spark (Structured Streaming, PySpark)
- Apache Kafka
- Spark MLlib (ALS algorithm)
- Local FS / MinIO / AWS S3 (optional)
- Docker (optional for Kafka setup)
- Jupyter / Databricks Community Edition

## 📁 Folder Structure
```
real_time_recommendation_engine/
├── data/               # Raw and processed data
│   ├── raw_logs/       # Simulated input logs
│   └── processed/      # Curated data for ML
├── notebooks/          # Jupyter/Databricks notebooks
├── scripts/            # Spark & Kafka scripts
│   ├── producer/       # Kafka producer (simulates user events)
│   └── consumer/       # Spark structured streaming consumer
├── models/             # Saved ALS models
├── output/             # Final recommendations
├── config/             # Config files (Kafka, Spark)
├── docs/               # Documentation, images
└── README.md           # Project overview
```

## 📌 Key Features
- Ingests real-time clickstream data via Kafka
- Parses, cleans, and transforms data using PySpark
- Trains ALS model using Spark MLlib for product recommendations
- Supports streaming input/output using Spark Structured Streaming

## ✅ Getting Started
1. Clone the repo
2. Set up Kafka locally or with Docker
3. Run the producer to simulate events
4. Use Spark Structured Streaming to consume data
5. Train and evaluate ALS recommender model

## 👩‍💻 Author
Sai Gireesha Gandhamuneni

---

Feel free to customize this structure. Let me know if you want sample code added!
