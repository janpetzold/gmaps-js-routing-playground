# Use openbox for resource efficiency and since it provides actual fullscreen
openbox-session &

# Start BusyBox httpd
cd /home/pi/code/zero-routing/web
busybox httpd -f -p 8080 &

# Start Chromium in kiosk mode
exec chromium-browser --kiosk --single-process http://localhost:8080
