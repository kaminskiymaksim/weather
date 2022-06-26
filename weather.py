#!/usr/bin/python3
from pyowm import OWM

owm = OWM('365ff4e5fe75404028238b48ab5f6ae1')

mgr = owm.weather_manager()
observation = mgr.weather_at_place('Nizhniy Novgorod')
w = observation.weather
t = w.temperature("celsius")

t1 = t['temp']
t2 = t['feels_like']
ti = w.reference_time
print(f"In city: {'Nizhniy Novgorod'} \n Temperature now: {t1}°C \n Feel like: {t2}°C \n Weather forecast for: {ti}" )
