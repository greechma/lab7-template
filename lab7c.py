#!/usr/bin/env python3
# Student ID: ggairhe

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError("Invalid time values: hours must be between 0 and 23, minutes and seconds must be between 0 and 59.")
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return format_time(self)


def format_time(time_obj):
    return f"{time_obj.hours:02}:{time_obj.minutes:02}:{time_obj.seconds:02}"


def time_to_sec(time_obj):
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds


def sec_to_time(seconds):
    if seconds < 0:
        raise ValueError("Cannot convert negative seconds to a valid time.")
    
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return Time(hours, minutes, seconds)


def sum_times(time1, time2):
    if not isinstance(time1, Time) or not isinstance(time2, Time):
        raise TypeError("Both arguments must be Time objects.")
    
    total_seconds = time_to_sec(time1) + time_to_sec(time2)
    return sec_to_time(total_seconds)


def change_time(time_obj, seconds):
    if not isinstance(time_obj, Time):
        raise TypeError("The first argument must be a Time object.")
    
    if not isinstance(seconds, int):
        raise TypeError("The second argument must be an integer representing the number of seconds to add.")
    
    if seconds < 0:
        raise ValueError("Cannot change time by negative seconds in this context.")
    
    total_seconds = time_to_sec(time_obj) + seconds
    return sec_to_time(total_seconds)
