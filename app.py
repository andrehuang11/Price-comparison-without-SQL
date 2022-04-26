from prices import get_data
from flask import Flask, render_template, request

app = Flask(__name__)

products = get_data()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
        product = request.form.get("product")
        
        if not product:
            return render_template("home.html", products=products)
        
        value = products[product]
        
        return render_template("results.html", value=value, product=product)

    else:
        return render_template("home.html", products=products)

if __name__ == "__main__":
  app.run(port = 8000, debug = False)
