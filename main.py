import streamlit as st
import plotly.express as px
from backend import get_data

# Widgets: title, text input, slider, select box, sub header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,help="Select the number of days by sliding")

place_cap = place.title()

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} day(s) in {place_cap}")

if place:

    try:
        # Get the temperature or Sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Filter data
            temp = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            # Create a temperature plot
            figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure, use_container_width=True)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("Place does not exist, please try again.")

