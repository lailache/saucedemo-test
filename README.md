# SauceDemo E2E Test

This README provides instructions on how to set up and run the end-to-end test for the https://www.saucedemo.com/
website.

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
