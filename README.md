# TestingAPI_Python
**Python API testing example**  
Пример организации Python API автотестов по тестированию ресурса https://demoqa.com/swagger   
Cтэк: Python + requests + Pytest + Allure. 
 
Для раздела Account выполнено:
- Чек-лист: функциональные проверки, выполнен в Excel-таблице — [ссылка](https://github.com/Badboy5555/TestingAPI_Python/blob/master/API%20%D1%87%D0%B5%D0%BA-%D0%BB%D0%B8%D1%81%D1%82.xlsx)
- Написаны автотесты — [ссылка](https://github.com/Badboy5555/TestingAPI_Python/tree/master/tests)

# Installation
1. Install Python 3.11
2. Clone the project `git clone https://github.com/Badboy5555/TestingAPI_Python.git`
3. Install requirements for project:   
   using CLI navigate to project directory and run command `pip install -r requirements.txt`

# Tests runnig
For run all test, using CLI navigate to project directory, run command: `pip3 -m pytest tests --alluredir=test_results`

# Report 
To generate testrun report, using CLI navigate to project directory, run command: `allure serve test_result`
