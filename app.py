# import streamlit as st
# import pickle
# import pandas as pd

# # Load trained model
# # with open("model.pkl", "rb") as file:
# #     model = pickle.load(file)

# st.write("App started")

# with open("model.pkl", "rb") as file:
#     model = pickle.load(file)

# st.write("Model loaded successfully")

# # App title
# st.title("🏠 House Price Prediction")

# st.write("Enter the property details below:")

# # Binary Features
# prefarea = st.selectbox(
#     "Preferred Area",
#     ["No", "Yes"]
# )

# airconditioning = st.selectbox(
#     "Air Conditioning",
#     ["No", "Yes"]
# )

# # Numerical Features
# area = st.number_input(
#     "Area (sq ft)",
#     min_value=0.0,
#     value=0.0,
#     step=1.0
# )

# bedrooms = st.number_input(
#     "Bedrooms",
#     min_value=0,
#     value=0,
#     step=1
# )

# bathrooms = st.number_input(
#     "Bathrooms",
#     min_value=0,
#     value=0,
#     step=1
# )

# stories = st.number_input(
#     "Stories",
#     min_value=0,
#     value=0,
#     step=1
# )

# parking = st.number_input(
#     "Parking Spaces",
#     min_value=0,
#     value=0,
#     step=1
# )

# # Predict Button
# if st.button("Predict Price"):

#     prefarea_yes = 1 if prefarea == "Yes" else 0
#     airconditioning_yes = 1 if airconditioning == "Yes" else 0

#     input_data = pd.DataFrame(
#         [[
#             prefarea_yes,
#             airconditioning_yes,
#             area,
#             bedrooms,
#             bathrooms,
#             stories,
#             parking
#         ]],
#         columns=[
#             'prefarea_yes',
#             'airconditioning_yes',
#             'area',
#             'bedrooms',
#             'bathrooms',
#             'stories',
#             'parking'
#         ]
#     )

#     prediction = model.predict(input_data)

#     st.success(
#         f"💰 Predicted House Price: ₹ {prediction[0]:,.2f}"
#     )





import streamlit as st
import pickle
import pandas as pd

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.write("Model loaded")

st.write("Intercept:", model.intercept_)
st.write("Coefficients:", model.coef_)

test_input = [[1, 1, 1000, 3, 2, 1, 1]]

prediction = model.predict(test_input)

st.write("Prediction:", prediction)