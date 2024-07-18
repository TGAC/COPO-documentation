.. _copo-project-setup-windows:

Set Up COPO Project on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Option 1: Using Ubuntu Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set up Ubuntu terminal on Windows by enabling the **Windows Subsystem for Linux** through the following steps.

# Navigate to Control Panel-->Programs--> Turn Windows Features On Or Off
# Enable the **Windows Subsystem for Linux** option in the list
#  Click the **OK** button
#  Click **Restart now** when you’re prompted to restart your computer
# Open Microsoft Store (MS) from the **Start** menu, and search for **Linux** in the store or open this
`link <https://www.microsoft.com/store/productId/9N6SVWS3RX71>`__ to find the Ubuntu app on MS store:
# Click **Get the apps** under the **Linux on Windows?** banner.
# Search and click Ubuntu Linux distribution to get "Get" or "Install" it
# Launch Ubuntu app


.. note::
    The first time that the Linux environment is launched, one is prompted to enter a UNIX username and password.
    These don’t have to match your Windows username and password, but will be used within the Linux environment.

.. hint::
   In the Ubuntu terminal (which can be found in the Microsoft Store or from the **Start** menu or by searching for
   **Ubuntu** using the search bar):

   * To copy text: highlight desired text then, ``right-click``
   * To paste text: ``right-click``


.. warning::
    * **Error #1**: 0x800701bc WSL 2 requires an update to its kernel component. For information please
      visit https://aka.ms/wsl2kernel
      **Solution**: Go to Manual installation steps for older versions of WSL | Microsoft Docs to download WSL 2Set
      WSL 2 as default version: wsl --set-default-version 2

    * **Error #2**: WslRegisterDistribution failed with error: 0x80370102. Error: 0x80370102 The virtual machine
      could not be started because a required feature is not installed.

      **Solution**:

      * Run Windows PowerShell under Administrator rights (Right-click the Windows 10 Start button and
        select “Windows PowerShell (Admin)"
      * Copy-paste the following command:
      * Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
      * Restart the PC or laptop

.. raw:: html

   <hr>

Option 2: Using Windows Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::

   * Commands are entered in the command prompt
   * Cloning a GitHub repository enables the branches to show and gives access to committing, pushing etc to the
     remote repository
   * Repeat steps 1 to 19 under Ubuntu section in setting up COPO project on Ubuntu

.. hint::

   * To open the command prompt in Windows, open the **Start menu** and search for ``cmd.``. Press **Enter** or click
     the result to open a command window or ``right-click`` the option to run it as an administrator
   * To view all environment variables in the terminal:C:\Users\<username> SET

#. Download and install Python:
#. Download PyCharm: Python IDE for Professional Developers by JetBrains
#. Install Django: >``py -m pip3 install Django``
#. Download `PyCharm IDE for Professional Edition <https://www.jetbrains.com/pycharm/download/#section=linux>`__:
#. Setup PyCharm Professional with a JetBrains account and a school email
#. Add/Authorise GitHub account to PyCharm

#. Clone the `COPO project GitHub repository <https://github.com/TGAC/COPO-production>`__ instead of
   downloading it as a ``.zip`` file from the GitHub repository

#. Open the cloned COPO project in PyCharm
#. In PyCharm, add a new configuration by navigating to - Add Configurations->Add new->Django Server

#. Set up or copy and paste environment variables in the following four places in PyCharm:
   * Edit Configurations
   * File->Settings->Build, Execution, Deployment->Console->Python console
   * File->Settings->Build, Execution, Deployment->Console->Django console
   * File->Settings->Languages & Frameworks->Django->Enable Django

#. Set system environment variables
   * On the Windows taskbar, ``right-click`` the Windows icon and select **System**.
   * In the **Settings** window, under R**elated Settings**, click **Advanced system settings**.
   * On the **Advanced** tab, click **Environment Variables**
   * Click **New* to create a new environment variable
   * Click **Edit** to modify an existing environment variable
   * After creating or modifying the environment variable, click **Apply** and then, **OK** to have the change take effect

.. centered:: **OR**

Set environment variables in the terminal
* To set environment variables in the terminal replace "export" with "set"

**e.g.** Replace > ``export ENVIRONMENT_TYPE="dev"`` with > ``set ENVIRONMENT_TYPE="dev"``