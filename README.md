#  Documentation

To set up a working environment locally:

1. Create a python virtual environment for the documentation with Python 3.x
2. Clone this repository: `git clone https://github.com/collaborative-open-plant-omics/Documentation.git`
3. Switch to the project (cloned) folder
4. Execute the following command within the virtual environment:
	```python
	pip install -r requirements.txt
	```

5. Write, commit, and push

6. To render locally, in the documentation directory (there should be a _build folder):
	```python
	make html
	```
	To view: `_build/html/index.html`
	
7. There are observable issues when running make, such as "WARNING: html_static_path entry '../_static' does not exist". Creating a _static folder in the root directory should hopefully resolve this.


This documentation uses Sphinx. For more information see: http://dont-be-afraid-to-commit.readthedocs.io/en/latest/documentation.html



