## Making sure dependencias are on the sytem
from scripts_module.setup import SetUpManager
os_handler = SetUpManager()
os_handler.requirements_location = os_handler.os.path.join(os_handler.os.path.dirname(__file__), 'config/list.txt')
##



if __name__ == "__main__":
    return 0