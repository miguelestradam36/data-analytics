## -- Making sure dependencias are on the sytem --
from scripts_module.setup import SetUpManager
os_handler = SetUpManager()
os_handler.requirements_location = os_handler.os.path.join(os_handler.os.path.dirname(__file__), 'config/info.yaml')
## -- Making sure dependencias are on the sytem --

## -- Starting the connection to the database --
from scripts_module.sql_connection import SqLiteManager
sqlite_ = SqLiteManager(database="scripts_module/data/CarSalesData.db")
## -- Starting the connection to the database --

if __name__ == "__main__":
    sqlite_.dataframe = "SELECT * FROM Invoices"
    sqlite_.run_query(script="SELECT * FROM Invoices")
    print(sqlite_.dataframe_)
    
