# ConnectToTeradata

Steps to Connect Teradata using Python
-----------------------------------------------------------------
Pre-requisites
----------------
1. Teradata tootls and utilities already installed
2. Install Python version 2.7

Steps for windows
-----------------
1. Download the drivers from Teradata website. You will have to register on the website to download. I have kept the drivers in the driver folder. Always download the driver for ther version of TD that you have.
2. Unzip the drivers and run the .exe file. It will run through the installation steps, no changes needed we just need standard installation. These drivers are for windows platform only.
3. Restarting windows is required, although you will not get the prompt for it.
4. Install the Teradata Package for Python. Example - pip install Teradata. If Python 3.6 is installed, then use the command "pip3 install Teradata". This uses pip for python 3.6.
5. Run the script, make necessary changes to the servername, username and password.
6. Password can be input using Teradata Wallet string, instructions in the TD Wallet section.

Steps for linux
-----------------
1. Download the drivers from Teradata website. Always download the driver for ther version of TD that you have. I downloaded for TD version 14.1.
2. Prior to installing the "ODBC Driver for Teradata", the dependency products that are listed. These should already be installed if you have installed Teradata Tools and Utilities.
            1. Shared common components for Internationalization for Teradata (tdicu1410)
            2. Teradata GSS client package                                    (TeraGSS_linux_390)
3. The following command is used to install the "ODBC Driver for Teradata".
            rpm -ivh <rpm package> --nodeps
        where <rpm package> is the rpm package to be installed.  An example of an rpm
        package name is tdodbc-14.10.00.00-1.noarch.rpm.
4. Read the readme that comes along with the download, if any issues with above step.
5. Install the Teradata Package for Python. Example - pip install Teradata
6. Run the script, make necessary changes to the servername, username and password.
7. Password can be input using Teradata Wallet string, instructions in the TD Wallet section.

Script - ConnectToTeradata.py

Authenticating using TD Wallet 
--------------------------------
Download Teradata Wallet for windows tdwallet__windows_x8664.14.10.00.06.zip (https://downloads.teradata.com/download/tools/teradata-wallet-for-windows). Install Teradata wallet like any other basic application program, start up TD wallet and it starts a window like a command prompt and enter the command "add td_password" and then it prompts for the value for the variable. See below.

tdwallet> add td_password
Enter desired value for the item named "td_password":
Item named "td_password" added.

Once this is added as a one time thing, we can then use the variable while logging on to teradata using SQL Assistant or as below in the python script.

session = udaExec.connect(method="odbc", system="servername", username="rahire", password="$$tdwallet(td_password)");