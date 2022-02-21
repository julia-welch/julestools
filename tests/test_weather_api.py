from julestools.weather_api import search_city, weather_forecast

def test_search_city():
    assert len(search_city('Paris')) != 0

def test_weather_forecast():
    assert len(weather_forecast(551801)) == 6

def test_main_weather(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "Vienna")

    # go about using input() like you normally would:
    i = input("City?\n> ")

    assert i == "Vienna"
