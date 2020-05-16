from bluezero import microbit

controller = "B8:27:EB:D3:B6:B8"
microbit1 = "D3:CB:9C:01:AF:14"


ubit = microbit.Microbit(adapter_addr = controller,
                         device_addr = microbit1,
                         accelerometer_service = False,
                         button_service = True,
                         led_service = True,
                         magnetometer_service = False,
                         pin_service = True,
                         temperature_service = True)
my_text = 'Hello, world'
ubit.connect()

while my_text is not '':
    ubit.text = my_text
    my_text = input('Enter message: ')

ubit.disconnect()
