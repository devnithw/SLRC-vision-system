import serial
import object_function

# Define serial port and baud rate
serial_port = '/dev/cu.usbmodem1101'  # Replace 'COMX' with your actual port
baud_rate = 9600

# Open serial port
ser = serial.Serial(serial_port, baud_rate)

# Return should be of this format
colour = "green"
# object_type = "cube"


def colurdetection():
    # Define colurdetection function implementation
    pass

try:
    while True:
        # Read data from Arduino
        received_data = ser.readline().decode().strip()
        received_data=int(received_data)


        # Perform actions based on received data
        if received_data == 20000:
            #colour = colurdetection()
            if colour == "green":
                command = '2'
            else:
                command = '3'
            ser.write(command.encode())

        elif received_data == 10000:
            #colour = colurdetection()
            if object_function.get_shape() == "cube":
                command = '2'
            else:
                command = '3'
            ser.write(command.encode())



        # Send command to Arduino

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()  # Close the serial port on keyboard interrupt
