from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)


openai.api_key = "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"  

#Моделть поведения 
conversation_history = [
    {"role": "system", "content": "You are a cool assistant who speaks all of the languages in a classy beitish way. Be expressive and real, while staying helpful."}
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
