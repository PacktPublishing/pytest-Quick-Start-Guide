# pytest-Quick-Start-Guide
pytest Quick Start Guide, published by Packt

This repository contains the source code shown in the pytest Quick Start Guide book.

Many of them can be executed directly to obtain the same results as shown in the book,
except in particular examples for Chapter 5, as they are only sample codes showcasing
code snippets of pytest plugins. 

## Run Examples

* Create a virtual envirnment:

  ```
  $ python3 -m venv .env
  $ source .env/bin/activate
  ```

* Install requirements:
  
  ```
  $ pip install -r requirements.txt
  ```

* Install `pre-commit`  :

  ```
  $ pre-commit install
  ```
  
To run the examples, it is advisable to go into each chapter directory
explicitly and execute `pytest -m pytest` instead of `pytest` directly,
as this will help Python find local modules that might be necessary.
Example:

```
$ cd "Code Bundle/CH3"
$ python -m pytest tests/test_formula.py  
```
