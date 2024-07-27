import ollama
def stage():
  response = ollama.chat(model='llama3', messages=[
    {
      'role': 'user',
      'content': 'Why is the sky blue?',
    },
  ])
  print(response['message']['content'])
  return None