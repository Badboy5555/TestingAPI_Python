import pytest
import os
from core.logger import Logger


@pytest.fixture(scope='function', autouse=True)
def start_mess():
    Logger.get_instance().logger.info(f'Start testing for {os.environ.get("PYTEST_CURRENT_TEST")}')
    yield
    Logger.get_instance().logger.info(f'Finish testing for {os.environ.get("PYTEST_CURRENT_TEST")}')


