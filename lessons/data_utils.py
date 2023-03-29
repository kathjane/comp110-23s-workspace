"""Data utils"""

from csv import DictReader 
#a built in csv function to read dictionaries

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)

    file_handle.close()
    return result

def column_vals(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table under a specific header"""
    result: list[str] = []
    # step through table 
    for row in table:
        # save every value under the key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str,str]]) -> dict[str,list]:
    """Reformats our data so that it is a dictionary with colmn headers as keys"""
    result: dict[str,list[str]] = {}
    # loop through keys of one row of table 
    first_row: dict[str,str] = table[0]
    for key in first_row: 
        # for each key, make a dict entry with all column values
        result[key] = column_vals(table, key)
    return result

