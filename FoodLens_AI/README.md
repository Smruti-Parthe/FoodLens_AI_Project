# FoodLens AI — Food Image Analyzer & Nutrition Estimator

## Features
- Upload a JPG/PNG food photo.
- Uses a pretrained Food-101 image classifier (`nateraw/food`) to suggest food labels.
- Shows the top 5 predictions and confidence scores.
- Allows the user to correct the nutrition category and enter portion size in grams.
- Estimates calories, protein, carbohydrates, fat, fibre, and sugar using illustrative reference values per 100 g.
- Displays a nutrient chart and allows downloading a CSV summary.

## Important limitation
A photo alone does not reveal exact weight, recipe, ingredients, or cooking oil. Nutrition figures in this educational project are estimates based on a small built-in reference table, scaled to the portion size entered by the user. Do not describe the figures as exact or medically reliable. The classifier may make mistakes; the user should confirm the food category.

## Requirements
- Python 3.10 or 3.11 recommended.
- VS Code with the Python extension.
- Internet connection for installing packages and downloading the AI model the first time.

## Run on Windows in VS Code
Open this folder in VS Code, then open Terminal → New Terminal.

Create a virtual environment:
```powershell
py -3.10 -m venv .venv
```

Activate it:
```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can avoid activation and run the environment's Python directly:
```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run main.py
```

If activation works, install and run:
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run main.py
```

Streamlit should open the app in your browser. If it does not, copy the local URL printed in the terminal (usually http://localhost:8501) into your browser.

## First run
The first run can take several minutes because the pretrained model is downloaded. Keep the terminal open. Later runs should be faster.

## Project algorithm (simple explanation)
1. The user uploads a food image.
2. The pretrained image-classification model processes the image and returns likely food labels with confidence scores.
3. The app maps the top label to a nutrition category; the user can correct it.
4. The user enters portion size in grams.
5. The app scales the reference nutrients using:
   `estimated nutrient = nutrient per 100 g × portion size / 100`
6. The app displays nutrition metrics, a bar chart, and a downloadable CSV.

## Resume wording
"Built a Python-based food image analysis and nutrition estimation web app using a pretrained image classifier, Streamlit, and a nutrition reference table. Implemented user correction, portion-size scaling, visual nutrient summaries, and CSV export."

Be transparent in your presentation: the image model classifies the visible food; the nutrition calculation uses a reference table and user-entered portion size. This version does not directly measure nutrients from pixels.
