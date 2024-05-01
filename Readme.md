# Project Setup

This README will guide you through setting up the environment and running the Django project.

## Prerequisites

Before you start, ensure you have Python and pip installed on your system.

## Setup

1. **Activate Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2. **Install Dependencies**:

    ```bash
    pip3 install -r requirements.txt
    ```

3. **Migrate Database**:

    ```bash
    python3 manage.py migrate
    ```

## Run the Server

To start the development server, run:

```bash
python3 manage.py runserver
```