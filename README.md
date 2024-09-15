# SauceDemo E2E Test

This README provides instructions on how to set up and run the end-to-end test for the https://www.saucedemo.com/
website.

### set up the environment

Create .env file and add the following lines to it:

GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
REPO_NAME=test-repo

### deploy virtual environment

```bash
python -m venv venv
```

Activation for **windows**:

```bash
venv/scripts/activate
```

### install libraries

```bash
pip install -r requirements.txt
```

### run the test

To run the test, use the following command:

```bash
python -m unittest tests/test_purchase.py
```
