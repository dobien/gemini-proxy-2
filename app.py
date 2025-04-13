from flask import Flask, request, jsonify
import os
# Импорт клиента из google-ai-generativelanguage
from google_ai_generativelanguage import LanguageServiceClient

app = Flask(__name__)

# Инициализация клиента (при необходимости, можно задать дополнительные параметры)
client = LanguageServiceClient()

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "Не передан prompt"}), 400

    try:
        # Вызов API для генерации текста
        # Обратите внимание: синтаксис может отличаться – проверьте [документацию](https://pypi.org/project/google-ai-generativelanguage/)
        response = client.generate_text(prompt=prompt)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # PORT будет задан Render (например, 5000 по умолчанию)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
