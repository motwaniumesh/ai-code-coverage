
import pytest

import os

from unittest.mock import MagicMock  

from src.app import app;

from flask import json
 
@pytest.fixture

def client():

    app.config['TESTING'] = True

    with app.test_client() as client:

        yield client
 