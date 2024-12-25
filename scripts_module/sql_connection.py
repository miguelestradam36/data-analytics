class SqLiteManager():

    #module as attribute to facilitate imports
    sqlite3 = __import__('sqlite3') #sqlite3 module as attribute
    pandas = __import__('pandas') #pandas module as attribute
    logging = __import__('logging')
    sys = __import__('sys')

    #------------------------
    # Methods
    #------------------------
    
    def __init__(self, database:str=""):
        """
        Function that initializes class
        ---
        Objective: Flags the start of process
        Params: No arguments/parameters
        """
        self.logger = self.logging.getLogger(__name__)

        print('Starting SqLite services...')

        if database != "":
            print('connecting to database...')
            self.connection = self.sqlite3.connect(database)
            self.cursor = self.connection.cursor()
            self.logger.info("DATABASE PATH: {}".format(database))
            self.logger.debug("Connection to database established")
            print('connection to database started...')

    @property
    def database(self):
        """
        Getter method
        ---
        Objective: returns database path location.
        Params: No arguments/parameters
        """
        return self.database_

    @database.setter
    def database(self, db_path:str):
        """
        Setter method
        ---
        Objective: Called to define the connection to SqLite connection
        Params:
            param -> db_path: Location of database into which we are going to write/get our data.
            param -> db_path: string       
        """
        try:
            self.database_ = db_path
            self.logger.info("DATABASE PATH: {}".format(self.database_))
            print('connecting to database...')
            self.connection = self.sqlite3.connect(self.database)
            self.logger.debug("Connection to database established")
            self.cursor = self.connection.cursor()
            print('connection to database started...')
        except Exception as error:
            self.logger.error("EXECUTION ERROR-> {} and message: {}".format(error.__class__.__name__, error))
            print("\nERROR: {}\n".format(error))

    @property
    def dataframe(self):
        """
        Getter method
        ---
        Objective: returns panda dataframe.
        Params: No arguments/parameters
        """
        return self.dataframe_

    @dataframe.setter
    def dataframe(self, script:str):
        """
        Setter method
        ---
        Objective: returns panda dataframe.
        Params: script which is a string with a sql query
        """
        try:
            self.dataframe_ = self.pandas.read_sql_query(script, self.connection)
            self.logger.debug("SQL LINE: {} EXECUTED IN DATABASE".format(script))
        except Exception as error:
            self.logger.error("EXECUTION ERROR-> {} and message: {}".format(error.__class__.__name__, error))
            print("\nERROR: {}\n".format(error))

    def run_query(self, from_file:bool=False, pandas_dataframe:bool=False, script:str="SELECT * FROM Invoices")->None:
        """
        Method
        ---
        Objective: Called to define the connection to SqLite connection
        Params:
            param -> db_path -> description: 
            param -> db_path -> type: string
            param -> db_path -> default: 'SHOW TABLES;'

            param -> db_path -> description: 
            param -> db_path -> type: bool
            param -> db_path -> default: False
        """
        try:
            #change variable content if the sql is on a file
            if from_file:
                with open(script, 'r') as sql_file:
                    script = sql_file.read()
                    self.logger.debug("QUERY TAKEN FROM FILE")
            #finish: reading sql file

            #Decide wether to execute with pandas or sqlite
            if pandas_dataframe:
                self.dataframe = script
                self.logger.debug("QUERY EXECUTED AND DATA SAVED ON A PANDAS DATAFRAME")
            else:  
                self.cursor.execute(script)
                print('\n',self.cursor.fetchall(),'\n')
                self.logger.debug("QUERY EXECUTED")
                #Saving changes
                if self.save_changes():
                    print('commited action...')
                else:
                    raise Exception
                #finish: saving changes
                
            #finish: pandas or sqlite

        except Exception as error:
            self.logger.error("EXECUTION ERROR-> {} and message: {}".format(error.__class__.__name__, error))
            print("\nERROR: {}\n".format(error))

    def save_in_excel(self, output:str)->None:
        """
        Class method
        ---
        Output: boolean value returned
        Params: Output string
        Objective: Changes into SqLite database have to be commited in order to be saved.  
        """
        try:
            # writing to Excel
            datatoexcel = self.pandas.ExcelWriter(output)
            # write DataFrame to excel
            self.dataframe_.to_excel(datatoexcel, index=False)
            # save the excel
            datatoexcel.close()
            self.logger.debug("QUERY SAVED IN FILE: {}".format(output))
            print("Excel file created...")
        except Exception as error:
            self.logger.error("EXECUTION ERROR-> {} and message: {}".format(error.__class__.__name__, error))
            print("\nERROR: {}\n".format(error))

    def save_changes(self)->bool:
        """
        Class method
        ---
        Output: boolean value returned
        Params: No arguments/parameters
        Objective: Changes into SqLite database have to be commited in order to be saved.  
        """
        try:
            print('Automatically saving changes...')
            self.connection.commit()
            self.logger.info("SCRIPT COMMITED IN DATABASE")
            return True
        except Exception as error:
            self.logger.error("EXECUTION ERROR-> {} and message: {}".format(error.__class__.__name__, error))
            print("\nERROR: {}\n".format(error))
        return False

    def print_graphic(self, x_axis:str, y_axis:str, kind:str, title:str="No title selected")->None:
        """
        Method
        ---
        Objective: Called to define the connection to SqLite connection
        Params:
            param -> db_path -> description: 
            param -> db_path -> type: string
            param -> db_path -> default: 'SHOW TABLES;'

            param -> db_path -> description: 
            param -> db_path -> type: bool
            param -> db_path -> default: False
        """
        try:
            import time
            import matplotlib.pyplot as plt
            self.dataframe_.plot(x=x_axis, y=y_axis, kind=kind)
            figure = plt.gcf()
            figure.savefig('plot_{}.png'.format(time.time()))
            plt.show()
            plt.draw()
            self.logger.debug("AN IMAGE HAS BEEN DONE WITH THE RESULTS OF YOUR QUERY. Y_AXIS: {} AND X_AXIS: {}".format(y_axis, x_axis))
        except Exception as error:
            self.logger.error("EXECUTION ERROR-> {} and message: {}".format(error.__class__.__name__, error))
            print("\nERROR: {}\n".format(error))

    def __del__(self):
        """
        Deletion method, this is done automatically once all the tasks have been executed
        ---
        Params: No arguments/parameters
        Objective: In this case, the changes done to the database will be automatically commited and the connection closed.
        """
        try:
            self.save_changes()
            self.cursor.close()
            self.logger.debug("DELETED OBJECT RESPONSABLE TO THE CONNECTION TO THE DATABASE")
        except Exception as error:
            self.logger.error("EXECUTION ERROR-> {} and message: {}".format(error.__class__.__name__, error))
            print("\nERROR: {}\n".format(error))