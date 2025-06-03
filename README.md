# 📊 Trade Operations REST API

This project implements a RESTful API to manage stock trade operations using **FastAPI** (or Django REST Framework). It allows clients to record and retrieve trade data securely and efficiently.

---

## 🚀 Features

- **Add Trade** – Record a new trade with details like ticker, price, quantity, side (buy/sell), and timestamp.
- **Fetch Trades** – Retrieve all or filtered trades (by ticker or date range).
- **Input Validation** – Ensures valid tickers, non-negative prices/quantities, correct data types.
- **Database** – Supports **PostgreSQL** or **MongoDB** for persistent storage.

---

## 📌 Tech Stack

- **Framework**: FastAPI or Django REST Framework
- **Database**: PostgreSQL or MongoDB
- **ORM**: SQLAlchemy / Tortoise (for FastAPI) or Django ORM
- **Validation**: Pydantic (FastAPI) or DRF Serializers
- **Testing**: Pytest or Django Test Client

---

## 📫 API Endpoints

### ➕ `POST /trades/`
Create a new trade.

**Request Body:**
```json
{
  "ticker": "AAPL",
  "price": 150.0,
  "quantity": 10,
  "side": "buy",
  "timestamp": "2025-06-03T14:30:00"
}
---

📁 Project Structure (FastAPI Example)
trade-api/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── routers/
│       └── trades.py
├── tests/
├── requirements.txt
└── README.md
---



