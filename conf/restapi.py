
MONITOR_LOOP_DELAY_SECS = 60.0
RESTART_MONITOR_DELAY_SECS = 120.0

# iotech sbms gate server on LAN
# 192.168.50.102 192.168.40.106
SBMS_GATE_LAN_IP = "10.0.50.200"

# REST LAN server
SBMS_REST_SERVER = f"{SBMS_GATE_LAN_IP}:8082"

# leave the first / from the string
REST_REPORT_ALARM_URL = "report-alarm"
REST_REPORT_STREAMER = "streamer"
REST_REPORT_KWH_URL = "report-kwh"
REST_REPORT_PING_URL = "ping"
