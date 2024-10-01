# Integration of exsited-python SDK with Django

This documentation outlines the steps to integrate the `exsited-python` SDK into a Django application. By following these steps, you will be able to use the SDK within your Django project environment. This method is an alternative to using `pip` to install the SDK directly from PyPI, allowing more flexibility in managing your own local version of the SDK.

# Steps for Integration

## 1. Create a Dependency Directory

In your Django application, create a directory where the SDK and other dependencies will be stored.

```bash
mkdir <your-django-app>/dependencies
```

## 2. Navigate to the Dependency Directory

Change your working directory to the newly created dependencies directory.

```bash
cd <your-django-app>/dependencies
```

## 3. Clone the SDK Repository

Clone the exsited-python SDK from GitHub into your dependencies directory.

```bash
git clone https://github.com/exsited/exsited-python.git
```

## 4. Set Up a Virtual Environment


```bash
#Navigate to the project directory
cd exsited-python

# Install virtualenv
pip install virtualenv

# Create Virtual Environment
python -m venv venv

# Active virtual Environment from windows
venv\Scripts\activate

# Upgrade the pip
python -m pip install --upgrade pip


```


## 5. Install SDK Dependencies


```bash
# Install setup tools
pip install setuptools

# Install app Dependency
pip install -e .

# Usage association Dependencies
pip install peewee
pip install mysql-connector-python
```



## 6. Set exsited-python as a Source Root

Make the exsited-python directory a source root for your Django project so you can import the SDK as needed. This may involve configuring your IDE or modifying PYTHONPATH.



Now, you can start using the SDK in your Django project. Import and integrate it as necessary in your views, models, or other components.
---

