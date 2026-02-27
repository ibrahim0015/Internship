from flask import Flask,render_template,request
import os
from huggingface_hub import InferenceClient
import markdown
from markupsafe import Markup

app = Flask(__name__)

@app.route("/")
def input():
    return render_template('form.html')



@app.route('/submit',methods=["POST"])
def output():
    try:
        client = InferenceClient(
            api_key=os.environ["HF_TOKEN"],
        )

        completion = client.chat.completions.create(
            model="Qwen/Qwen3-Coder-Next:novita",
            messages=[
                {
                    "role": "user",
                    "content": f"{request.form['user_input']}"
                }
            ],
        )
        html_output =completion.choices[0].message['content']
        html_output_prettified = Markup(markdown.markdown(html_output))
        return html_output_prettified
    except:
        return "something went wrong!"

    


if __name__== "__main__":
    app.run(debug=True)
