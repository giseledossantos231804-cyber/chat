from flask import Flask, request, jsonify, render_template
from google.cloud import dialogflow
import os
import uuid

app = Flask(**name**)

# ==========================================

# CONFIGURAÇÕES DO DIALOGFLOW

# ==========================================

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")

LANGUAGE_CODE = "pt-BR"

# ==========================================

# PÁGINA PRINCIPAL

# ==========================================

@app.route("/")
def home():
return render_template("index.html")

# ==========================================

# CHAT

# ==========================================

@app.route("/chat", methods=["POST"])
def chat():

```
try:

    # Recebe os dados enviados pelo HTML

    data = request.get_json()

    mensagem = data.get("mensagem", "").strip()

    if not mensagem:

        return jsonify({
            "erro": "Mensagem vazia."
        }), 400


    # ==========================================
    # CRIA UMA SESSÃO PARA O USUÁRIO
    # ==========================================

    session_id = str(uuid.uuid4())


    # ==========================================
    # CLIENTE DO DIALOGFLOW
    # ==========================================

    session_client = dialogflow.SessionsClient()


    # Cria o caminho da sessão

    session = session_client.session_path(
        PROJECT_ID,
        session_id
    )


    # ==========================================
    # PREPARA A MENSAGEM
    # ==========================================

    text_input = dialogflow.TextInput(
        text=mensagem,
        language_code=LANGUAGE_CODE
    )


    query_input = dialogflow.QueryInput(
        text=text_input
    )


    # ==========================================
    # ENVIA PARA O DIALOGFLOW
    # ==========================================

    response = session_client.detect_intent(
        request={
            "session": session,
            "query_input": query_input
        }
    )


    # ==========================================
    # PEGA A RESPOSTA
    # ==========================================

    query_result = response.query_result

    resposta = query_result.fulfillment_text


    # Caso não exista resposta configurada

    if not resposta:

        resposta = "Desculpe, não consegui encontrar uma resposta."


    # ==========================================
    # RETORNA PARA O HTML
    # ==========================================

    return jsonify({
        "resposta": resposta
    })


except Exception as erro:

    print("Erro:", erro)

    return jsonify({
        "erro": "Ocorreu um erro ao conversar com o assistente."
    }), 500
```

# ==========================================

# WEBHOOK DO DIALOGFLOW

# ==========================================

@app.route("/webhook", methods=["POST"])
def webhook():

```
data = request.get_json()

intent = data["queryResult"]["intent"]["displayName"]


if intent == "horario_atendimento":

    resposta = "Nosso horário de atendimento é das 9h às 20h."


elif intent == "Localizacao":

    resposta = "Estamos localizados na Rua Principal, nº 146."


elif intent == "Formas_Pagamento":

    resposta = "Aceitamos Pix, cartão de crédito e cartão de débito."


else:

    resposta = f"Recebi a Intent: {intent}"


return jsonify({

    "fulfillmentMessages": [

        {

            "text": {

                "text": [resposta]

            }

        }

    ]

})
```

# ==========================================

# EXECUÇÃO

# ==========================================

if **name** == "**main**":

```
app.run(
    host="0.0.0.0",
    port=8080,
    debug=True
)
```
