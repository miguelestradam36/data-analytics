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
        print('Starting SqLite services...')
        if database != "":
            print('connecting to database...')
            self.connection = self.sqlite3.connect(database)
            self.cursor = self.connection.cursor()
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
            print('connecting to database...')
            self.connection = self.sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            print('connection to database started...')
        except Exception as error:
            print("\nERROR: {}\n".format(error))

    @property
    def dataframe(self):
        """
        Getter method
        ---
        Objective: returns database path location.
        Params: No arguments/parameters
        """
        return self.dataframe_

    @dataframe.setter
    def dataframe(self, script:str):
        """

        """
        try:
            self.dataframe_ = self.pandas.read_sql_query(script, self.connection)
        except Exception as error:
            print("\nERROR: {}\n".format(error))

    def run_query(self, from_file:bool=False, pandas_dataframe:bool=False, script:str="SELECT * FROM Invoices")->None:
        """
        Setter method
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
            #finish: reading sql file

            #Decide wether to execute with pandas or sqlite
            if pandas_dataframe:
                self.dataframe = script
            else:  
                self.cursor.execute(script)
                print('\n',self.cursor.fetchall(),'\n')
                #Saving changes
                if self.save_changes():
                    print('commited action...')
                else:
                    raise Exception
                #finish: saving changes
                
            #finish: pandas or sqlite

        except Exception as error:
            print("\nERROR: {}\n".format(error))

    def save_in_excel(self, output:str)->None:
        """
        Class method
        ---
        Output: boolean value returned
        Params: No arguments/parameters
        Objective: Changes into SqLite database have to be commited in order to be saved.  
        """
        try:
            # writing to Excel
            datatoexcel = self.pandas.ExcelWriter(output)
            # write DataFrame to excel
            self.dataframe_.to_excel(datatoexcel, index=False)
            # save the excel
            datatoexcel.close()
            print("Excel file created...")
        except Exception as error:
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
            return True
        except Exception as error:
            print("\nERROR: {}\n".format(error))
        return False

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
        except Exception as error:
            print("\nERROR: {}\n".format(error))