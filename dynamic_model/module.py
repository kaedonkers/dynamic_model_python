import yaml

class Module(object):
    '''Module'''
    def __init__(self):
        '''Initialise empty attributes'''
        self.instance_name = None

        # Initial conditions
        self.y_0 = None

        # Parameters
        self.param = None

        # State variables
        self.y = None

    def _load_config(self, config_file):
        '''Read the configuration file and set parameters'''
        # Read the configuration file
        # TODO: Handle JSON and YAML automatically
        with open(config_file) as file:
            config = yaml.full_load(file)[self.instance_name]
        
        # Set initial conditions
        self.y_0 = config["y_0"]

        # Set parameters
        self.param = config["param"]

    def initialise(self, instance_name, config_file=None):
        '''Initialise instance of class'''
        self.instance_name = instance_name
        if not config_file: 
            config_file = "config.yaml"
        self._load_config(config_file)

    def update_states(self, x):
        '''Update state variables'''
        self.y = self.equation(x)
        return self.y

    def equation(self, x):
        '''Equation'''
        return self.param * x**2