import joblib
import numpy as np
try:
    sensor_model = joblib.load("models/sensor_model.pkl")
    terrain_model = joblib.load("models/terrain_model.pkl")
    weather_model = joblib.load("models/weather_model.pkl")
except Exception as e:
    print(e)

def predict_sensor_risk(features):
    features = np.array(features).reshape(1,-1)
    prob = sensor_model.predict_proba(features)[0]
    risk = 0.5 * prob[1] + prob[2]
    return float(risk)
    
def predict_terrain_risk(features):
    features = np.array(features).reshape(1, -1)
    score = -terrain_model.score_samples(features)
    return float(score)

def predict_weather_risk(features):
    features = np.array(features).reshape(1, -1)
    score = -weather_model.score_samples(features)
    return float(score)

def predict_final_risk(terrain_features,weather_features,sensor_features):
    terrain_score = predict_terrain_risk(terrain_features)
    weather_score = predict_weather_risk(weather_features)
    sensor_score = predict_sensor_risk(sensor_features)
    final_score = (0.3 * terrain_score + 0.3 * weather_score + 0.4 * sensor_score)
    return {
        "terrain": round(terrain_score,3),
        "weather": round(weather_score,3),
        "sensor": round(sensor_score,3),
        "final": round(final_score,3)
    }
def risk_category(score):
    if score < 0.3:
        return "LOW"
    elif score < 0.6:
        return "MEDIUM"
    else:
        return "HIGH"