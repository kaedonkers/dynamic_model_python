import numpy as np
import yaml
import json

from .module import Module


class Simulator(object):
    '''
    Class to manage timed calls to modules
    '''
    def __init__(self):
        '''
        Initialise empty attributes
        '''
        self.instance_name = None
        
        # Time
        self.n = 0

        # Modules
        self.modules = {}

        # Parameters

        # Internal states

    def _load_config(self, config_file):
        '''
        Read the configuration file and set parameters
        '''
        # Read the configuration file
        # TODO: Handle JSON and YAML automatically
        with open(config_file) as file:
            config = yaml.full_load(file)[self.instance_name]
        
        # Set parameters
        self.n = config["n"]
        self.modules = config["modules"]


    def initialise(self, instance_name, config_file=None):
        '''
        Initialise the simulation
        '''
        self.instance_name = instance_name
        if not config_file: 
            config_file = "config.yaml"
        self._load_config(config_file)

        for module in self.modules.keys():
            self.modules[module] = Module().initialise(module, config_file) 
        





