from flask import Flask, render_template, request
import requests

app = Flask(__name__)

EXCHANGE_RATE_API = "https://api.apilayer.com/exchangerates_data/latest"
API_KEY = "YOUR_EXCHANGE_RATE_API_KEY"

@app.route("/", methods=["GET", "POST"])
def forex_converter():
    if request.method == "POST":
        amount = float(request.form.get("amount"))
        source_currency = request.form.get("source_currency")
        target_currency = request.form.get("target_currency")
        
        response = requests.get(EXCHANGE_RATE_API, params={"apikey": API_KEY})
        data = response.json()
        
        if data.get("success"):
            exchange_rates = data["rates"]
            if source_currency in exchange_rates and target_currency in exchange_rates:
                source_rate = exchange_rates[source_currency]
                target_rate = exchange_rates[target_currency]
                converted_amount = (amount / source_rate) * target_rate
                return render_template(
                    "converter.html",
                    converted=True,
                    source_currency=source_currency,
                    target_currency=target_currency,
                    amount=amount,
                    converted_amount=converted_amount
                )
            else:
                return "Invalid currency codes."
        else:
            return "Failed to fetch exchange rates."
    
    return render_template("converter.html", converted=False)

if __name__ == "__main__":
    app.run(debug=True)