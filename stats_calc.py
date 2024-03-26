"""
----------------
!!! ON PAUSE !!!
----------------

"""

def calc_data_rate(num_resource_elements=100, resource_element_size=10, num_time_slots=10):
    """
    By Jacky Liang and Shub B

    Calculates the data rate for a given user using information from resource allocation algorithms.

    Parameters:
    - num_resource_elements = number of resource elements used to transmit user's requested data
    - resource_element_size = bit size of a single resource element
    - num_time_slots = number of time slots used to transmit user's requested data

    Returns:
    - Data rate in bits per second
    """
    return (num_resource_elements * resource_element_size) / num_time_slots

def calc_transmit_power(data_rate=10, bandwidth=100, power_density_noise=10, channel_gain=5):
    """
    By Jacky Liang and Shub B
    
    Calculates the transmission power (P_t) to handle a user's request based on devrived formula 2 from
    https://www.researchgate.net/publication/278123907_User-Oriented_Energy-_and_Spectral-Efficiency_Tradeoff_for_Wireless_Networks

    Parameters:
    - data_rate = Data rate (R) in bits per second
    - bandwidth = System bandwidth (W) in Hertz
    - power_density_noise = Power spectral density of noise (N_0) in Watts over Hertz
    - channel_gain = Channel gain (h) in ...

    Returns:
    - Transmission power (P_t) in Watts
    """
    return ((2 ** (data_rate / bandwidth) - 1) * bandwidth * power_density_noise) / channel_gain