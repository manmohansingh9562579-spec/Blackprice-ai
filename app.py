from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Data load
df = pd.read_csv("data.csv")
X = df[["area", "bedrooms", "age"]]
y = df["price"]

# Model train
model = LinearRegression()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        age = int(request.form["age"])

        result = model.predict([[area, bedrooms, age]])
        prediction = round(result[0], 2)

    return render_template("index.html", prediction=prediction)

app.run(host="0.0.0.0", port=10000)