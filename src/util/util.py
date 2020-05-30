'''
Collection of utility classes used throughout the application
'''

'''
Converts an RGB color code to a hexadecimal
color.
'''
def to_hex(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))