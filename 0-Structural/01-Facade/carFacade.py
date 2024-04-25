from subsystems.airconditioning import AirConditioning
from subsystems.engine import Engine
from subsystems.lights import Lights


class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.airconditioning = AirConditioning()
        self.lights = Lights()
    def start_car(self):
        self.engine.turn_on()
        self.lights.turn_on()
        self.airconditioning.turn_on()
    def stop_car(self):
        self.engine.turn_off()
        self.lights.turn_off()
        self.airconditioning.turn_off()
