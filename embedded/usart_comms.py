import serial
import time
import crcmod

# Configure the serial port
ser = serial.Serial(
    port='COM5',
    baudrate=115200,
    timeout=1 # Timeout for read operations
)

try:
    # Send data
    byte_values = [0x00, 0x01, 0x02, 0x04, 0x05]
    
    # OP byte
    op_byte = [0x06]
    
    byte_sequence = bytes(byte_values) + bytes(op_byte) # Configure the frame
    
    # Create CRC-8 function
    crc8_fun = crcmod.predefined.mkPredefinedCrcFun('crc-8')
    crc = crc8_fun(byte_sequence)
    
    # Prefix with length, excluding length byte
    length_byte = len(byte_sequence) + 1 # +1 for CRC
    
    # Append CRC and length_byte into packet
    packet = bytes([length_byte]) + byte_sequence + bytes([crc])
    
    ser.write(packet) # Serial write
    print(f"Sent bytes with CRC and length byte: {packet}")
    
    time.sleep(0.5)
    
    # Receiving data: Read the length byte
    length_data = ser.read(1)
    if not length_data:
        print("No data received.")
        ser.close()
        exit()
    
    received_msg_length = length_data[0]
    print(f"Expected payload length (including CRC): {received_msg_length}")
    
    # Receiving data: Read the rest of the packet
    received_msg = ser.read(received_msg_length)
    
    byte_list = list(received_msg)
    print(f"Byte list: {[f'{b:#04x}' for b in byte_list]}")
    
    
    if len(byte_list) == received_msg_length:
        received_payload = bytes(byte_list[:-1])
        received_crc = byte_list[-1]
        calculated_crc = crc8_fun(received_payload)
        
        if(received_crc == calculated_crc):
            print("CRC check passed!")
        else:
            print(f"CRC check failed. Expected {calculated_crc:#04x}, received {received_crc:#04x}")
    else:
        print("Not enough data to verify CRC")
    
    operation_byte = byte_list[-2]
    print(f"Operation byte: {operation_byte:#04x}")
    
    received_data = bytes(byte_list[:-2])
    print(f"Received data: {received_data}")
    
except KeyboardInterrupt:
    print("Stopped by user")
    
finally:
    ser.close()
    print("Serial port closed.")
    
