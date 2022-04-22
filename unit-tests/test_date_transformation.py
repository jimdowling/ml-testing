from features import date_transform as dt
from unittest import TestCase
import time
import pytest
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "example_date, excp",
    [('03-31-1970 12:20 59', does_not_raise())
    ,('12-01-2020 09:59 00', does_not_raise())
    ,('13-01-2020 09:59 00', pytest.raises(Exception))]
)    
def test_date_transform(example_date, excp):
    with excp:
        date_as_int = dt.date_string_to_timestamp(example_date)
        intvalue = int(date_as_int)

