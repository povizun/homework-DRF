# Инструкция по запуску проекта:

1. Убедитесь в наличии `Docker Desktop` на вашем устройстве

2. После развертывания проекта, необходимо создать файл `.env`, в котором указать данные для переменных окружения. Переменные находятся в файле `.env_example`

3. Используется виртуальное окружение - poetry, зависимости записаны в файл `pyproject.toml`

4. Соберите образ и запустите проект при помощи команды: `docker-compose up --build`

5. После запуска сервера в Docker перейдите по ссылке
