import logging

import boto3 as boto3
import moto as moto

with moto.mock_dynamodb(), moto.mock_sts():
    pass