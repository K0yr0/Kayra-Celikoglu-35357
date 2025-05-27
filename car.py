class Car:
    def __init__(self):
        self.color = "red"          
        self.__engine_status = "off" 

    def display_private_attribute(self):
        print("Engine status:", self.__engine_status)

    def __start_the_engine(self):
        print("Engine started!")
        self.__engine_status = "on"

    def start_the_car(self):
        self.__start_the_engine()