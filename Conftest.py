def pytest_addoption(parser):
    parser.addoption('--browser', default="Chrome")
    parser.addoption('--system',default="Windows")
    parser.addoption('--url',default="test")
