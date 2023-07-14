# 🚀 PyMOUtility

A handy collection of helper functions, decorators, and utilities designed to streamline and simplify your Python 🐍 development experience. PyMOUtility is an open-source project that provides powerful tools to make your code cleaner, more readable, and easier to debug.

## ⚙️ Installation

PyMOUtility uses [Poetry](https://python-poetry.org/docs/) for dependency management. To install PyMOUtility, make sure you have Python 3.7 or higher and Poetry installed on your system.

First, clone the repository:

```bash
git clone https://github.com/username/pyMOUtility.git
cd pyMOUtility
```

Please replace 'username' with the actual username of the repository.

Then, install the dependencies using Poetry:

```bash
poetry install
```

This will create a virtual environment and install all the necessary dependencies.

You can then use PyMOUtility within this virtual environment or build it for usage elsewhere.

If you wish to build a distribution package, use:

```bash
poetry build
```

This will produce a .whl file in the `dist/` directory that you can install using pip:

```bash
pip install dist/pyMOUtility-*.whl
```

Please replace '*' with the actual version of the PyMOUtility package.

Remember to always activate the virtual environment created by Poetry before using the package:

```bash
poetry shell
```

This command will spawn a shell within the virtual environment. If you want to leave the virtual environment, simply exit the shell.

## ✨ Features

* **🛠️ Helper Functions**: A collection of functions to help handle and manipulate data more efficiently.
* **🖼️ Decorators**: Save time on writing repetitive code blocks with these ready-to-use decorators.
* **🔍 Error Handlers**: Tools for handling and debugging exceptions gracefully.

## 📖 Usage

Import the required utility from the PyMOUtility package. Here's a simple example:

```python
from pymoutility.decorators import timeit

@timeit(print)
def my_function():
    ...

my_function() # this will print the time taken to execute my_function
```

## 📚 Detailed Documentation

For a complete understanding of how to use PyMOUtility, refer to the [documentation](LINK_TO_DOCUMENTATION_HERE) (to be updated).

## 💡 Examples

To see PyMOUtility in action, check out these [examples](./pymoutility/notebooks/Examples.ipynb).


## 👥 Contributing

PyMOUtility is an open-source project, and we welcome contributions of all sorts! Here are some ways you can contribute:

- **Improving Documentation**: If you find any issues in the documentation or think it can be improved, feel free to make changes and submit a pull request.

- **Reporting Bugs**: If you find a bug, please create an issue detailing what you found. Include as much detail as possible, such as the Python version, PyMOUtility version, and the steps to reproduce the bug.

- **Feature Requests**: If you think a feature could be useful in PyMOUtility, please create an issue describing the feature and why it would be beneficial.

- **Writing Code**: If you want to contribute code to fix bugs, add features, or enhance the project in any way, here's a basic workflow:
    1. Fork the repository and clone it locally.
    2. Create a branch for your changes.
    3. Make the changes in your branch.
    4. Run the tests to ensure your changes don't break existing functionality.
    5. Push your changes to your fork.
    6. Submit a pull request.

When submitting a pull request, please make sure your code follows the existing coding style, your changes are well-documented, and that you've added tests if you've introduced any new features.

We appreciate all contributions, and we're always excited to see what the community comes up with!

## 🧪 Testing

To run the tests, use the following command:

```bash
python -m pytest "tests"
```

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](./LICENSELICENSE) file for details.

## 📧 Contact

For any queries, feel free to open an issue or contact us at [jasmeet.gujral@mostacktechnology.com](mailto:jasmeet.gujral@mostacktechnology.com).

## 🧪 Testing

To run the tests, use the following command:

```bash
python -m pytest "tests"
```

## 📜 Changelog

See the [CHANGELOG]() for a history of notable changes to PyMOUtility.

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 📧 Contact

For any queries, feel free to open an issue or contact us at [jasmeet.gujral@mostacktechnology.com](mailto:jasmeet.gujral@mostacktechnology.com).
