# TestingAPI_Python
**Python API testing example**  
This project implemets Python API autotests for https://demoqa.com/swagger   
A tech stack: Python + requests + Pydantic + Pytest + Allure
 
 For "Account" section were made:
- Check-list: functional checks (Excel-table) — [link](https://github.com/Badboy5555/TestingAPI_Python/blob/master/API%20%D1%87%D0%B5%D0%BA-%D0%BB%D0%B8%D1%81%D1%82.xlsx)
- Autotests — [link](https://github.com/Badboy5555/TestingAPI_Python/tree/master/tests)

**Advanced features**  
1. Pre-commit configs for code logic and code style validation via [link]():
- Isort [link]()
- Black [link]()
- Flake [link]()
- Mypy [link]()
2. GitHub Actions config [link]()
3. Dockerfile config [link]()


# Installation
1. Install Python 3.11
2. Clone the project `git clone https://github.com/Badboy5555/TestingAPI_Python.git`
3. Install requirements for project:   
   using CLI, navigate to project directory and run command `pip install -r requirements.txt`

# Tests runnig
To run all test, using CLI navigate to project directory and run command: `python -m pytest tests --alluredir=allure-results`

# Report 
To generate testrun report, using CLI, navigate to project directory and run command: `allure serve allure-results`

