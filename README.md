# auto_pipetty

## pipetty
"Pipetty" is an electronic pipette of Icomes Lab Co., Ltd., [https://www.icomes.co.jp/product/pipetty/](https://www.icomes.co.jp/product/pipetty/).  
The function of liquid handling (aspiration, dispensing) can be controlled through the USB or Bluetooth.

## Setup 
```
sudo chmod 666 /dev/ttyACM0
sudo usermod -a -G dialout $USER
```

## Hardware of Pipetty
In order to grasp the pipetty and push the tip disposal button by a motor, here are the parts used, as shown in the figure.  
![pipetty](assets/pipetty.png "pipetty")  
The motor with the gear and gear rack is: [https://kitronik.co.uk/products/2595-linear-actuator](https://kitronik.co.uk/products/2595-linear-actuator).


