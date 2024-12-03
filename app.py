from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)


openai.api_key = "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"  

#Моделть поведения 
conversation_history = [
    {"role": "system", "content": "You are a cool assistant who speaks English in a classy beitish way. Be expressive and real, while staying helpful."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    global conversation_history

    
    data = request.get_json()
    user_query = data.get("query", "")

    conversation_history.append({"role": "user", "content": user_query})

    try:
       
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 
            messages=conversation_history,
            max_tokens=150,
            temperature=0.9
        )

        
        answer = response['choices'][0]['message']['content']
        
        conversation_history.append({"role": "assistant", "content": answer})

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"answer": f"An error occurred: {e}"})

if __name__ == '__main__':
    app.run(debug=True)
