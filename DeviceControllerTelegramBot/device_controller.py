from serial import Serial


class Pin:
    def __init__(self, pin_name: str, pin_num: int, pin_type: int = 0) -> None:
        self.name = pin_name
        self.pin = pin_num
        self.pin_type = pin_type
        self.state = 0

    def __str__(self) -> str:
        return f'{self.pin_type}:{self.pin}:{self.state}'

    def __repr__(self) -> str:
        return f'Pin({self.__str__()})'


class DeviceController:
    def __init__(self, devices: dict, serial_comms_conf: dict = None) -> None:
        # map devices to pins
        self.device_pins = dict()
        for device in devices:
            pin_type, pin_num = devices[device]
            device_pin = Pin(
                pin_name=device,
                pin_num=pin_num,
                pin_type=pin_type
            )
            self.device_pins[device] = device_pin

        # configure serial comms
        self.encoding = serial_comms_conf['encoding']
        self.board_comm = Serial(
            serial_comms_conf["PORT"],
            serial_comms_conf["baud_rate"],
            timeout=serial_comms_conf["timeout"]
        )
        print(f"Controlling board pins using PORT {serial_comms_conf['PORT']}")
        

    def update_values(self, command:str):
        self.board_comm.write(command.encode(self.encoding))
