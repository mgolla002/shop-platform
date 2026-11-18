from app.main import app

def test_stock():
    r = app.test_client().get("/stock/Laptop")
    assert r.status_code == 200
    assert r.get_json()["stock"] == 5

def test_unknown():
    assert app.test_client().get("/stock/phone").status_code == 404