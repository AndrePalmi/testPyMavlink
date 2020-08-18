import time
from pymavlink import mavutil


# funzione per il set della mod, eventualmente posso farmi anche le 3/4 che mi servono
def set_mode(mode):
    # Check if mode is available
    # Get mode ID
    mode_id = autopilot.mode_mapping()[mode]
    autopilot.mav.set_mode_send(
        autopilot.target_system,
        mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
        mode_id)


# method that arm the motors
def arm():
    '''
        Arming the copter motors
        '''

    autopilot.mav.command_long_send(
        1,  # autopilot system id
        1,  # autopilot component id
        400,  # command id, ARM/DISARM
        0,  # confirmation
        1,  # arm!
        0, 0, 0, 0, 0, 0  # unused parameters for this command
    )


# method that disarm the motors
def disarm():
    '''
        Disarming the copter motors
        '''

    autopilot.mav.command_long_send(
        1,  # autopilot system id
        1,  # autopilot component id
        400,  # command id, ARM/DISARM
        0,  # confirmation
        0,  # disarm!
        0, 0, 0, 0, 0, 0  # unused parameters for this command
    )


# method for the take off of the copter at the height desidered
def cmd_takeoff(height):
    '''
        Method that start the take off of the Copter
        :param
                height: type 'float';
                        height that the drone will reach at the take-off
    '''

    # setting the mode
    set_mode('GUIDED')

    altitude = float(height)
    print("Take Off started")
    # sending the take-off command to the copter
    autopilot.mav.command_long_send(
        1,  # target_system
        1,  # target_component
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,  # command
        0,  # confirmation
        0,  # param1
        0,  # param2
        0,  # param3
        0,  # param4
        0,  # param5
        0,  # param6
        altitude  # param7
    )

    # defining the desidered height (AMSL - " above mean sea level ")
    objective = autopilot.field('GPS_RAW_INT', 'alt', 0) / 1.0e3 + height

    # loop to reach the height requested
    while True:
        # saving the actual height of the copter
        alt = autopilot.location().alt
        # loop until the gap is 1 metre
        if alt >= objective - 1:
            print("Desired height reached")
            break

        time.sleep(0.5)

    print("Altitude: " + str(altitude) + "[m] reached")

# method to land the drone
def cmd_land():
    '''
        Land the Copter
        '''
    ground_lng = autopilot.field('GPS_RAW_INT', 'lon', 0)
    ground_lat = autopilot.field('GPS_RAW_INT', 'lat', 0)
    ground_alt = autopilot.field('GPS_RAW_INT', 'alt', 0) / 1.0e3

    autopilot.mav.command_long_send(
        1,  # target_system
        1,  # target_component
        mavutil.mavlink.MAV_CMD_NAV_LAND,  # command
        0,  # confirmation
        0,  # param1
        0,  # param2
        0,  # param3
        float("nan"),  # param4
        ground_lat,  # param5
        ground_lng,  # param6
        ground_alt)  # param7


# method for the return to lauch (RTL)
def cmd_rtl():
    '''
        Return the Copter to the place where it was lauch
        '''
    autopilot.mav.command_long_send(
            1,  # target_system
            1,  # target_component
            mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,  # command
            0,0,0,0,0,0,0,0)


# TODO: MAV_FRAME_BODY_OFFSET_NED is deprecated, we need to replace it with MAV_FRAME_BODY_FRD
#  see: https://mavlink.io/en/messages/common.html#MAV_FRAME_BODY_OFFSET_NED
def cmd_move_to_ned(dX, dY, dZ, dYaw):
    '''

    :param dX: type 'float'
                movement in metres [m] in the x axis
                from the actual position of the Copter
    :param dY: type 'float'
                movement in metres [m] in the y axis
                from the actual position of the Copter
    :param dZ: type 'float'
                movement in metres [m] in the z axis
                from the actual position of the Copter
    :param dYaw: type 'float'
    '''
    autopilot.mav.set_position_target_local_ned_send(
        0,  # timestamp
        autopilot.target_system,  # target system_id
        autopilot.target_component,  # target component id
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,
        0b1111101111111000,  # mask specifying use-only-x-y-z-yaw
        dX,  # x
        dY,  # y
        -dZ,  # z
        0,  # vx
        0,  # vy
        0,  # vz
        0,  # afx
        0,  # afy
        0,  # afz
        dYaw,  # yaw
        0,  # yawrate
    )

# command for the movement of the copter with
# gps coordinate
def cmd_move_to_gps(lat, lng, alt):
    '''

    :param lat: type 'float'
                latitude coordinate that the Copter will reach
    :param lng: type 'float'
                longitude coordinate that the Copter will reach
    :param alt: type 'float'
                altitude (in metres [m]) that the Copter will reach
    '''

    set_mode("GUIDED")

    autopilot.mav.set_position_target_global_int_send(
        0,  # timestamp
        autopilot.target_system,  # target system_id
        autopilot.target_component,  # target component id
        mavutil.mavlink.MAV_FRAME_GLOBAL_INT,  # frame
        0b0000111111111000,  # type_mask (only speeds enabled)
        lat * 1e7,  # lat_int - X
        lng * 1e7,  # lon_int - Y
        alt,
        0,  # X velocity in NED frame in m/s
        0,  # Y velocity in NED frame in m/s
        0,  # Z velocity in NED frame in m/s
        0, 0, 0,  # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)  # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)


    # while loop for waiting that the Copter reach the desidered position
    while True:
        current_lat = autopilot.location().lat
        current_lng = autopilot.location().lng
        current_alt = autopilot.location().alt
        # print("long :" + str(current_long) +" lat" + str(current_lat) +" alt" + str(current_alt))

        # check if the drone as reached the position demanded
        if ((alt - 1 <= current_alt <= alt + 1)
                and (abs(current_lat - lat) <= 0.000001)
                and (abs(current_lng - lng) <= 0.000001)):
            print("Position desired reached:\n  -lat: %.6f;\n  -lng: %.6f;\n  -alt: %.1f [m];" % (lat, lng, alt))
            break

        time.sleep(0.5)


# cerchio raggi non funzionante
def cmd_circle(radius):
    set_mode("CIRCLE")
    # Set parameter value
    # Set a parameter value TEMPORARILY to RAM. It will be reset to default on system reboot.
    # Send the ACTION MAV_ACTION_STORAGE_WRITE to PERMANENTLY write the RAM contents to EEPROM.
    # The parameter variable type is described by MAV_PARAM_TYPE in http://mavlink.org/messages/common.
    autopilot.mav.param_set_send(
        autopilot.target_system, autopilot.target_component,
        b'CIRCLE_RADIUS',
        10,
        mavutil.mavlink.MAV_PARAM_TYPE_REAL32,
        b'ALTITUDE',
    )


if __name__ == "__main__":

    mavutil.set_dialect("ardupilotmega")
    autopilot = mavutil.mavlink_connection('udpin:localhost:14550')

    autopilot.wait_heartbeat()
    print("Heartbeat from system (system %u component %u)" % (autopilot.target_system, autopilot.target_system))
    msg = None

    # wait for autopilot connection
    while msg is None:
        msg = autopilot.recv_msg()
    print(msg)

    # functions test:
    arm()
    cmd_takeoff(10)
    # cmd_circle(20)  # err
    cmd_move_to_gps(-35.3631386609230, 149.16303429167112, 600)
    cmd_land()
    # cmd_move_to_ned(100, 100, 2, 0)
    # cmd_rtl()
    # disarm()
