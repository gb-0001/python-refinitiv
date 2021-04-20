import requests as req

url = "https://jsonplaceholder.typicode.com/todos"

res = req.get(url)

message = ''
for todo in res.json():
  if todo['completed']:
    message = 'tâche terminée'
  else:
    message = 'encore du travail...'
  print(todo['title'][:5].upper(), message)
