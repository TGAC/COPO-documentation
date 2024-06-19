#  Collaborative OPen Omics (COPO) 
COPO documentation was created using the Sphinx reStructuredText (reST) markup language. It is hosted on 
[readthedocs.io](https://copo-docs.readthedocs.io).

For more information about Sphinx visit:
http://dont-be-afraid-to-commit.readthedocs.io/en/latest/documentation.html

---

## Getting Started
Clone the COPO **Documentation** GitHub repository: 

$ `git clone https://github.com/collaborative-open-plant-omics/Documentation.git`

## Create a Python virtual environment locally
1. Navigate to the (cloned) project folder

2. Create a Python virtual environment for the documentation with Python 3.x
    $ `sudo apt install python3.10-venv`
    $ `python3 -m venv venv`

3. Activate the virtual environment

    $ `source venv/bin/activate`

4. Execute the following command within the virtual environment:

   $ `pip3 install -r requirements.txt`

5. Write, commit then, push code to the repository

Visit [Configure a virtual environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) to 
learn more about Python virtual environments (if using PyCharm as an IDE).

## Create a Sphinx configuration (if using PyCharm as an IDE)

1. Navigate to Add New Configuration > Python docs
2. Select **Sphinx task**
3. Input following configuration options:
   * Command: `html`
   * Input: `<path to the documentation root directory>`
   * Output:  `<path to the `_build/html` directory>`
   * Python interpreter: `<path to the Python virtual environment>`
   * Working directory:  `<path to the documentation root directory>`

Visit [Run/debug configurations](https://www.jetbrains.com/help/pycharm/run-debug-configuration.html) to learn how to 
create a configuration in PyCharm.

## Upgrade all packages in requirements.txt

1. Install pip-upgrader: $ `pip3 install pip-upgrader`
2. Navigate to the project directory: $ `cd Documentation`
3. Upgrade the packages: $ `pip-upgrade`

---

## Launch COPO Documentation locally
### Public COPO Documentation
To render locally, in the project documentation directory (there should be a _build folder):

 Run the command to build the project: $ `make html`
                                       $ ``sphinx-build -b html . _build/``
 Run the command to do a full build of the project: $ `make clean html`

 To view the web browser, locate and manually open the `index.html` file located at - `_build/html/index.html`

 **e.g.** The web browser (local) full path will be  `http://localhost:63342/documentation/_build/html/index.html` 
 where `63342` is the port number.
	
**OR** 

To render locally with automatic rebuild when changes are made and open the homepage of the generated 
documentation in the default browser:

$ `sphinx-autobuild --open-browser ./ _build/html` or $ `make htmllive`

Server will start at http://127.0.0.1:8000 

**OR** 

To render locally with automatic rebuild when changes are made and open the homepage of the generated 
documentation in the default browser on a specific port:

$ `sphinx-autobuild --port=8002 --open-browser ./ _build/html`

Server will start at http://127.0.0.1:8002

**OR**

To render locally with a spell checker enabled:
$ `sphinx-build -b spelling html/_source _build`

### Internal COPO Documentation

Repeat the steps above but, instead of running the command to build the project, run the command to build the project
with the `htmlinternal` flag: 

$ `make htmlinternal`
$ ``sphinx-build -b html . _buildinternal/``

Full build command: $ `make clean htmlinternal`
View browser:  `_buildinternal/html/index.html` or via `http://localhost:63342/documentation/_buildinternal/html/index.html`
Automatic rebuild: $ `sphinx-autobuild --port=8002 --open-browser ./ _buildinternal/html` or $ `make htmlinternallive`

---

## Potential issues
**Issue #1** (when running the Sphinx project for the first time):

`"WARNING: html_static_path entry '../_static' does not exist"` 

**OR**

`WARNING: html_static_path entry '_static' does not exist`

**Solution #1**: Create a `_static` folder in the project root directory 
                 Command to do so: $ `mkdir _static`
______________________________________________________________________

**Issue #2**: `bash: make: command not found`
**Solution #2**: $ `sudo apt install make`

______________________________________________________________________

**Issue #3**: `OSError: [Errno 98] Address already in use`
**Solution #3**: $ `sudo lsof -i TCP:8002 | grep LISTEN | awk '{print $2}' | xargs kill -9`

NB. `8002` is the port number. The solution above will kill the process running on that port.
______________________________________________________________________

**Issue #4 (Mac)**: `NotOpenSSLWarning: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'`
**Solution #4.1 (Linux)**: Install Enchant C library
                       $ `sudo apt-get install enchant-2`
**Solution #4.2 (Mac)**: Install Enchant C library
                       $ `brew update`
                       $ `brew install enchant`

**NB**: Install [Homebrew](https://brew.sh/) before running the commands above

______________________________________________________________________

**Issue #5 (Mac)**: `Extension error: Could not import extension sphinxcontrib.email (exception: dlopen(~/site-packages/lxml/etree.cpython-39-darwin.so, 0x0002):'`
                    `(mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64e' or 'arm64'))`
**Solution #5 (Mac)**: Force reinstall **lxml** package so that it is assigned to the correct OS architecture
                       $ `pip3 install lxml==5.2.2  --compile --force-reinstall`

**NB**: Find the version of the currently installed **lxml** package: $ `pip3 show lxml`
        The version is displayed by the **Version**
______________________________________________________________________

**Issue #6 (Mac)**: `Could not import extension sphinxcontrib.spelling (exception: The 'enchant' C library was not found and maybe needs to be installed`
**Solution #6 (Mac)**: Downgrade sphinxcontrib.spelling by forcing reinstall of **sphinxcontrib.spelling** package 
                       so that it is assigned to the correct OS architecture
                       $ `pip3 install sphinxcontrib.spelling==7.7.0  --compile --force-reinstall`

**NB**: Find the version of the currently installed **sphinxcontrib.spelling** package: $ `pip3 show sphinxcontrib.spelling`
        The version is displayed by the **Version**

---

## Importing your Documentation into ReadTheDocs
* [Read how to import a Read the Docs project into Read the Docs](https://docs.readthedocs.io/en/stable/intro/import-guide.html)

* [Read how to integrate a .readthedocs.yaml configuration file into a Read the Docs project](https://docs.readthedocs.io/en/stable/config-file/v2.html#)






