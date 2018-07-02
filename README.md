# AFSK
An attempt to use AFSK for a CubeSat communication system

Curently python scripts are written to produce an analogue voltage, using a Raspberry Pi, an ADC, a 15 Bit RAM, an oszillator circuit and a binary counter.

Due to the small sampling frequency the Raspberry Pi provides, it is necessary to save digital signals in the RAM before giving them to the ADC.

The analogue signal from the ADC then goes into the microphone input of a radio transceiver.
 
Another radio transceiver will receive this AFSK signal and steps will be taken to decode the signal.

We hope to archieve a higher datarate with this technique.
