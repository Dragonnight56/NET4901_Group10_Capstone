#POWER VS TIME GRAPH CREATION CODE (I am still working on it ) - SHUB 
#############################################################################
########### 1-time slots to the multiple time slots #####################
def datarate(timeslots , req_data_amt):
    datarate = 0
    datarate = req_data_amt / timeslots
    calculate_transmitted_power(datarate)

def calculate_transmitted_power(data_rate, bandwidth, power_density_noise, channel_gain):
        """
        Calculate transmitted power (P_t) based on devrived formula 2 from 
        https://www.researchgate.net/publication/278123907_User-Oriented_Energy-_and_Spectral-Efficiency_Tradeoff_for_Wireless_Networks

        Parameters:
        - data_rate = Data rate (R) in bits per second (bps)
        - bandwidth = System bandwidth (W) in Hertz (Hz)
        - power_density_noise = Power spectral density of noise (N_0) 
        - channel_gain = Channel gain (h)

        Returns:
        - Transmitted power (P_t) in Watts
        """
        transmitted_power = (2 ** (data_rate / bandwidth) - 1) * bandwidth * power_density_noise / channel_gain
        return transmitted_power

#############################################################################
########### multiple time slots to the powers time graph #########################
# timeslots is an array that carries value for each channel per time slot
# Here we will have timeslot { row = 3 (channels = 3 ) and cols = 4 (over 4 timeslots) }
Timeslots = [ [1, 1, 0, 0], [1, 0, 0, 1], [ 1, 0, 1, 0] ]

def powerConversion(array):
    global counter
    for row in array:
        if len(row) >  0:
            first_element = row[0]
            if first_element == 1:
                counter += 1
    power_per_timeslot = counter * power_per_channel
    print(power_per_timeslot)

def calcDataRate(arr):
    print(len(arr))
    for i in range(0, len(arr)):
        channel = channelDataUsage(arr[i])
    print(userData)

def channelDataUsage(arr):
    userData = {}
    print(arr)
    return arr