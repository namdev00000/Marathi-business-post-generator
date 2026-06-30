import os
import json
from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    if request.method == "POST":
        product_name = request.form["product_name"]
        price = request.form["price"]
        extra = request.form["extra"]

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Product: {product_name}, Price: {price}, Extra: {extra}. Generate a structured output in JSON format with the following keys: 'facebook_post', 'instagram_caption', and 'whatsapp_message'. Each key should contain a relevant message for the product in Marathi Language."
        )

        text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(text)

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)