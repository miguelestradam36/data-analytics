class SetUpManager():
    #modules as attributes to facilitate imports
    os = __import__('os') #os module as attribute
    sys = __import__('sys') #sys module as attribute
    logging = __import__('logging')

    #Normal attributes
    requirements_location_ = '' #requirements file location
    required_modules = '' #modules saved in yaml structure

    #------------------------
    # Methods
    #------------------------

    def __init__(self):
        """
        Construction method
        ---
        Params: No arguments/parameters
        Objective: Make sure yaml is available in order to read YAML file
        """
        self.logger = self.logging.getLogger(__name__)
        import time
        self.logging.basicConfig(filename='logs/os_{}.log'.format(time.time()), encoding='utf-8', level=self.logging.DEBUG)
        try:
            self.yaml = __import__('yaml')
            print('Checking {} module into environment...'.format('yaml'))
            print('module {} confirmed on environment'.format('yaml'))
            self.logger.info("YAML already on the system")
        except:
            print('Installing module {}...'.format('pyyaml'))
            self.os.system('pip install {} --quiet'.format('pyyaml'))
            self.yaml = __import__('yaml')
            self.logger.debug("YAML installed in the system, the sytem was not able to detect it")

    @property
    def requirements_location(self):
        """
        Getter method
        ---
        Params: No arguments/parameters
        Objective: Used to define the config file path.
        """
        return self.requirements_location_

    @requirements_location.setter
    def requirements_location(self, file_path:str):
        """
        Setter method
        ---
        Objetive: Can be compared to: 
            pip install -r requirements.txt
        Params:
            param -> file_path: Location of requirements.txt file
            param -> file_path: string      
        """
        print('Checking system...')
        self.requirements_location_ = file_path
        self.logger.debug("READING REQUIREMENTS FROM: {}".format(self.requirements_location_))

        with open(self.requirements_location_, 'r') as file:
            self.required_modules = self.yaml.safe_load(file)
            self.logger.debug("REQUIREMENTS OBTAINED")

        if (self.check_module()):
            self.logger.debug("ALL REQUIREMENTS ARE NOW ON THE SYSTEM")
            print("Environment up to date!")

    def check_module(self)->bool:
        """
        Class Method
        ---
        Objective: Check python module into environment
        Params:
            param -> module: module to be checked
            param -> module: string
        """
        for module in self.required_modules['python']['global']['modules']:
            try:
                print('Checking {} module into environment...'.format(module))
                __import__(module)
                print('module {} confirmed on environment'.format(module))
                self.logger.debug("MODULE {} ALREADY ON FILE".format(module))
            except:
                try:
                    self.os.system('pip install {} --quiet'.format(module))
                    print('Installing module {}...'.format(module))
                    self.logger.debug("MODULE {} INSTALLED".format(module))
                except Exception as error:
                    self.logger.error("NOT ABLE TO INSTALL MODULE {}".format(module))
                    print("\nERROR: {}\n".format(error))
                    return False

        return True
    
    def __del__(self):
        print("Finished setting up dependencies...\n")