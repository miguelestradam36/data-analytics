## Avoid python Cache
import sys

sys.dont_write_bytecode = True
## Finished the section to avoid python Cache

## -- Making sure dependencias are on the sytem --
from scripts_module.setup import SetUpManager
os_handler = SetUpManager()
os_handler.requirements_location = os_handler.os.path.join(os_handler.os.path.dirname(__file__), 'config/info.yaml')
del os_handler
## -- Making sure dependencias are on the sytem --

## -- Starting the connection to the database --
from scripts_module.sql_connection import SqLiteManager
sqlite_ = SqLiteManager(database="scripts_module/data/CarSalesData.db")
## -- Starting the connection to the database --

if __name__ == "__main__":
    sqlite_.run_query(from_file=False, pandas_dataframe=True, script="SELECT * FROM Invoices")
    sqlite_.dataframe_ = sqlite_.dataframe_.sort_values(['DeliveryCharge'],ascending=True)
    sqlite_.save_in_excel(output="output/output.xlsx")
    sqlite_.print_graphic(title="No title selected",x_axis="ClientID", y_axis="DeliveryCharge", kind="bar")
    del sqlite_
