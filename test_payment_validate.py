from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

payload = {
    "card_number":"79927398713234567",
    "cvv": "343",
    "expiry_date": "2023-09",
    "card_name" : "Agughalam Davis"
}

def test_valid_cvv():
    response = client.post("/payment/validate", data=json.dumps(payload))
    assert response.status_code == 200

def test_card_number_with_valid_luhn():
    payload["card_number"] = "79927398713234567"
    response = client.post("/payment/validate", data=json.dumps(payload))
    assert response.status_code == 200

def test_valid_expiry_date():
    payload["expiry_date"] = "2023-10"
    response = client.post("/payment/validate", data=json.dumps(payload))
    assert response.status_code == 200

def test_valid_cvv_with_amex_pan():
    payload["card_number"] = "34927398713234562"
    payload["cvv"] = "2344"
    response = client.post("/payment/validate", data=json.dumps(payload))
    assert response.status_code == 200

def test_invalid_expiry_date():
    payload["expiry_date"] = "2023-08"
    response = client.post("/payment/validate", data=json.dumps(payload))
    assert response.status_code == 422

def test_invalid_cvv():
    payload["cvv"] = "23456"
    response = client.post("/payment/validate", data=json.dumps(payload))
    assert response.status_code == 422

def test_invalid_cvv_with_amex_pan():
    payload["card_number"] = "34927398713234562"
    payload["cvv"] = "234"
    response = client.post("/payment/validate", data=json.dumps(payload))
    assert response.status_code == 422

def test_invalid_card_number_length():
    payload["card_number"] = "37927398"
    response = client.post("/payment/validate", data=json.dumps(payload))
    assert response.status_code == 422

def test_card_number_with_invalid_luhn():
    payload["card_number"] = "3792739871323456"
    response = client.post("/payment/validate", data=json.dumps(payload))
    assert response.status_code == 422





    