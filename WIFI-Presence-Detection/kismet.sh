while true; do
echo "Looking For Interface in Moitor Mode"
if ip a | grep -q "wlan0mon"; then
        echo "Taking Interface Device Down"
        airmon-ng stop wlan0mon
        echo "Restarting Interafce ....."
        if airmon-ng start wlan0 | grep -q "kill"; then
                echo "Trouble Found! Killing Network Processes That Might Interfere"
                airmon-ng check kill
		echo "Starting interface"
		airmon-ng start wlan0
        else
		echo "Starting interface"
                airmon-ng start wlan0
        fi
else
        echo "Starting Interface In Monior Mode"
        if airmon-ng start wlan0 | grep -q "kill"; then
                echo "Trouble Found! Killing Network Processes That Might Interfere"
                airmon-ng check kill
                echo "Starting interface"
                airmon-ng start wlan0
        else
		echo "Starting interface"
		airmon-ng start wlan0
	fi
fi

        echo "Starting Kismet ..."
        kismet -c wlan0mon &
        sleep 60
        echo "Killing Kismet ..."
        killall kismet
	sleep 10
        echo "Moving Data Into Main Database"
        python3 Python_org.py
        echo "Removing Old Database File"
        rm -f kismet.kismet
done
