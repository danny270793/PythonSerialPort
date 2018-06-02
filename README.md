# SerialPort
A serial communication library for python, this library is a wrapper for pyserial library

## Installation
To install the libary first install git
```bash
sudo apt-get install git
```

Clone the repository
```bash
git clone https://github.com/danny270793/PythonSerialPort.git
```

Enter to the folder and install it with python 2
```bash
cd PythonSerialPort
pip install .
```

Or with python 3
```bash
cd PythonSerialPort
pip3 install .
```

## Usage
To use the library if we do not know the name of the serial port we can use the function "find" to test a list of serial ports
```python
from serialport import SerialPort

arduino=SerialPort.find()
while True:
    line=arduino.read_line()
    print(line)
```
If we know the name of the serial porr we can connect to it
```python
from serialport import SerialPort

arduino=SerialPort('/dev/ttyUSB0')
while True:
    line=arduino.read_line()
    print(line)
```

## Follow me
* [Facebook](https://www.facebook.com/danny.vaca.9655)
* [Instagram](https://www.instagram.com/danny27071993/)
* [Youtube](https://www.youtube.com/channel/UC5MAQWU2s2VESTXaUo-ysgg)
* [Github](https://www.github.com/danny270793/)
* [LinkedIn](https://www.linkedin.com/in/danny270793)

## License
Copyright (c) Danny Vaca. All rights reserved.

Licensed under the [MIT](LICENSE.txt) License.