from app import main

def test_order_total(monkeypatch):
    monkeypatch.setattr(main, "get_stock", lambda item: 5)
    r = main.app.test_client().get("/order/laptop/1")
    assert r.status_code == 200
    assert r.get_json()["total"] == 974.25

def test_insufficient_stock(monkeypatch):
    monkeypatch.setattr(main, "get_stock", lambda item: 0)
    assert main.app.test_client().get("/order/laptop/1").status_code == 409