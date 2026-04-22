from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 🔥 City price logic (realistic approx)
def get_rate(city):
    city = city.lower()

    if "mumbai" in city:
        return 12000
    elif "delhi" in city:
        return 8000
    elif "bangalore" in city:
        return 7000
    elif "pune" in city:
        return 6000
    elif "lucknow" in city or "kanpur" in city:
        return 3500
    elif "kannauj" in city or "mainpuri" in city:
        return 2500
    else:
        return 3000  # default


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/home", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        try:
            area = float(request.form.get("area", 0))
            bedrooms = int(request.form.get("bedrooms", 0))
            age = int(request.form.get("age", 0))
            city = request.form.get("city", "")

            # 🔥 VALIDATION (strong)
            if area < 300 or area > 10000:
                prediction = "Area must be between 300–10000 sqft ❌"

            elif bedrooms < 1 or bedrooms > (area // 200):
                prediction = "Invalid bedroom count for given area ❌"

            elif age < 0 or age > 100:
                prediction = "Invalid house age ❌"

            elif city.strip() == "":
                prediction = "Please enter a city ❌"

            else:
                rate = get_rate(city)

                price = area * rate
                price += bedrooms * 500000
                price -= age * 10000

                price = max(price, 500000)

                prediction = f"{round(price / 100000, 2)} Lakhs"

        except:
            prediction = "Invalid input ❌"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)