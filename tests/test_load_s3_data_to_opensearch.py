import unittest
import mock
from load_s3_data_to_opensearch import load_data

class TestLoadData(unittest.TestCase):
    @mock.patch('load_s3_data_to_opensearch.boto3')
    @mock.patch('load_s3_data_to_opensearch.opensearch')
    def test_load_data(self, mock_opensearch, mock_boto3):
        # Test data
        s3_bucket = 'my-bucket'
        s3_key = 'data.json'
        data = {'key': 'value'}

        # Set up mock S3 client
        mock_s3 = mock_boto3.client.return_value
        mock_s3.get_object.return_value = {'Body': data}

        # Set up mock OpenSearch client
        mock_opensearch_client = mock_opensearch.Client.return_value
        mock_opensearch_client.push.return_value = True

        # Test load_data function
        result = load_data(s3_bucket, s3_key)
        self.assertEqual(result, 'Data Loaded')
        mock_s3.get_object.assert_called_with(Bucket=s3_bucket, Key=s3_key)
        mock_opensearch_client.push.assert_called_with(data)

