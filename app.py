from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        try:
            area = float(request.form["area"])
            bedrooms = int(request.form["bedrooms"])
            age = int(request.form["age"])

            # 🔥 VALIDATION
            if area <= 0:
                prediction = "Area must be greater than 0 ❌"

            elif bedrooms <= 0:
                prediction = "Bedrooms must be at least 1 ❌"

            elif bedrooms > (area / 200):
                prediction = "Too many bedrooms for given area ❌"

            elif age < 0:
                prediction = "Age cannot be negative ❌"

            elif age > 100:
                prediction = "House too old ❌"

            elif area < 300:
                prediction = "Area too small ❌"

            else:
                # 🔥 REALISTIC PRICE CALCULATION
                price = (area * 3000) + (bedrooms * 50000) - (age * 10000)

                # Minimum safeguard
                if price < 500000:
                    price = 500000

                prediction = f"₹ {round(price):,}"

        except:
            prediction = "Invalid input, please enter correct values ❌"

    return render_template("index.html", prediction=prediction)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)