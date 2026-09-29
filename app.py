from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Webhook do Dialogflow funcionando!"


@app.route("/webhook", methods=["POST"])
def webhook():

    # Recebe os dados enviados pelo Dialogflow
    data = request.get_json()

    # Descobre qual Intent foi acionada
    intent = data["queryResult"]["intent"]["displayName"]

    # Define a resposta
    if intent == "horario_atendimento":
        resposta = "Nosso horário de atendimento é das 9h às 20h."

    elif intent == "Localizacao":
        resposta = "Estamos localizados na Rua Principal, n 146."

    elif intent == "Formas_Pagamento":
        resposta = "Aceitamos Pix, cartão de crédito e cartão de débito."

    else:
        resposta = f"Recebi a Intent: {intent}"

    # Devolve a resposta para o Dialogflow
    return jsonify({
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [resposta]
                }
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)