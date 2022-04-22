from pipeline import feature_pipeline
from unittest import TestCase
import hsfs
import time
import pytest

class HsfsTest(TestCase):
    @pytest.fixture(autouse=True)  # this method is only called once per class - use for common setup
    def init_fs(self):
        # First, you have to create a project on Hopsworks called 'dev'
        self._connection = connect("dev")
        self._fs = self._connection.get_feature_store()
        try:
            fg = fs.get_feature_group("clicks",version=1)
            fg.delete()
        except:
            print("Creating feature group...")

    def test_create_write(self):
        self._df = read_data("sample-click-logs.csv")
        self._df = engineer_features(self._df)
        fg = fs.create_feature_group("clicks",
                        version=1,
                        description="User clicks on our website",
                        primary_key=['id'],
                        online_enabled=True)
        
        fg.insert(self._df)
        # wait 10 secs until data has been written to the online Feature Store
        time.sleep(10) 
        df_read = fg.read(online=True)
        # Validate that the number of rows in the 'clicks' FG is the same as the num of rows in the DF written.
        assert df_read.count() == self._df.count()
        self._connection.close()

