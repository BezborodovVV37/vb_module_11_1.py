import requests

# URL для запроса данных
url = 'https://jsonplaceholder.typicode.com/posts'

# Отправка GET-запроса
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    # Вывод первых пяти записей
    posts = response.json()[:5]
    for post in posts:
        print(f"ID: {post['id']}, Title: {post['title']}")
else:
    print("Ошибка при запросе данных:", response.status_code)
