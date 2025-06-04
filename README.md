<a name="top"></a>
# COPO Documentation

The Collaborative OPen Omics (COPO) documentation is created using the Sphinx reStructuredText (reST) markup language and is hosted on
[ReadThedocs.io](https://copo-docs.readthedocs.io). It provides a comprehensive overview of the platform, including visual guides, usage instructions, answers to frequently asked questions, and guidance on how to make necessary metadata submissions.

The documentation is available at http://copo-docs.rtfd.io or http://copo-docs.readthedocs.io.

You can access the COPO website at https://copo-project.org and its GitHub repository at https://github.com/TGAC/COPO-production.

For more information about Sphinx, see the [Don’t Be Afraid to Commit guide](http://dont-be-afraid-to-commit.readthedocs.io/en/latest/documentation.html).

---

## Table of Contents 📚

- [Getting Started 🚀](#getting-started)
  1. [Clone the GitHub Repository](#1-clone-the-github-repository)
  1. [Set Up a Python Virtual Environment](#2-set-up-a-python-virtual-environment)
- [PyCharm Configuration (Optional) ⚙️](#pycharm-configuration-optional)
- [Updating Packages 🔄](#updating-packages)
- [Building the Documentation Locally 🧪](#building-the-documentation-locally)
  - [Public Documentation](#public-documentation)
  - [Internal Documentation](#internal-documentation)
- [Common Issues and Fixes 🐞](#common-issues-and-fixes)
  - [Issue 1: \_static folder missing](#issue-1-_static-folder-missing)
  - [Issue 2: make not found](#issue-2-make-not-found)
  - [Issue 3: Port already in use](#issue-3-port-already-in-use)
  - [Issue 4: Enchant C library missing](#issue-4-enchant-c-library-missing)
  - [Issue 5: lxml incompatible on Mac (ARM64)](#issue-5-lxml-incompatible-on-mac-arm64)
  - [Issue 6: sphinxcontrib.spelling architecture issue](#issue-6-sphinxcontribspelling-architecture-issue)
  - [Issue 7: Environment not reflecting updates](#issue-7-environment-not-reflecting-updates)
- [Publishing to ReadTheDocs 📦](#publishing-to-readthedocs)

---

## Getting Started

### 1. Clone the GitHub repository

```bash
git clone https://github.com/TGAC/COPO-documentation.git
cd COPO-documentation
```

### 2. Set Up a Python Virtual Environment

```bash
sudo apt install python3.10-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

To learn more, see: [Creating a virtual environment (PyCharm)](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)

#### 2.1 Check for broken dependencies (optional)

```bash
pip3 check
```
> **Note**: This command checks for broken dependencies in the installed packages. If there are any issues, you may 
> need to resolve them before proceeding.
---

## PyCharm Configuration (Optional)

To use PyCharm’s Sphinx task runner:

1. Go to **Add New Configuration** > **Python docs**
1. Select **Sphinx task**
1. Fill in the configuration:
   - Command: `html`
   - Input: `<path to the documentation root directory>`
   - Output: `<path to _build/html>`
   - Python interpreter: `<path to the Python virtual environment>`
   - Working directory: `<path to the documentation root>`

More information: [Run/debug configurations in PyCharm](https://www.jetbrains.com/help/pycharm/run-debug-configuration.html)

---

## Updating Packages

To update the packages in the `requirements.txt` file, use `pip-upgrader` which allows packages to be updated interactively.

```bash
pip3 install pip-upgrader
cd COPO-documentation
pip-upgrade
```

---

## Building the Documentation Locally

### Public Documentation

**Build the documentation**

```bash
make html
# or
sphinx-build -b html . _build/
```

**Clean build**

```bash
make clean html
```

**View the docs locally by opening `_build/html/index.html` in a browser, or use the following commands**

```bash
sphinx-autobuild --open-browser ./ _build/html
# or
make htmllive
# or with a port
sphinx-autobuild --port=8002 --open-browser ./ _build/html
```

> **Note**:
> - If the `index.html` is launched then the web browser (local) full path will be `http://  localhost:63342/documentation/_build/html/index.html` where `63342` is the port number.
> - Server will start at http://127.0.0.1:8000 with port `8000` by default unless specified otherwise.

**Enable spell checking**

```bash
sphinx-build -b spelling html/_source _build
```

> **Note**: This renders the project locally with spell checker enabled

### Internal Documentation

**To build internal docs**

```bash
make htmlinternal
# or
sphinx-build -b html . _buildinternal/
```

**Clean and build**

```bash
make clean htmlinternal
```

**Auto-build and serve**

```bash
sphinx-autobuild --port=8002 --open-browser ./ _buildinternal/html
```

**View browser**

- To view the web browser, locate and manually open the `index.html` file
  located at `_buildinternal/html/index.html`

- To view the web browser (local) full path will be:
  `http://localhost:63342/documentation/_buildinternal/html/index.html`

---

## Common Issues and Fixes

### Issue #1: \_static folder missing

    WARNING: html_static_path entry '_static' does not exist

**Fix**:

```bash
mkdir _static
```

**Note**: This creates the `_static` folder in the documentation root directory, which is required for static files used by Sphinx.

---

### Issue #2: make not found

    bash: make: command not found

**Fix**:

```bash
sudo apt install make
```

> **Note**: This installs the `make` utility, which is required to build the documentation.

---

### Issue #3: Port already in use

    OSError: [Errno 98] Address already in use

**Fix**:

```bash
sudo lsof -i TCP:8002 | grep LISTEN | awk '{print $2}' | xargs kill -9
```

> **Note**: `8002` is the port number. The solution above will kill the process running on that port.

---

### Issue #4: Enchant C library missing

    NotOpenSSLWarning: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'

**Fix**:

#### Linux

```bash
sudo apt-get install enchant-2
```

#### Mac

```bash
brew update
brew install enchant
```

> **Note**: Install [Homebrew](https://brew.sh/) before running the Mac commands. 
> The fixes describe how to install Enchant C library

---

### Issue #5: lxml incompatible on Mac (ARM64)

    Extension error: Could not import extension sphinxcontrib.email (exception: dlopen(~/site-packages/lxml/etree.cpython-39-darwin.so, 0x0002): (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64e' or 'arm64')))

**Fix**:

#### Linux

```bash
pip3 install lxml==5.2.2  --compile --force-reinstall
```

#### Mac

```bash
brew update
brew install enchant
```

> **Note**: Force reinstall **lxml** package so that it is assigned to the correct OS architecture. 
> To find the version of the currently installed **lxml** package, run `pip3 show lxml` 
  in the terminal. The version is displayed by the **Version**.

---

### Issue #6: sphinxcontrib.spelling architecture issue

    Could not import extension sphinxcontrib.spelling (exception: The 'enchant' C library was not found and maybe needs to be installed)

**Fix**:

```bash
pip3 install sphinxcontrib.spelling==7.7.0  --compile --force-reinstall
```

> **Note**:
> - This fix downgrades the `sphinxcontrib.spelling` package by forcing reinstall of `sphinxcontrib.spelling` package
>   so that it is assigned to the correct OS architecture.
> - To find the version of the currently installed `sphinxcontrib.spelling` package, run - `pip3 show sphinxcontrib.spelling`.
>   The version is displayed by the **Version**.

---

### Issue #7: Environment not reflecting updates

    Requirements are not installing or old package versions are still being recognised despite being upgraded

**Fix**:

```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

> **Note**: This deletes the `venv` directory file (if it exists) from the project directory then, recreates the `venv` virtual environment and install the requirements.

---

## Publishing to ReadTheDocs

- [How to import a project](https://docs.readthedocs.io/en/stable/intro/import-guide.html)

- [Using .readthedocs.yaml](https://docs.readthedocs.io/en/stable/config-file/v2.html#)

<br> <br> 
<p align="right"><a href="#top">Back to top&nbsp;&nbsp;⬆️</a></p>