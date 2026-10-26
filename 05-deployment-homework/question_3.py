import pickle


with open("pipeline.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)


lead = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}


probability = pipeline.predict_proba([lead])[0, 1]

print(f"Вероятность покупки курса: {probability}")
print(f"Ответ, округлённый до трёх знаков: {probability:.3f}")