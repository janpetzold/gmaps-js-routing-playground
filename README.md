# gmaps Javascript routing playground
Playing around with JavaScript API

Sample route:

    45.661826442279775, 25.606524511810704
    45.641251682717716, 25.589605754137434
    45.634788726015465, 25.592675482083997
    45.6395263917423, 25.59392649831764

URL: https://maps.app.goo.gl/5t2vbyiqKXTZQoM69

For decoding & polyline generation see `python`.

For web frontend see `web`. Run this locally via

    cd web
    busybox httpd -f -p 8080 &

# Results

When measuring frames per second the Zero 2 achieved TODO fps (benchmark here TODO).

Measuring power consumption resulted in the following:

Raspberry Pi Zero 2 idle: 0.145A
External display w. 800*480 resolution: 0.29A
Raspberry Pi Zero 2 with routing benchmark running: 0.26A

So in total this means when routing we end up with power consumption of ~0.55A. Using a $15 2500mAh battery would lead to a max runtime of approx. 5 hours.