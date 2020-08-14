import time
from pymavlink import mavutil

#attenzione non posso definire in una funzione altrimenti non ho autopilot per dopo
mavutil.set_dialect("ardupilotmega")
autopilot = mavutil.mavlink_connection('udpin:localhost:14551')
autopilot.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (autopilot.target_system, autopilot.target_system))
msg = None
# wait for autopilot connection
while msg is None:
        msg = autopilot.recv_msg()
print(msg)

#funzione per il set della mod, eventualmente posso farmi anche le 3/4 che mi servono
def set_mode(mode):
        # Check if mode is available
        # Get mode ID
        mode_id = autopilot.mode_mapping()[mode]
        autopilot.mav.set_mode_send(
                autopilot.target_system,
                mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
                mode_id)

#funzione per attivare i motori
def arm():
        autopilot.mav.command_long_send(
        1, # autopilot system id
        1, # autopilot component id
        400, # command id, ARM/DISARM
        0, # confirmation
        1, # arm!
        0,0,0,0,0,0 # unused parameters for this command
        )

def disarm():
        autopilot.mav.command_long_send(
                1,  # autopilot system id
                1,  # autopilot component id
                400,  # command id, ARM/DISARM
                0,  # confirmation
                0,  # disarm!
                0, 0, 0, 0, 0, 0  # unused parameters for this command
        )

#comando per decollo
def cmd_takeoff(height):
        #set modalita di guida
        set_mode('GUIDED')
        #eseguo decollo
        altitude = float(height)
        print("Take Off started")
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
                altitude)  # param7

#comando per atterraggio verticale in posizione
def cmd_land():
        set_mode("LAND")

#comando per ritorno alla base
def cmd_rtl():
        set_mode("RTL")

#comando per movimento rispeto NED
def cmd_move_to_ned(dX,dY,dZ,dYaw):
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

#comando per movimento rispetto posizione
#relativo al mare altezza 600 per mappa
def cmd_move_to_gps(lat,lon,alt):
    """
    Send SET_POSITION_TARGET_GLOBAL_INT command to request the vehicle fly to a specified location.
    """
    set_mode("GUIDED")
    autopilot.mav.set_position_target_global_int_send(
        0,  # timestamp
        autopilot.target_system,  # target system_id
        autopilot.target_component,  # target component id
        mavutil.mavlink.MAV_FRAME_GLOBAL_INT, # frame
        0b0000111111111000, # type_mask (only speeds enabled)
        lat*1e7, # lat_int - X Position in WGS84 frame in 1e7 * meters
        lon*1e7, # lon_int - Y Position in WGS84 frame in 1e7 * meters
        alt, # alt - Altitude in meters in AMSL altitude, not WGS84 if absolute or relative, above terrain if GLOBAL_TERRAIN_ALT_INT
        0, # X velocity in NED frame in m/s
        0, # Y velocity in NED frame in m/s
        0, # Z velocity in NED frame in m/s
        0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

#cerchio raggi non funzionante
def cmd_circle(radius):
        from pymavlink import mavutil
        set_mode("GUIDED")
        autopilot.mav.command_send(
                1,  # target_system
                1,  # target_component
                mavutil.mavlink.MAV_CMD_SET_GUIDED_SUBMODE_CIRCLE,  # command
                0,  # confirmation
                radius,  # param1
                0,  # param2
                0,  # param3
                0,  # param4
                0,  # param5
                0)  # param7


if __name__ == "__main__":
        arm()
        cmd_takeoff(10) #ok
        time.sleep(10)
        cmd_circle(20)  # err
        #cmd_move_to_gps(-35.3631386609230, 149.16303429167112, 600.0) #ok
        #cmd_move_to_ned(100, 100, 2, 0) #ok
        time.sleep(30)
        cmd_rtl()  #ok
        time.sleep(30)
        #disarm()  #ok

