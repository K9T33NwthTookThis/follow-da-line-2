ir_val = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
while True:
    left_ir = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
    right_ir = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)

    if left_ir =! ir_val:
        Kitronik_Move_Motor.stop()
        Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.LEFT, 20)

    elif right_ir =! ir_val:
        Kitronik_Move_Motor.stop()
        Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.RIGHT, 20)

    else:
        Kitronik_Move_Motor.stop()
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 30)
