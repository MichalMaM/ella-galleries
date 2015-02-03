"""
In this package, You can find test environment for Ella galleries unittest project.
As only true unittest and "unittest" (test testing programming unit, but using
database et al) are there, there is not much setup around.
"""
import os
import django

test_runner = None
old_config = None

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_ella_galleries.settings'

def setup():
    global test_runner
    global old_config
    try:
        from django.test.runner import DiscoverRunner as TestRunner
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner as TestRunner
    try:
        django.setup()
    except AttributeError:
        pass
    test_runner = TestRunner()
    test_runner.setup_test_environment()
    old_config = test_runner.setup_databases()

def teardown():
    test_runner.teardown_databases(old_config)
    test_runner.teardown_test_environment()
