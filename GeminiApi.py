"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai
import csv
import time

genai.configure(api_key="AIzaSyDxy2HKtvwud733EufRiA5DUj3VG6Gx4qU")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Hãy sinh ra 1 câu có dạng : Hiện tại lớp học đang có {nhãn} bạn đang {nhãn} và 1 câu nhận xét duy nhất dựa trên dòng cuối đoạn dữ liệu sau : \"2 readings,\"\n\"2 readings,\"\n\"2 readings,\"\n\"2 readings,\"\n\"5 sleep, 6 use phone,\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hiện tại lớp học đang có **5** bạn đang **ngủ** và **6** bạn đang **sử dụng điện thoại**.\n\n**Nhận xét:**  Học sinh trong lớp học này dường như không tập trung vào bài học. \n",
      ],
    },
  ]
)


# def remove_text_before_colon(input_file, output_file):
#     with open(input_file, 'r', newline='', encoding='utf-8') as infile:
#         with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
#             reader = csv.reader(infile)
#             writer = csv.writer(outfile)
#             for row in reader:
#                 cleaned_row = [cell.split(':', 1)[-1].strip() if ':' in cell else cell for cell in row]
#                 writer.writerow(cleaned_row)

# Sử dụng hàm
# remove_text_before_colon('runs/detect/exp2/predictions.csv', 'output.csv')

# with open("output.csv", "r") as file:
#     lines = file.readlines()
#     print(len(lines))
#     for i in range(0, len(lines), 30*5):
#         message = "Vấn đề: Dữ liệu đầu vào là các nhãn mà yolo nhận diện được, mỗi dòng dữ liệu tương ứng với các nhãn tìm thấy trong 1 frame. Nếu trong các dòng dữ liệu nhận vào, có dòng nào có dữ liệu bất thường với các dòng khác thì lấy ra dòng đó để thực hiện yêu cầu.Lưu ý: Dữ liệu vào là độc lập, không liên quan đến dữ liệu đã nhập ở lần request trước.Yêu cầu: Sinh ra 1 câu có dạng: Hiện tại {thời gian} đang có {nhãn} người đang {nhãn} và 1 câu nhận xét duy nhất.Dữ liệu:"

#         question = message +"".join(lines[i:i+30*5])
#         # print(question)
#         time.sleep(5)
#         response = chat_session.send_message(question)
#         print(response.text)
        # with open("response.txt", "a") as file:
        #     file.write(response.text + "\n")
def get_response(s):
    question = "Sinh ra một câu duy nhất có dạng: Hiện tại đang có {nhãn} người đang sử dụng {nhãn} để làm ... dựa trên dữ liệu sau:"
    message = question + s
    response = chat_session.send_message(message)
    return response.text
        