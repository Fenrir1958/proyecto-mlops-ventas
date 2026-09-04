import subprocess
import os
import joblib

def test_train_genera_modelo():
    resultado = subprocess.run(
        ["python", "src/train.py"],
        capture_output=True, text=True
    )
    assert resultado.returncode == 0
    assert os.path.exists("models/modelo.pkl")

    modelo = joblib.load("models/modelo.pkl")
    assert hasattr(modelo, "predict")