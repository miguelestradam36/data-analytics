# Managing Data with Python

Make a query from a sql database and save the results in an excel file :file_folder:

![Image](docs/images/pandas_logo.png)

## Managing a sql database

Connect to a localdatabase using python.
This code is not designed for an online database (For example, a mysql database hosted online would not be supported for this code :black_nib: )

![Image](docs/images/sql.png)

### Use logs to save previous queries

All information, like the connection and queries are `logged` in a file for future reference.
There is going to be a new file for each execution done :paperclip:

### Automate some code execution with a MAKEFILE

Automate some command line execution using MAKEFILE.
In this case the MAKEFILE has been programmed with the intention og being able to execute this code in a virtual environment (Not the OS of your computer `in case you use the MAKEFILE, if you do not, the code will be executed on your OS`)

### Save the data you require 

Save the data of your query in an excel file with the name of your choosing