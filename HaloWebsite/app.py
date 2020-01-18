from flask import Flask, request, render_template, flash
import sys
from processing import do_calculation
from balance import pause
from flask.ext.scss import Scss


#balance = pause()
app = Flask(__name__)
Scss(app)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
	
	
    
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])
        if number1 is not None and number2 is not None:
            result = do_calculation(number1, number2)
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)


    return '''
        <html>
            <body>
                {errors}
                <p>Enter your numbers:</p>
                <form method="post" action=".">
                    <p><input name="number1" /></p>
                    <p><input name="number2" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)


@app.route('/balance')
def my_form():
    return render_template('my-from.html')

@app.route('/balance', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = pause(text)
    print("TEST")
    return processed_text





if __name__ == '__main__':
   app.run()