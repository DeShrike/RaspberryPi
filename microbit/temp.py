from bluezero import microbit, device

controller_address = "B8:27:EB:D3:B6:B8"
device_address = "DD:82:10:FF:52:5E" # gizup
# device_address = "D3:CB:9C:01:AF:14" # pigot


# device = device.Device(adapter_addr = controller_address,
#                        device_addr = device_address)

# print("Connecting")
# device.connect()
# print("Connected")
# print("Name: ", device.name)
# print("Alias: ", device.alias)
# print("Address: ", device.address)
# print("Disconnecting")
# device.disconnect()
# print("Disconnected")


ubit = microbit.Microbit(adapter_addr = controller_address,
                         device_addr = device_address,
                         accelerometer_service = False,
                         button_service = True,
                         led_service = True,
                         magnetometer_service = False,
                         pin_service = True,
                         temperature_service = True)

print("Connecting")
ubit.connect()
print("Connected")
print("Reading temperature")
print("Temperature:", ubit.temperature)
print("Setting Pixels")

for i in range(10):
  ubit.pixels = [0b10001, 0b01010, 0b00100, 0b01010, 0b10001]
  ubit.pixels = [0b00100, 0b01010, 0b00100, 0b00100, 0b00100]
print("Disconnecting")
ubit.disconnect()
print("Disconnected")


