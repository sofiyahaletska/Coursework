from flask import Flask, request, render_template, redirect, url_for
import main
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route("/" ,methods=['GET', 'POST'])
def home():
    return render_template('main.html')

@app.route("/action" ,methods=['GET', 'POST'])
def action():
    if request.method == "POST":
        input_type_of_chart = request.form['type']
        input_currency = request.form['currency']
        input_info = request.form['info']
        link = draw(input_type_of_chart, input_info, input_currency)
        if input_type_of_chart == "chart":
            redirect("http://127.0.0.1:8050/")
        else:
             return redirect(link)


if __name__ == '__main__':
    app.run_server(debug=True)