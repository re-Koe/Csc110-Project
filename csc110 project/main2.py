"""
Evaluating the impact of COVID-19 on Canadians’ spending habits: main module

This module is responsible for displaying the main code the user will interact with.

Copyright and Usage Information
===============================
This file is Copyright (c) 2021 Ajinkya Bhosale, Kowshik Mazumdar, Rafael Gacesa, Raiyan Raad.
"""
import visualization

print()
print('∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆')
print('Notice: Please use right click')
print('∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆')
print()

# Before you use pygame make sure to input the start date and end date into the python console
visualization.show_visual()

if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'extra-imports': ['visualization'],
        'max-line-length': 100,
    })

    import doctest

    doctest.testmod()
