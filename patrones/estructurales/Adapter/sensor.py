class Sensor:
    def temperatura_celsius(self):
        pass


class SensorUSA:
    def fahrenheit(self):
        return 86


class SensorAdapter(Sensor):
    def __init__(self, sensor):
        self.sensor = sensor

    def temperatura_celsius(self):
        f = self.sensor.fahrenheit()

        return (f - 32) * 5 / 9


sensor = SensorAdapter(SensorUSA())
print(sensor.temperatura_celsius())
