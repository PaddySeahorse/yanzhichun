# 中文助手 API (TinyLlama)

Fork 自 https://github.com/jzhang38/TinyLlama，基于 TinyLlama-1.1B 的对话型助手 API，支持中文客服和问答。

## 使用方法
- 端点：`POST /chat`
- 请求：`{"message": "你好", "history": []}`
- 响应：`{"response": "您好！有什么可以帮助您的？", ...}`

## 技术细节
- 模型：TinyLlama-1.1B-Chat-v1.0
- 部署：Railway.app / 本地 / Hugging Face Spaces
- 许可：Apache 2.0