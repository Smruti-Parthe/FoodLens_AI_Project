# 🍎 FoodLens AI – Smart Food Image Analyzer & Nutrition Estimator

## 📌 Project Overview

FoodLens AI is a Python-based application that analyzes food images and provides estimated nutritional information. It uses a pretrained image classification model to identify food items and calculates nutritional values based on the selected food category and serving size.

The application helps users understand the nutritional content of their meals through a simple and interactive interface.

## 🎯 Problem Statement

People often find it difficult to track the nutritional content of their daily meals. Manually searching for calories and nutritional values can be time-consuming.

FoodLens AI aims to simplify this process by allowing users to upload a food image and receive an estimated nutritional breakdown.

## ✨ Key Features

- **Food Image Upload:** Upload an image of a food item for analysis.
- **Food Recognition:** Uses a pretrained image classification model to predict the food category.
- **Serving Size Input:** Enter the serving quantity in grams.
- **Nutrition Estimation:** Displays estimated:
  - Calories
  - Protein
  - Carbohydrates
  - Fat
  - Fibre
  - Sugar
- **Visual Representation:** Displays nutritional information using charts.
- **CSV Export:** Allows users to download nutritional results for future reference.
- **Interactive Interface:** Simple and user-friendly interface developed using Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Hugging Face Transformers | Pretrained image classification |
| Pandas | Nutritional data handling |
| Matplotlib | Data visualization |

## ⚙️ Working Process

1. The user uploads an image of a food item.
2. The pretrained image classification model analyzes the image and predicts the food category.
3. The user enters the serving size in grams.
4. The application retrieves the corresponding nutritional reference values.
5. Nutritional values are adjusted according to the serving size.
6. Results are displayed through nutritional summaries and charts.
7. Users can export the results as a CSV file.

## 🧠 Model & Approach

FoodLens AI uses a pretrained image classification model available through Hugging Face Transformers.

**Approach:**
- Image Classification for food category prediction.
- Reference-Based Nutrition Estimation for nutritional calculations.
- Serving-Size Scaling to calculate estimated nutritional values according to the entered quantity.

The project uses a built-in nutritional reference table rather than directly measuring nutrients from the image.

## 📂 Project Structure

```text
FoodLens-AI/
│
├── main.py
├── requirements.txt
└── README.md
```

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd FoodLens-AI
```

### 3. Create a Virtual Environment

```bash
py -3.10 -m venv .venv
```

### 4. Install Dependencies

```bash
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
.\.venv\Scripts\python.exe -m streamlit run main.py
```

### 6. Open in Browser

The application will be available at:

```text
http://localhost:8501
```

## 📊 Expected Output

The application provides:
- Predicted food category.
- Estimated nutritional values based on serving size.
- Visual nutritional charts.
- CSV file containing nutritional results.

## ⚠️ Limitations

- Nutritional values are estimates and may differ from actual food composition.
- Food recognition depends on the accuracy of the image classification model.
- The estimation uses predefined nutritional reference values.
- Actual nutritional content can vary depending on ingredients and preparation methods.

## 🔮 Future Enhancements

- Support for identifying multiple food items in a single image.
- Integration with a larger nutritional database.
- Improved food recognition accuracy.
- Personalized daily nutrition tracking.
- User accounts and meal history.

## 👩‍💻 Developed By

**Smruti Parthe**

Computer Engineering Diploma Student

**Project:** FoodLens AI – Smart Food Image Analyzer & Nutrition Estimator

---

*FoodLens AI – Making nutritional awareness simpler, one meal at a time.*
