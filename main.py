def on_forever():
    for I in range(5):
        led.plot(2, 2 + I)
        led.plot(2 + I, 2)
        led.plot(2, 2 - I)
        led.plot(2 - I, 2)
        basic.pause(200)
basic.forever(on_forever)
