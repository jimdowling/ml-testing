from datetime import datetime
 
def date_string_to_timestamp(input_date : str) -> int:
    """ Converts stringified date to a timestamp
    Args:
        input_date (str): The input  
    Returns:
        timestamp (int): The Unix timestamp
    """
    date_format = "%m-%d-%Y %H:%M %S"
    return int(float(datetime.strptime(input_date, date_format).timestamp()) * 1000)

