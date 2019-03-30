from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form action="/" method="post">
                <label for="rot">Rotate by: </label>
                <input id="rot" type="text" name="rot" value="0" />
                <br>
                <label for="text"></label>
                <textarea id="text" name="text" rows="5" cols="30">{0}
                </textarea>
                <input type="submit" value="Submit Query" />

            </form>
        </body>
    </html>
    """        

### encrypt
@app.route("/", methods=['POST'])
def encrypt():
    loc_rot = int(request.form['rot'])
    loc_text = request.form['text']

    encrypt_sent = rotate_string(loc_text,loc_rot)
    return form.format(encrypt_sent)


@app.route("/")
def index():
    return form.format(' ')


app.run()