import time
from pymavlink import mavutil


def setMode(mode):
        # Check if mode is available
        # Get mode ID
        mode_id = autopilot.mode_mapping()[mode]
        autopilot.mav.set_mode_send(
                autopilot.target_system,
                mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
                mode_id)

mavutil.set_dialect("ardupilotmega")

autopilot = mavutil.mavlink_connection('udpin:localhost:14551')
autopilot.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (autopilot.target_system, autopilot.target_system))
msg = None

# wait for autopilot connection
while msg is None:
        msg = autopilot.recv_msg()

print(msg)

# # The values of these heartbeat fields is not really important here
# # I just used the same numbers that QGC uses
# # It is standard practice for any system communicating via mavlink emit the HEARTBEAT message at 1Hz! Your autopilot may not behave the way you want otherwise!
# autopilot.mav.heartbeat_send(
# 6, # type
# 8, # autopilot
# 192, # base_mode
# 0, # custom_mode
# 4, # system_status
# 3  # mavlink_version
# )

autopilot.mav.command_long_send(
1, # autopilot system id
1, # autopilot component id
400, # command id, ARM/DISARM
0, # confirmation
1, # arm!
0,0,0,0,0,0 # unused parameters for this command
)

time.sleep(2)


def cmd_takeoff(height):
        #set modalita di guida
        setMode('GUIDED')
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


cmd_takeoff(40)
time.sleep(20)

autopilot.mav.command_long_send(
1, # autopilot system id
1, # autopilot component id
400, # command id, ARM/DISARM
0, # confirmation
0, # disarm!
0,0,0,0,0,0 # unused parameters for this command
)