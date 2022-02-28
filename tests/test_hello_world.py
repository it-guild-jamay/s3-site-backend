import unittest
from functions import hello_world

class TestLambdaHandler(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_lambda_handler(self):
        response = hello_world.lambda_handler({},{})
