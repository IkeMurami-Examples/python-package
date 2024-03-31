# python-package

Python distribution package configuration example

## Что за задача

В [документации](https://packaging.python.org/en/latest) по созданию пакетов нету примеров по настройке проекта для работы со сложной структурой [namespace](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/)'ов и [плагинов](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/). Поэтому я создал этот репозиторий, чтобы потренироваться в настройках.

Я создал легкий проект, используя [src-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) структуру проекта:

```
.
├── .gitignore
├── LICENSE.txt
├── README.md
├── src
│   ├── first-package-namespace    # Неймспейс
│   |   ├── plugins                # Плагины
│   |   │   └── myplugin           # Пакет-плагин
│   |   │       ├── __init__.py
|   |   |       └── main.py
│   |   ├── subpkg1                # Пакет
│   |   │   ├── __init__.py
│   |   │   └── main.py
│   |   └── subpkg2
|   |       ├── __init__.py
│   |       └── main.py
│   └── second-package-namespace    # Неймспейс
│       ├── subpkg1
│       │   ├── __init__.py
│       │   └── main.py
│       └── subpkg3
|           ├── __init__.py
│           └── main.py
├── tools                           # Кодогенерация
│   └── generate.py
└── usage-example                   # Использование пакетов и плагинов
    └── main.py
```

Задача:

1. [+] Настройть сборку проекта (добавив pyproject.toml)
2. [+] Добавить кодогенерацию
3. [+] Добавить поддержку плагинов
4. [ ] Добавить тесты
5. [ ] Добавить линтер
6. [ ] Добавить форматтер
7. [ ] Добавить статическую проверку типов

Стек:

- hatch & hatchling
- pytest
- flake8
- mypy
- black
- isort
- pep8
- ruff (как альтернатива flake8 + black)
