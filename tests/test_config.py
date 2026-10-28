"""
Test cases for the service configuration
"""
import os
import importlib
from unittest import TestCase
from unittest.mock import patch
from service import config


class TestConfig(TestCase):
    """Configuration Tests"""

    def tearDown(self):
        """Restore the original configuration"""
        importlib.reload(config)

    def test_database_uri_from_environment(self):
        """It should build the DATABASE_URI from the environment variables"""
        env = {
            "DATABASE_USER": "tester",
            "DATABASE_PASSWORD": "secret",
            "DATABASE_NAME": "testdb",
            "DATABASE_HOST": "dbhost",
        }
        with patch.dict(os.environ, env, clear=False):
            os.environ.pop("DATABASE_URI", None)
            importlib.reload(config)
            self.assertEqual(
                config.DATABASE_URI,
                "postgresql://tester:secret@dbhost:5432/testdb",
            )
