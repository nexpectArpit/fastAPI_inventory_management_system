# FastAPI + React Demo

**Project:** Simple product-tracking demo using FastAPI (backend) and a React frontend.

**Purpose:** Demonstrates a small CRUD API backed by SQLAlchemy and a create-react-app frontend that talks to the API.

---

**Prerequisites:**
- Python 3.10+ (project uses a local venv at `myFastAPienv`).
- Node.js and npm (for the frontend).

---

**Quick Start (Backend)**

- Create and activate the virtual environment (optional if `myFastAPienv` already exists):

```
python3 -m venv myFastAPienv
source myFastAPienv/bin/activate
```

- Install Python dependencies (FastAPI, Uvicorn, SQLAlchemy, DB driver):

```
pip install fastapi uvicorn sqlalchemy psycopg2
```

- Run the backend development server:

```
uvicorn main:app --reload
```

- Open the FastAPI interactive docs at: `http://127.0.0.1:8000/docs`

Notes:
- The backend code is in `main.py`. It defines CRUD endpoints for `Product` objects and uses SQLAlchemy models defined under `database_models.py` together with session helpers in `database.py`.
- On first run the code will create tables and initialize a few sample products if the database is empty.

---

**Quick Start (Frontend)**

- Change to the frontend directory and install packages:

```
cd frontend
npm install
```

- Start the frontend (create-react-app):

```
npm start
```

- The frontend expects the backend at `http://localhost:8000` (see `frontend/package.json` -> `proxy`). The React app runs by default at `http://localhost:3000`.

---

**Repository Structure**

- `main.py`: FastAPI application with routes and DB initialization.
- `database.py`: SQLAlchemy session / engine helpers.
- `database_models.py`: SQLAlchemy ORM models and `Base` metadata.
- `models.py`: Pydantic models used by FastAPI request/response validation.
- `frontend/`: React app (create-react-app).
- `setup.txt`: Quick setup notes and useful commands.
- `myFastAPienv/`: Optional local Python virtual environment (not checked in normally).

---

**API Endpoints (summary from `main.py`)**

- `GET /` — health check returns a welcome string.
- `GET /products` — list all products.
- `GET /products/{id}` — get product by id.
- `POST /products` — add a new product (accepts the Pydantic `Product` model payload).
- `PUT /products/{id}` — update an existing product.
- `DELETE /products/{id}` — delete a product by id.

Use the interactive docs at `http://127.0.0.1:8000/docs` to explore and test these endpoints.

---

**Database**

- The project uses SQLAlchemy. The default DB connection is configured in `database.py` — by default that file may use SQLite or another engine depending on your configuration. If you're using PostgreSQL, install `psycopg2` and set the correct connection URL in `database.py`.
- On first run, tables are created automatically via `database_models.Base.metadata.create_all(bind=engine)`.

---

**Developer Notes**

- The project includes a helper `get_db()` (dependency injection) to provide a DB `Session` to route handlers and ensure sessions are closed automatically.
- Sample data is inserted automatically if the products table is empty (see `init_db()` in `main.py`).

---
