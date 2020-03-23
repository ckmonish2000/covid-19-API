from flask import Flask,jsonify,request,render_template
from scraper import scrape
from totalscrape import totalscrape

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.htm')


@app.route('/total')
def total():
    a=totalscrape()
    return jsonify({"head":"from covid-19-generator","status":200,"body":a})



@app.route('/all')
def all():
    a=scrape()   
    return jsonify({"head":"from covid-19-generator","status":200,"body":a})


@app.route("/country/<string:ctr>")
def test(ctr):
    val=[]
    a=ctr.capitalize()
    print(a)
    b=scrape()
    for x in b:
        if(x['country']==a):
            val.append(x)
            break
        else:
            pass
    return jsonify({"head":"from covid-19-generator","status":200,"body":val})

        

    



if __name__=="__main__":
    app.run()