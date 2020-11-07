class BadCSVFile(Exception):
    """
    Error occured while reading the csv file
    """
    pass


class BadQueryParameter(Exception):
    """
    Error occured because query list is empty
    """
    pass
