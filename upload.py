import re
import requests
import os
import http

# from resource import Questions

# question_list = Questions.question_list
# print(question_list)


def send():

    url = 'http://localhost:5000/questions/1' # works

    num = 7
    results = []

    for i in range(num):
        print(f"sending question {i}")
        response = requests.get(url)
        results.append(response.json())

    print("Complete")


def format_questions():
    pass


def batch_upload():
    url = 'http://localhost:5000/api/questions'
    for q in question_list:
        question, answer, alternate1, alternate2, alternate3, subject = q['question'], q['answer'], q['alt_answers'][0], q['alt_answers'][1], q['alt_answers'][2], q['subject']
    
        data = {
          'question': question,
          'answer': answer,
          'alternate1': alternate1,
          'alternate2': alternate2,
          'alternate3': alternate3,
          'subject': subject
        }
        
        res = requests.post(url, json=data)

        print(res.text)

def delete_all():
    count = 0
    while True:
      count += 1
      url = f'http://localhost:5000/api/questions/{count}'
      res = requests.delete(url)
      if res.ok != True:
        break
      else:
        print(res.text)


# batch_upload()
delete_all()
