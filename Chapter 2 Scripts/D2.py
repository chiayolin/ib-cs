# D2.py - All That Talking
#
# The Problem:
#   Develop and test a Python program that determines how much time it would 
#   take to download all instances of every word ever spoken. Assume the size 
#   of this information as given in Figure 2-1. The download speed is to be 
#   entered by the user in million of bits per second (Mbps). To find your 
#   actual connection speed, go to the following website (from Intel Corporat-
#   ion) or similar site, 
#       <www.intel.com/content/www/us/en/gamers/broadband-speed-test.html>.
#   Because connection speeds can vary, run this connection speed three times. 
#   Take the average of three results, and use that as the connection speed to 
#   enter into your program. Finally, determine what is an appropriate unit of 
#   time to express your program results in minutes? hours? days? other?
#
# Analysis:
#   Acording to Figure 2-1 that all the words ever spoken is about 5 exabytes.
#   We can convert the exabytes to megabits since the connection speed is 
#   usually measured in Mbps (megabits per second). In order to do that, we can
#   take 2^60 divide by 1024^2 since there are 2^60 bytes in an exabyte and by
#   dividing it by 1024^2, we will get the amount of megabytes there are. How-
#   ever, we would have to times that number by 8 because it is measued in
#   "megabit" not "megabyte" -- the amount of megabits we have is 1099511627776. 
#   Finally, we can take that number and divide it by the connection speed (in
#   Mbps) to get the amount of time it would take in seconds.
#
# Implementation:
#   Ask the user if they want to test their current download speed. If yes, run 
#   the speed testing function. Otherwise use the default connection speed.
#   
# Date:    09/05/2016
# Author:  Chiayo Lin
# License: GPL 3.0

import urllib.request, time

# return the current average "download" Mbps
def speed_test():
    print("Testing the current connection speed...")
    print("Using the server from Softlayer, Singapore...")
    file_size = 100 * (2**20) # size of the test file in bytes
    start_time = time.time()
    urllib.request.urlretrieve(
        "http://speedtest.sea01.softlayer.com/downloads/test100.zip", \
            "/dev/null")
    
    # devide by 1024^2 and multiply by 8 to convert bytes to megabits
    speed = (int(file_size / (time.time() - start_time)) / (2**20)) * 8
    print("The current connection speed is about {:.2f} Mbps.".
        format(speed))

    return speed

# main
def main():
    print("How long it would take you to download 5EB of data?")
    # ask the user if he wants to test his current connection speed
    connection_mbps = speed_test() if \
        input("Do you want to test your current speed? (y/N) ") \
            .strip().lower()[0] is 'y' else \
                int(input("Enter your speed (Mbps): "))

    target_size_b = 5 * (2**60) * 8
    seconds_in_a_year = 60 * 60 * 24 * 365
    total_time = (target_size_b / (connection_mbps * (2**20))) / seconds_in_a_year

    print("At the speed of", format(connection_mbps, '.2f'), 
        "Mbps, it will take about", format(total_time, '.2f'), 
            "years to download.")

if __name__ == "__main__":
    main()
