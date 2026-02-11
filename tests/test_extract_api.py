"""
Tests unitaires pour ExtractApi avec pytest.
"""
import pandas as pd
from services.extract_api import ExtractApi

class TestExtractApi:
    """Tests pour ExtractApi."""

    def test_execute_success(self, mocker):
        """Test d'une extraction API réussie."""

        mock_df = pd.DataFrame({
            'heure_utc': ['2024'],
            'temperature': [20],
            'humidite': [50],
            'pression': [1000]
        })
        mocker.patch('pandas.read_csv', return_value=mock_df)

        extractor = ExtractApi("http://url")
        dataframe = extractor.execute()

        assert dataframe.empty is False
        assert 'temperature' in dataframe.columns
