#  Collaborative OPen Omics (COPO) 
COPO documentation was created using the Sphinx reStructuredText (reST) markup language which is hosted on 
[readthedocs.io](https://copo-project.readthedocs.io).

The documentation uses Sphinx. For more information visit:
http://dont-be-afraid-to-commit.readthedocs.io/en/latest/documentation.html

## Getting Started
Clone the COPO **Documentation** GitHub repository: 

$ `git clone https://github.com/collaborative-open-plant-omics/Documentation.git`

## Create a Python virtual environment locally
1. Navigate to the (cloned) project folder

2. Create a Python virtual environment for the documentation with Python 3.x

    $ `python3 -m venv venv`

3. Execute the following command within the virtual environment:

   $ `pip3 install -r requirements.txt`

4. Write, commit then, push code to the repository

Visit [Configure a virtual environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) to 
learn more about Python virtual environments (if using PyCharm as an IDE).

## Create a Sphinx configuration (if using PyCharm as an IDE)

1. Navigate to Add New Configuration > Python docs
2. Selec **Sphinx task**
3. Input following configuration options:
   * Command: `html`
   * Input: `<path to the documentation root directory>`
   * Output:  `<path to the `_build/html` directory>`
   * Python interpreter: `<path to the Python virtual environment>`
   * Working directory:  `<path to the documentation root directory>`

Visit [Run/debug configurations](https://www.jetbrains.com/help/pycharm/run-debug-configuration.html) to learn how to 
create a configuration in PyCharm.
    
## Launch COPO Documenation locally

To render locally, in the project documentation directory (there should be a _build folder):

 Run the command to build the project: $ `make html`
 Run the command to do a full build of the project: $ `make clean html`

 To view the web browser, locate and manually open the `index.html` file located at - `_build/html/index.html`

 **e.g.** The web browser (local) full path will be  `http://localhost:63342/documentation/_build/html/index.html` 
 where `63342` is the port number.
	
**OR** 

To render locally with automatic rebuild when changes are made and open the homepage of the generated 
documentation in the default browser:

$ `sphinx-autobuild --open-browser ./ _build/html`

Server will start at http://127.0.0.1:8000 

**OR** 

To render locally with automatic rebuild when changes are made and open the homepage of the generated 
documentation in the default browser on a specific port:

$ `sphinx-autobuild --port=8001 --open-browser ./ _build/html`

Server will start at http://127.0.0.1:8001

**OR**

To render locally with a spell checker enabled:
$ `sphinx-build -b spelling html/_source _build`

## Potenial issues
**Issue** (when running the Sphinx project for the first time):

`"WARNING: html_static_path entry '../_static' does not exist"`

**Solution**: Create a `_static` folder in the project root directory






