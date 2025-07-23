from crud.tomas.toma import Toma

def test_toma() -> None:
    toma = Toma()
    data = {
        "ubicacion": "Centro",
        "usan_personas": 7
    }
    response = toma.create(data)

    assert response == True

