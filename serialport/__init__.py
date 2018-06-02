from serial import Serial
from serial import serialutil
from datetime import datetime

class SerialPortNotFoundException(Exception):
    pass

class SerialReadTimeoutException(Exception):
    pass

class SerialPort:
    debug=False
    windows_ports=['com1','com2','com3','com4','com5','com6','com7','com8']
    linux_ports=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyUSB0','/dev/ttyUSB1']

    @staticmethod
    def write_debug(message):
        if SerialPort.debug:
            print('{now} : {message}'.format(now=datetime.now(),message=message))
    
    @staticmethod
    def find(ports=[],baud_rate=9600):
        if len(ports)==0:
            ports=SerialPort.windows_ports+SerialPort.linux_ports
        for port in ports:
            try:
                SerialPort.write_debug('Finding serial device in port "{port}"'.format(port=port))
                return SerialPort(port,baud_rate)
            except serialutil.SerialException:
                pass
            SerialPort.write_debug('Any serial device was detected on the available ports')
        raise SerialPortNotFoundException('Any serial device was detected on the available ports')
    
    def __init__(self,port,baud_rate=9600,timeout=5,charset='utf-8'):
        self.port=port
        self.baud_rate=baud_rate
        self.timeout=timeout
        self.charset=charset
        if self.timeout==0:
            self.serial=Serial(port=self.port,baudrate=self.baud_rate)
        else:
            self.serial=Serial(port=self.port,baudrate=self.baud_rate,timeout=self.timeout)
    
    def __del__(self):
        SerialPort.write_debug('Destroying SerialPort object from port "{port}"'.format(port=self.port))
        if hasattr(self,'serial'):
            SerialPort.write_debug('Closing serial port')
            self.serial.close()
    
    def write(self,data):
        encoded_data=data.encode(self.charset)
        SerialPort.write_debug('Sending via serial: "{data}"'.format(data=encoded_data))
        self.serial.write(encoded_data)
    
    def write_line(self,data):
        data_with_new_line=data+'\r\n'
        SerialPort.write_debug('Sending line via serial "{data}"'.format(data=data_with_new_line))
        self.write(data_with_new_line)
    
    def read(self):
        character=self.serial.read()
        decoded_character=character.decode(self.charset)
        if self.timeout!=0:
            if decoded_character=='':
                SerialPort.write_debug('Any response into the timeout interval "{timeout}"'.format(timeout=self.timeout))
                raise SerialReadTimeoutException('Any response into the timeout interval "{timeout}"'.format(timeout=self.timeout))
        SerialPort.write_debug('Receiving via serial "{data}"'.format(data=decoded_character))
        return decoded_character
    
    def read_line(self):
        line=''
        while True:
            character=self.read()
            line=line+character
            if character=='\n':
                break
        SerialPort.write_debug('Receiving line via serial "{data}"'.format(data=line))
        return line
    
    def __str__(self):
        return str({
            'port':self.port,
            'baud_rate':self.baud_rate,
            'charset':self.charset,
            'timeout':self.timeout
        })

if __name__=='__main__':
    arduino=SerialPort.find()
    while True:
        if arduino.read_line()=='OK\r\n':
            break
    arduino.write('hello my name is danny vaca')
    print(arduino)