# RPA - Web consultations and extraction.

## Description

The purpose of this project is to create a RPA that allows to browse the web, query some desired data within wikipedia and finally, take the information that is presented there to store it in a cvs file.

The project has been developed with Python, Selenium, and pandas for csv management.

## Authors

- [@juan154850](https://github.com/juan154850)

## Necessary programs

For the execution of the project, python must be installed to use selenium and pandas.
Link: https://www.python.org/downloads/

Additionally, it is recommended to use VS Code as a code editor.
Link: https://code.visualstudio.com/download

## Some of the dependencies are:

* selenium: v4.11.2
* pandas: v2.0.3

NOTE: Remember that to install the dependencies, you can make use of the following command, where name: is the package you want to install:

```bash
  pip install "name"
  E.g: pip install pandas
```

## Instructions for installation and use:

1. Using the console, the virtual environment is created

```bash
 python -m venv venv
```

2. In a python, console run the virtual environment (From VS Code, and located in main.py right click > run python file in terminal).
3. All dependencies are installed with:

```bash
 pip install -r .\requirements.txt
```

Note: Once the virtual environment is created, with the name "venv" you can run start.bat if your operating system is Windows to perform the installation of dependencies and program execution.
