import pytest
import os
from core.logger import Logger


@pytest.fixture
def start_mess():
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', os.environ.get("PYTEST_CURRENT_TEST"))
    Logger.get_instance().logger.info(f'Start testing for {os.environ.get("PYTEST_CURRENT_TEST")}')
    yield
    Logger.get_instance().logger.info(f'Finish testing for {os.environ.get("PYTEST_CURRENT_TEST")}')
