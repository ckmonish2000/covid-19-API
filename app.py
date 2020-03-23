from flask import Flask,jsonify,request
from scraper import scrape

app=Flask(__name__)

@app.route("/")
def index():
    return "Welcome To Covid-19-API-Generator"


@app.route('/all')
def total():
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

        

    return "works"



if __name__=="__main__":
    app.run()