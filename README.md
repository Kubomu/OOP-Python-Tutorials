# Object-Oriented Programming (OOP) in Python

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Kubomu/OOP-Python-Tutorials?quickstart=1)
[![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Welcome to the OOP in Python tutorial repository! This repository contains a series of Python scripts designed to teach the core concepts of Object-Oriented Programming (OOP). Each concept is explained with examples, and you can practise every one of them with hands-on exercises that grade themselves as you go.

New to programming? You do not need to install anything. Jump to [Try it now](#try-it-now-no-install-needed) and you will be running real Python code in your browser in under a minute.

## Table of Contents

- [Try it now (no install needed)](#try-it-now-no-install-needed)
- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [How to Use This Tutorial](#how-to-use-this-tutorial)
- [Concepts Covered](#concepts-covered)
- [Interactive practice with instant feedback](#interactive-practice-with-instant-feedback)
- [Code Examples](#code-examples)
- [Learning Path](#learning-path)
- [License](#license)
- [Contributing](#contributing)
- [Support](#support)
- [Contact](#contact)

## Try it now (no install needed)

Click the green button below. GitHub builds a full Python workspace for you in the cloud (this is called a Codespace) with everything already set up. Nothing to download, nothing to configure.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Kubomu/OOP-Python-Tutorials?quickstart=1)

Once it opens:

1. Wait a few seconds for the setup to finish. A small progress scoreboard prints in the terminal.
2. Run any lesson, for example: `python 01_basic_oop_concepts.py`
3. Open `exercises/practice.py` and start solving. Check your progress any time with `python check.py`.

Prefer to work on your own machine instead? See [Installation](#installation) below.

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. Python supports OOP principles such as:

- **Classes and Objects**
- **Encapsulation**
- **Inheritance**
- **Polymorphism**
- **Abstraction**

OOP helps in making code reusable, easier to maintain, and closer to real-world modeling. This repository aims to introduce these concepts step-by-step, with examples to make learning OOP in Python easy and interactive.

## Getting Started

### Prerequisites

If you use the [Try it now](#try-it-now-no-install-needed) button above, you can skip this section entirely.

To work on your own machine you will need:
- **Python 3.6 or higher** installed on your system
  - Check your version: `python --version` or `python3 --version`
  - Download from [python.org](https://www.python.org/downloads/) if needed
- A text editor or IDE (recommended: VS Code, PyCharm, or any editor you are comfortable with)
- Basic understanding of Python fundamentals (variables, functions, loops)

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Kubomu/OOP-Python-Tutorials.git
   cd OOP-Python-Tutorials
   ```

2. **Install the tools used by the exercises (one small package, pytest):**
   ```bash
   pip install -r requirements.txt
   ```
   The lesson files (`01_` through `06_`) use only the Python standard library, so they run without this step. You only need pytest to grade the practice exercises.

### How to Use This Tutorial

1. **Start with the introduction:**
   - Read `00_Intro.md` to understand what OOP is and why it matters

2. **Follow the tutorials in order:**
   - Begin with `01_basic_oop_concepts.py`
   - Progress through each numbered file sequentially
   - Each file builds on concepts from previous lessons

3. **Run the examples:**
   ```bash
   # Run any tutorial file
   python 01_basic_oop_concepts.py

   # Or use python3 if that's your command
   python3 01_basic_oop_concepts.py
   ```

4. **Read the code carefully:**
   - Every file includes detailed comments
   - Docstrings explain what each class and method does
   - Expected outputs are noted in comments

5. **Practise with the self-grading exercises:**
   - Open `exercises/practice.py` and fill in the parts marked `# TODO`
   - See [Interactive practice with instant feedback](#interactive-practice-with-instant-feedback) for how the grading works

## Concepts Covered

### 1. **Classes and Objects**
Learn the basics of classes and objects. Understand how to define a class and instantiate objects in Python.

### 2. **Encapsulation**
Understand how encapsulating data and methods within a class can help protect the internal state of objects.

### 3. **Inheritance**
Learn how classes can inherit attributes and methods from other classes to promote code reuse.

### 4. **Polymorphism**
Understand how polymorphism allows objects to be treated as instances of their parent class, and how method overriding works.

### 5. **Abstraction**
Learn how abstraction hides complex implementation details and shows only essential features to the user.

### 6. **Magic Methods**
Explore Python's built-in methods (dunder methods) that allow you to customize the behavior of your classes.

## Interactive practice with instant feedback

Reading about OOP is one thing. Writing it yourself, and getting told immediately whether you got it right, is how it sticks. That is what the `exercises/` folder is for.

**How it works:**

1. Open `exercises/practice.py`. There is one small exercise for each of the six concepts above. Each one has a `# TODO` where your code goes.
2. Fill in a `# TODO` with your own solution.
3. Ask for a friendly progress report:
   ```bash
   python check.py
   ```
   You will see a scoreboard, one line per topic:
   ```
     [x] 1. Classes and Objects     done
     [ ] 2. Encapsulation           todo
     [ ] 3. Inheritance             todo
     ...
     Solved 1 of 6
   ```
4. Want the full detail on a result? Run the grader directly:
   ```bash
   pytest
   ```
5. Keep going until all six read `done`.

If you get stuck on a topic, open its matching lesson file (`01_` through `06_`) for a worked example, then come back and try again. You cannot break anything, so experiment freely.

**Working in a fork?** When you push your solved `exercises/practice.py` to your own fork, GitHub automatically runs the same grader and shows a green check next to your commit once every exercise passes.

## Code Examples

In this repository, each topic is covered in separate files, including:

- `00_Intro.md` - Introduction to OOP
- `01_basic_oop_concepts.py` - Introduction to classes and objects
- `02_encapsulation.py` - Encapsulation and private attributes
- `03_inheritance.py` - Understanding inheritance in Python
- `04_polymorphism.py` - Using polymorphism for code reusability
- `05_abstraction.py` - Working with abstract base classes
- `06_magic_methods.py` - Understanding magic methods like `__init__`, `__str__`, and `__add__`
- `07_exercises.md` - A written list of extra exercises and two capstone projects
- `exercises/practice.py` - Hands-on, self-grading exercises (start here after the lessons)
- `check.py` - Prints your exercise progress as a simple scoreboard

## Learning Path

Here's the recommended order for working through this repository:

1. **00_Intro.md** - Understand OOP fundamentals and benefits
2. **01_basic_oop_concepts.py** - Classes, objects, and methods
3. **02_encapsulation.py** - Data hiding and access control
4. **03_inheritance.py** - Code reuse through inheritance
5. **04_polymorphism.py** - Flexible code with polymorphism
6. **05_abstraction.py** - Abstract base classes
7. **06_magic_methods.py** - Special methods and operator overloading
8. **exercises/practice.py** - Solve the self-grading exercises, one per concept
9. **07_exercises.md** - Extra written exercises and capstone projects

**Estimated time:** 3 to 5 hours to complete all tutorials and basic exercises.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Here's how you can help:

- **Report bugs** - Open an issue if you find errors in the code
- **Suggest improvements** - Share ideas for better explanations or examples
- **Add exercises** - Propose new practice problems
- **Fix typos** - Submit pull requests for documentation improvements

Please feel free to fork this repository and submit pull requests.

## Support

If you find this tutorial helpful:
- Give it a star on GitHub
- Share it with others learning Python
- Provide feedback through issues or discussions

## Contact

For questions or to share your solutions:
- Open an issue on this repository
- Email: [Kubomuedwin@gmail.com](mailto:Kubomuedwin@gmail.com)

---

Happy coding and learning!
