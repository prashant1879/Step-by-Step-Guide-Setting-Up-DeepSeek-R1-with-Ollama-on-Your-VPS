from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

# This route renders the index page with the form
@app.route('/')
def home():
    return render_template('index.html')

# This route handles the form submission via POST
@app.route('/query', methods=['POST'])
def query():
    # Get the query input from the form
    user_query = request.form['query']
    
    # Get the response from the ollama chat API
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": user_query}])
    
    # Extract the actual answer from the response and remove <think> tags
    assistant_message = response.get('message', {}).get('content', 'No answer available')
    clean_message = assistant_message.replace("<think>", "").replace("</think>", "").strip()

    # Pass the cleaned response text to the template
    return render_template('index.html', response=clean_message)

if __name__ == '__main__':
    app.run(debug=True)
