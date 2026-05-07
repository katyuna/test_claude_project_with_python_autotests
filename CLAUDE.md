# my_python_tets_project — Автотесты

## Стек
- Python 3.11+
- pytest — основной фреймворк
- Selenium / Playwright — UI тесты
- requests / httpx — API тесты
- Allure — отчёты
- GitHub Actions — CI/CD (.github/)

## Структура проекта

```
my_python_tets_project/
├── .github/          ← CI/CD пайплайны (GitHub Actions)
├── .venv/            ← виртуальное окружение (не трогать)
├── api/              ← вспомогательный код для API (клиенты, хелперы)
├── data/             ← тестовые данные (JSON, константы)
├── pages/            ← Page Object классы для UI тестов
│   └── base_page.py  ← базовый класс, наследуй от него
├── tests/
│   ├── api/          ← API тесты
│   ├── ui/           ← UI тесты
│   │   └── conftest.py  ← фикстуры для UI (браузер, драйвер)
│   └── __init__.py
├── conftest.py       ← глобальные фикстуры для всех тестов
├── .gitignore
├── requirements.txt
└── README.md
```

## Команды

```bash
# Запуск всех тестов
pytest tests/

# Только UI тесты
pytest tests/ui/

# Только API тесты
pytest tests/api/

# С Allure отчётом
pytest tests/ --alluredir=allure-results
allure serve allure-results

# С покрытием
pytest tests/ --cov=. --cov-report=html

# Параллельный запуск
pytest tests/ -n auto
```

## Правила написания тестов

### Обязательно
- Следуй паттерну **Arrange-Act-Assert** в каждом тесте
- UI логика — только в классах папки `pages/`, не в тестах
- Новые Page Object классы наследуй от `base_page.py`
- Фикстуры для UI — в `tests/ui/conftest.py`
- Глобальные фикстуры (браузер, клиент) — в корневом `conftest.py`
- Тестовые данные храни в папке `data/`
- Добавляй **Allure-аннотации**: `@allure.feature`, `@allure.story`, `@allure.step`
- Используй **type hints** для всех функций и фикстур
- Имена: `snake_case` для функций/переменных, `PascalCase` для классов

### Запрещено
- НИКОГДА не запускай тесты не сохранив файл
- НИКОГДА не удаляй файлы тестов
- Не коммить закомментированные тесты
- Не использовать `from module import *`
- Не хранить URL, логины, пароли в коде — только в `.env`
- Не трогать `.venv/` — только через pip/requirements.txt
- `time.sleep()` — запрещено, использовать явные ожидания

## Page Object правила
```python
# pages/base_page.py — базовый класс, наследуй от него
class BasePage:
    def __init__(self, driver):
        self.driver = driver

# pages/новая_страница.py — новый Page Object
class NewPage(BasePage):
    LOCATOR = (By.ID, "element-id")  # локаторы внутри класса

    @allure.step("Описание действия")
    def do_something(self):
        ...
```

## Фикстуры
- `conftest.py` (корень) — браузер, API клиент, общие данные (scope=session)
- `tests/ui/conftest.py` — фикстуры специфичные для UI тестов
- Тестовые данные берём из `data/`

## GitHub Actions CI
- Тесты запускаются автоматически на push и pull request
- Allure отчёт публикуется как артефакт
- Воркфлоу в `.github/` — не менять без необходимости
- Секреты хранятся в GitHub Secrets

## Что нельзя трогать
- `.venv/` — виртуальное окружение
- `.github/` — CI конфигурация (только по согласованию)
- `conftest.py` корневой — согласовывать изменения
- `.gitignore` — не менять без необходимости

## .gitignore (должно быть)
```
.env
.venv/
allure-results/
allure-report/
.pytest_cache/
htmlcov/
__pycache__/
*.pyc
```