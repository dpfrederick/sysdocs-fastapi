# Local Setup

This document explains how to setup the local development environment for the project.

## Installation

### 1. Install Pyenv
Pyenv is a Python version manager. It allows you to install multiple versions of Python on your machine and switch between them easily.

  - [Windows Installation](https://github.com/pyenv-win/pyenv-win#introduction)
  - [*Nix Installation](https://github.com/pyenv/pyenv#installation)


### 2. Install Python using Pyenv

- Navigate to the project root directory
- Run `pyenv install 3.11.3` to install python

### 3. Install Poetry

Poetry is a Python dependency manager. It allows you to install and manage dependencies for your Python projects.


- Navigate to the project root directory
- Run `pip install poetry` to install poetry for the specific python version

### 4. Install Dependencies

- Navigate to the project root directory
- Run `poetry install` to install the project dependencies


### 5. Activate Virtual Environment

- Navigate to the project root directory
- Run `poetry shell` to activate the virtual environment

## IDE integration

### Visual Studio Code

To integrate the project with Visual Studio Code, follow the steps below:

1. Open `.vscode/default.code-workspace` in Visual Studio Code
1. Install the recommended extensions

## Local Secrets
All local that should not be committed to source control should be stored in the `.env` file. This file should be created in the project root directory and should not be committed to source control.