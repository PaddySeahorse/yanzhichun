FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r chat_gradio/requirements.txt
CMD ["python", "chat_gradio/app.py"]