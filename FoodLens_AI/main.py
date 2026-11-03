import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="FoodLens AI | Nutrition Analyzer",
    page_icon="🥗",
    layout="wide"
)

# Estimated values per 100 g. These are illustrative reference values,
# not laboratory measurements. Recipes and preparation methods vary.
NUTRITION_DB = {
    "Apple":                 {"calories": 52,  "protein": 0.3,  "carbs": 13.8, "fat": 0.2,  "fiber": 2.4, "sugar": 10.4},
    "Banana":                {"calories": 89,  "protein": 1.1,  "carbs": 22.8, "fat": 0.3,  "fiber": 2.6, "sugar": 12.2},
    "Orange":                {"calories": 47,  "protein": 0.9,  "carbs": 11.8, "fat": 0.1,  "fiber": 2.4, "sugar": 9.4},
    "Rice, cooked":          {"calories": 130, "protein": 2.7,  "carbs": 28.2, "fat": 0.3,  "fiber": 0.4, "sugar": 0.1},
    "Roti / flatbread":      {"calories": 297, "protein": 9.0,  "carbs": 55.0, "fat": 7.5,  "fiber": 7.0, "sugar": 2.0},
    "Dal / lentils, cooked": {"calories": 116, "protein": 9.0,  "carbs": 20.1, "fat": 0.4,  "fiber": 7.9, "sugar": 1.8},
    "Cooked chicken":        {"calories": 165, "protein": 31.0, "carbs": 0.0,  "fat": 3.6,  "fiber": 0.0, "sugar": 0.0},
    "Grilled fish":          {"calories": 150, "protein": 26.0, "carbs": 0.0,  "fat": 5.0,  "fiber": 0.0, "sugar": 0.0},
    "Boiled egg":            {"calories": 155, "protein": 12.6, "carbs": 1.1,  "fat": 10.6, "fiber": 0.0, "sugar": 1.1},
    "Plain yogurt":          {"calories": 61,  "protein": 3.5,  "carbs": 4.7,  "fat": 3.3,  "fiber": 0.0, "sugar": 4.7},
    "Paneer":                {"calories": 265, "protein": 18.3, "carbs": 1.2,  "fat": 20.8, "fiber": 0.0, "sugar": 1.2},
    "Mixed salad":           {"calories": 35,  "protein": 1.5,  "carbs": 7.0,  "fat": 0.4,  "fiber": 2.5, "sugar": 3.5},
    "French fries":          {"calories": 312, "protein": 3.4,  "carbs": 41.4, "fat": 15.0, "fiber": 3.8, "sugar": 0.3},
    "Pizza":                 {"calories": 266, "protein": 11.0, "carbs": 33.0, "fat": 10.0, "fiber": 2.3, "sugar": 3.6},
    "Burger":                {"calories": 295, "protein": 17.0, "carbs": 24.0, "fat": 14.0, "fiber": 1.5, "sugar": 5.0},
    "Pasta, cooked":         {"calories": 158, "protein": 5.8,  "carbs": 30.9, "fat": 0.9,  "fiber": 1.8, "sugar": 0.6},
    "Oatmeal, cooked":       {"calories": 71,  "protein": 2.5,  "carbs": 12.0, "fat": 1.5,  "fiber": 1.7, "sugar": 0.3},
    "Potato, boiled":        {"calories": 87,  "protein": 1.9,  "carbs": 20.1, "fat": 0.1,  "fiber": 1.8, "sugar": 0.9},
    "Chocolate cake":        {"calories": 390, "protein": 5.0,  "carbs": 56.0, "fat": 17.0, "fiber": 2.5, "sugar": 35.0},
    "Ice cream":             {"calories": 207, "protein": 3.5,  "carbs": 24.0, "fat": 11.0, "fiber": 0.7, "sugar": 21.0},
    "Samosa":                {"calories": 300, "protein": 6.0,  "carbs": 32.0, "fat": 17.0, "fiber": 3.0, "sugar": 2.0},
    "Idli":                  {"calories": 146, "protein": 4.0,  "carbs": 30.0, "fat": 0.7,  "fiber": 1.5, "sugar": 0.5},
    "Dosa":                  {"calories": 168, "protein": 4.0,  "carbs": 29.0, "fat": 3.7,  "fiber": 1.5, "sugar": 1.0},
    "Poha":                  {"calories": 130, "protein": 2.5,  "carbs": 25.0, "fat": 2.5,  "fiber": 2.0, "sugar": 1.0},
    "Chole / chickpeas":     {"calories": 164, "protein": 8.9,  "carbs": 27.4, "fat": 2.6,  "fiber": 7.6, "sugar": 4.8},
    "Vegetable curry":       {"calories": 100, "protein": 3.0,  "carbs": 12.0, "fat": 4.0,  "fiber": 3.0, "sugar": 4.0},
    "Sandwich":              {"calories": 250, "protein": 10.0, "carbs": 30.0, "fat": 9.0,  "fiber": 3.0, "sugar": 4.0},
    "Soup":                  {"calories": 45,  "protein": 2.0,  "carbs": 7.0,  "fat": 1.0,  "fiber": 1.5, "sugar": 2.0},
    "Other / unknown food":  {"calories": 180, "protein": 6.0,  "carbs": 22.0, "fat": 7.0,  "fiber": 2.0, "sugar": 4.0},
}

# Map labels from the Food-101 classifier to a nutrition category.
LABEL_MAP = {
    "apple pie": "Other / unknown food",
    "baby back ribs": "Cooked chicken",
    "baklava": "Other / unknown food",
    "beef carpaccio": "Cooked chicken",
    "beef tartare": "Cooked chicken",
    "beet salad": "Mixed salad",
    "bibimbap": "Rice, cooked",
    "bread pudding": "Other / unknown food",
    "breakfast burrito": "Sandwich",
    "bruschetta": "Roti / flatbread",
    "caesar salad": "Mixed salad",
    "caprese salad": "Mixed salad",
    "carrot cake": "Chocolate cake",
    "cheesecake": "Chocolate cake",
    "chicken curry": "Cooked chicken",
    "chicken quesadilla": "Cooked chicken",
    "chicken wings": "Cooked chicken",
    "chocolate cake": "Chocolate cake",
    "chocolate mousse": "Chocolate cake",
    "clam chowder": "Soup",
    "club sandwich": "Sandwich",
    "dumplings": "Other / unknown food",
    "eggs benedict": "Boiled egg",
    "falafel": "Chole / chickpeas",
    "fish and chips": "Grilled fish",
    "french fries": "French fries",
    "french toast": "Roti / flatbread",
    "fried rice": "Rice, cooked",
    "garlic bread": "Roti / flatbread",
    "greek salad": "Mixed salad",
    "grilled cheese sandwich": "Sandwich",
    "grilled salmon": "Grilled fish",
    "guacamole": "Mixed salad",
    "hamburger": "Burger",
    "hot dog": "Sandwich",
    "ice cream": "Ice cream",
    "lasagna": "Pasta, cooked",
    "macaroni and cheese": "Pasta, cooked",
    "omelette": "Boiled egg",
    "onion rings": "French fries",
    "pad thai": "Pasta, cooked",
    "paella": "Rice, cooked",
    "pancakes": "Roti / flatbread",
    "pizza": "Pizza",
    "poutine": "French fries",
    "ramen": "Soup",
    "risotto": "Rice, cooked",
    "samosa": "Samosa",
    "spaghetti bolognese": "Pasta, cooked",
    "spaghetti carbonara": "Pasta, cooked",
    "sushi": "Rice, cooked",
    "tacos": "Sandwich",
    "waffles": "Roti / flatbread",
    "sashimi": "Grilled fish",
}

def normalize_label(label: str) -> str:
    return label.replace("_", " ").replace("-", " ").strip().lower()

def nutrition_category_for_label(label: str) -> str:
    clean = normalize_label(label)
    if clean in LABEL_MAP:
        return LABEL_MAP[clean]

    # Basic keyword matching for common food classes.
    if "banana" in clean:
        return "Banana"
    if "apple" in clean and "pie" not in clean:
        return "Apple"
    if "orange" in clean:
        return "Orange"
    if "pizza" in clean:
        return "Pizza"
    if "burger" in clean or "hamburger" in clean:
        return "Burger"
    if "salad" in clean:
        return "Mixed salad"
    if "chicken" in clean:
        return "Cooked chicken"
    if "fish" in clean or "salmon" in clean or "sashimi" in clean:
        return "Grilled fish"
    if "rice" in clean:
        return "Rice, cooked"
    if "pasta" in clean or "spaghetti" in clean or "lasagna" in clean:
        return "Pasta, cooked"
    if "soup" in clean:
        return "Soup"
    if "fries" in clean or "potato" in clean:
        return "French fries"
    if "ice cream" in clean:
        return "Ice cream"
    if "cake" in clean or "donut" in clean or "donuts" in clean:
        return "Chocolate cake"
    return "Other / unknown food"

@st.cache_resource(show_spinner="Loading the AI food image model. The first run may take a few minutes...")
def load_classifier():
    from transformers import pipeline
    return pipeline(
        task="image-classification",
        model="nateraw/food",
        device=-1
    )

st.title("🥗 FoodLens AI")
st.subheader("Food Image Analyzer & Nutrition Estimator")
st.write(
    "Upload a food photo to get an AI-generated food label and an approximate "
    "nutrition estimate. You can correct the detected food and serving size."
)

with st.sidebar:
    st.header("About this project")
    st.write("**AI technique:** pretrained image classification")
    st.write("**Model:** Food-101 image classifier")
    st.write("**Nutrition:** reference values per 100 g, scaled to the selected portion")
    st.info(
        "This is an educational estimator. It cannot reliably determine exact "
        "ingredients, oil, recipe, or weight from a photo."
    )

uploaded_file = st.file_uploader(
    "Upload a food image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is None:
    st.info("Choose a JPG or PNG image to begin.")
    st.markdown("### Example workflow")
    st.write("1. Upload a food image.")
    st.write("2. Review the AI's top predictions.")
    st.write("3. Confirm the food category and serving size.")
    st.write("4. View estimated nutrition and the chart.")
    st.stop()

try:
    image = Image.open(uploaded_file).convert("RGB")
except Exception:
    st.error("This image could not be opened. Please upload a valid JPG or PNG file.")
    st.stop()

left, right = st.columns([1, 1])
with left:
    st.image(image, caption="Uploaded food image", use_container_width=True)

with right:
    st.markdown("### AI image analysis")
    try:
        classifier = load_classifier()
        predictions = classifier(image, top_k=5)
    except Exception as exc:
        st.error(
            "The AI model could not be loaded. Check your internet connection, "
            "then restart the app. If the error continues, read README.md."
        )
        with st.expander("Technical error details"):
            st.code(str(exc))
        st.stop()

    prediction_df = pd.DataFrame([
        {
            "Predicted food": item["label"].replace("_", " ").title(),
            "Model confidence": f"{item['score'] * 100:.1f}%"
        }
        for item in predictions
    ])
    st.dataframe(prediction_df, use_container_width=True, hide_index=True)

top_label = predictions[0]["label"].replace("_", " ").title()
suggested_category = nutrition_category_for_label(predictions[0]["label"])

st.markdown("---")
st.markdown("### Confirm food and serving size")
st.caption(
    "Image classification may confuse visually similar foods. Select the closest "
    "nutrition category yourself for a more relevant estimate."
)

category_options = list(NUTRITION_DB.keys())
default_index = (
    category_options.index(suggested_category)
    if suggested_category in category_options
    else category_options.index("Other / unknown food")
)

c1, c2 = st.columns([2, 1])
with c1:
    selected_category = st.selectbox(
        "Food / nutrition category",
        options=category_options,
        index=default_index
    )
with c2:
    serving_grams = st.number_input(
        "Serving size (grams)",
        min_value=1,
        max_value=2000,
        value=150,
        step=10
    )

per_100g = NUTRITION_DB[selected_category]
factor = serving_grams / 100.0
estimated = {key: value * factor for key, value in per_100g.items()}

st.markdown("---")
st.markdown("## Estimated nutrition")
st.caption(
    f"Selected category: **{selected_category}** · Portion: **{serving_grams} g**. "
    "Values are estimates and vary by ingredients and cooking method."
)

m1, m2, m3 = st.columns(3)
m1.metric("Calories", f"{estimated['calories']:.0f} kcal")
m2.metric("Protein", f"{estimated['protein']:.1f} g")
m3.metric("Carbohydrates", f"{estimated['carbs']:.1f} g")

m4, m5, m6 = st.columns(3)
m4.metric("Fat", f"{estimated['fat']:.1f} g")
m5.metric("Fibre", f"{estimated['fiber']:.1f} g")
m6.metric("Sugar", f"{estimated['sugar']:.1f} g")

chart_df = pd.DataFrame({
    "Nutrient": ["Protein", "Carbohydrates", "Fat", "Fibre", "Sugar"],
    "Grams": [
        estimated["protein"],
        estimated["carbs"],
        estimated["fat"],
        estimated["fiber"],
        estimated["sugar"]
    ]
})

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.bar(chart_df["Nutrient"], chart_df["Grams"])
ax.set_title(f"Estimated nutrients for {serving_grams} g of {selected_category}")
ax.set_ylabel("Amount (g)")
ax.set_xlabel("Nutrient")
ax.grid(axis="y", linestyle="--", alpha=0.3)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

with st.expander("View calculation details"):
    details_df = pd.DataFrame({
        "Nutrient": ["Calories (kcal)", "Protein (g)", "Carbohydrates (g)", "Fat (g)", "Fibre (g)", "Sugar (g)"],
        "Reference per 100 g": [
            per_100g["calories"], per_100g["protein"], per_100g["carbs"],
            per_100g["fat"], per_100g["fiber"], per_100g["sugar"]
        ],
        f"Estimate for {serving_grams} g": [
            estimated["calories"], estimated["protein"], estimated["carbs"],
            estimated["fat"], estimated["fiber"], estimated["sugar"]
        ]
    })
    st.dataframe(details_df.round(2), use_container_width=True, hide_index=True)
    st.write("Calculation: nutrient estimate = reference value per 100 g × serving size ÷ 100.")

csv_data = pd.DataFrame([{
    "AI_top_prediction": top_label,
    "Selected_food_category": selected_category,
    "Serving_size_g": serving_grams,
    "Calories_kcal_est": round(estimated["calories"], 2),
    "Protein_g_est": round(estimated["protein"], 2),
    "Carbohydrates_g_est": round(estimated["carbs"], 2),
    "Fat_g_est": round(estimated["fat"], 2),
    "Fibre_g_est": round(estimated["fiber"], 2),
    "Sugar_g_est": round(estimated["sugar"], 2),
}]).to_csv(index=False).encode("utf-8")

st.download_button(
    "Download nutrition result as CSV",
    data=csv_data,
    file_name="food_nutrition_estimate.csv",
    mime="text/csv"
)

st.warning(
    "For demonstration and educational use only. The nutrition figures are approximate "
    "reference estimates, not medical advice or a verified analysis of the uploaded meal."
)
