from pipeline import feature_pipeline
from unittest import TestCase
import hsfs
import pytest

class HsfsTest(TestCase):

    def test_create_write(self):
        self._connection = feature_pipeline.connect(host="791bb4a0-bb1c-11ec-8721-7bd8cdac0b54.cloud.hopsworks.ai",project="dev")
        self._fs = self._connection.get_feature_store()
        df = feature_pipeline.read_data("sample-click-logs.csv")
        df = feature_pipeline.engineer_features(df)
        try:
            fg = self._fs.get_feature_group("clicks",version=1)
        except:
            fg = self._fs.create_feature_group("clicks",
                        description="User clicks on our website",
                        primary_key=['id'],
                        online_enabled=True)
        
        fg.insert(df)
        df_read = fg.read(online=True)
        # Validate that the number of rows in the 'clicks' FG is the same as the num of rows in the DF written.
        assert df_read.count() == df.count()
        self._connection.close()

