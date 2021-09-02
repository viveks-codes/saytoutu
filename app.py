from flask import Flask, request, render_template,url_for
from os import listdir
import pandas as pd
app = Flask(__name__)



@app.route('/index.html')
def my_form():
    return render_template('index.html')
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route("/saytoutu.html")
def saytoutu():
    return render_template('saytoutu.html')
@app.route("/reload")
def reload():
	addallconfessions()
	return "thay gayu bhai!!!!!"
@app.route("/thankyou.html")
def thankyou():
	return render_template('thankyou.html')
@app.route("/rules.html")
def rules():
    return render_template('rules.html')
@app.route("/view.html")
def view():
	gurl = "https://docs.google.com/spreadsheets/d/1QyRJTNd1eIOxjQXzOkhHnAfEvmZGTIix45fF24ylfck/gviz/tq?tqx=out:csv&sheet=confession"
	#dataframe data
	df = pd.read_csv(gurl)
	#drop duplicates (preprocessing)
	df.drop_duplicates(subset ="confession",keep = "last", inplace = True)
	df["year"].fillna("9", inplace = True)
	df['year'] = df['year'].astype(int)
	df['dept'] = df['dept'].replace(['FALSE'],['Not want to mention'])
	#preprocessing end
	df = df.reset_index(drop=True)
	df = df.reindex(index=df.index[::-1])
	df = df.values.tolist()
	return render_template('view.html',df=df)
@app.route('/', methods=['POST'])
def my_form_post():
	input_nopol = request.form['text_box']
	if request.method == 'POST':
			lines.append(input_nopol)
			print(lines)
	return render_template('index.html', nopol=input_nopol)


if __name__ == '__main__':
	app.debug = True;
	app.run()
        

