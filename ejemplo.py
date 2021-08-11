"""
ejemplo.py
this file is to confirm that we can use
docstring automatic fom shpinx
"""
import pandas as pd
import sys

# Modules
#sys.path.append('C:/Users/candan/Documents/GitHub/datacube/update_datacube/scripts/00_data_wrangling')
#sys.path.append('scripts/00_data_wrangling')
#from table_ramp_up import RampUpData
#from table_block_model import BlockModelData
#from table_dispatch import DispatchData
#from table_tags import TagsData

def function_example(my_name):
    '''
       Return the name from a person

       Parameters
       -----------
       my_name
           a string that indicate a user name

    '''

    data = pd.read_pickle("datahiu/interim/block_model.pkl")

    data.columns
	
    return 'The name is {}'.format(my_name)


class ExampleClass:
    ''' docstring from class exampleClass '''

    def __init__(self, name):
        '''
            this is the init function from class 'exampleClass

            parameters
            ----------
            name
                a string to assign 'name' instance attribute
        '''
        self.name = name

    def abaut_self(self):
        '''
            return information abaut an instance created from exampleClass
        '''

        return 'The instance name is  {}'.format(self.name)

    def sum_number(self):
        '''
            this function return a number
        '''
        number = 5 + 10

        return number
