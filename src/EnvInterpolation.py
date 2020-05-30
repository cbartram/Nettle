import os
import configparser

'''
Interpolation which expands environment variables in values within an INI file.
Syntax is:

[DEFAULT]
property = $ENV_VAR
'''
class EnvInterpolation(configparser.BasicInterpolation):
    def before_get(self, parser, section, option, value, defaults):
        return os.path.expandvars(value)