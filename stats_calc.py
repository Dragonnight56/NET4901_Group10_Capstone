#POWER VS TIME GRAPH CREATION CODE (I am still working on it ) - SHUB 
#############################################################################
########### 1-time slots to the multiple time slots #####################
def datarate(timeslots , req_data_amt):
    datarate = 0
    datarate = req_data_amt / timeslots
    calculate_transmitted_power(datarate)


def calculate_transmitted_power(data_rate):
        """
        Calculate transmitted power using the given formula.

        Parameters:
        - data_rate: Data rate (r)
        - bandwidth: Bandwidth (w)
        - constant_W: Constant term (W)
        - power_density_noise: Power spectral density of noise (N0)
        - constant_h: Another constant term (h)

        Returns:
        - Transmitted power (Pt)
        """
        transmitted_power = (2 ** (data_rate / bandwidth) - 1) * constant_W * power_density_noise / constant_h
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