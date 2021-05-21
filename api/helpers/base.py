# Python libraries
import tabula
import pandas as pd
import numpy as np


def check_item(name, model):
    try:
        item = model.objects.get(name=name)
        print(item, 'Already exists')
        return item
    except:
        item = model.objects.create_item(name=name)
        print(item, 'Item created')
        return item


def check_conversion(file):
    # convert pdf to data frame
    df = tabula.read_pdf(file)

    if len(df) <= 0 or None:

        print("File couldn't be converted check input")
        return None

    print('File converted', df)
    return df[0]


def check_variable(var):
    # check if variable is present
    present = False

    # convert pdf to data frame
    if var[1] != '':
        present = True
        print(var[0] + 'is present')
        return present

    print("Couldn't find " + var[0])
    return present
