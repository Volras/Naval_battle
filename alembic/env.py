from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Импортируйте следующие модули
from sqlalchemy.ext.declarative import declarative_base
import sys
import os
sys.path.append(os.getcwd())  # Добавляет корень проекта в PYTHONPATH

# Импортируйте вашу базу данных и модели
from your_application.database import Base  # Измените на ваш путь к базе данных
from your_application import models  # Измените на ваш путь к моделям

# Этот вызов позволяет Alembic использовать файлы конфигурации
fileConfig(config.config_file_name)

# Настройка моделей для автогенерации миграций
target_metadata = Base.metadata

def run_migrations_offline():
    # Этот блок кода остается без изменений
    ...

def run_migrations_online():
    # В этом блоке устанавливается соединение с базой данных
    ...

# Остальная часть файла остается без изменений