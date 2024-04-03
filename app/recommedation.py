from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder="D:\\program file\\semantic_research\\rec_templates")


def get_recommendations(
    location, temperature, sun_hours, date, soil_ph, soil_type, area
):
    # Construct the query parameters for the Trefle API
    params = {
        "location": location,
        "temperature": temperature,
        "sun_hours": sun_hours,
        "date": date,
        "soil_ph": soil_ph,
        "soil_type": soil_type,
        "area": area,
        "token": "1cXcZZ1r5ir9fHWX_KGUaVazygGUl0xiZIZbFyW8_Ag", 
    }

    try:
        # Make a GET request to the Trefle API
        response = requests.get("https://trefle.io/api/plants", params=params)
        data = response.json()

        if "data" in data:
            # Extract plant information from the API response
            plants_data = data["data"]
            recommendations = []

            # Iterate over the plant data and extract relevant information
            for plant_info in plants_data:
                recommendation = {
                    "common_name": plant_info.get("common_name", "N/A"),
                    "scientific_name": plant_info.get("scientific_name", "N/A"),
                    "family": plant_info.get("family_common_name", "N/A"),
                    "native_status": plant_info.get("native_status", "N/A"),
                    # Add more attributes as needed
                }
                recommendations.append(recommendation)

            return recommendations

    except requests.exceptions.RequestException as e:
        print("Error fetching plant information:", e)
        return []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    location = request.form["location"]
    temperature = request.form["temperature"]
    sun_hours = request.form["sun_hours"]
    date = request.form["date"]
    soil_ph = request.form["soil_ph"]
    soil_type = request.form["soil_type"]
    area = request.form["area"]

    # Call the get_recommendations function passing user inputs
    recommendations = get_recommendations(
        location, temperature, sun_hours, date, soil_ph, soil_type, area
    )

    # Pass user input parameters to the result template
    return render_template(
        "result.html",
        recommendations=recommendations,
        location=location,
        temperature=temperature,
        sun_hours=sun_hours,
        date=date,
        soil_ph=soil_ph,
        soil_type=soil_type,
        area=area,
    )


if __name__ == "__main__":
    app.run(debug=True)
