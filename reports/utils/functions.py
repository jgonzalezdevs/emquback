def get_ping_counts(queryset):
    queryset = queryset
    ping_counts = {}
    for device_log in queryset:
        if device_log.device.id not in ping_counts:
            ping_counts[device_log.device.id] = {
                'device_name': device_log.device.name,
                'device_ipv4': device_log.device.ipv4,
                'sucess_ping': 0,
                'failed_ping': 0
            }
        if device_log.device_answered is True:
            ping_counts[device_log.device.id]['sucess_ping'] += 1
        elif device_log.device_answered is False:
            ping_counts[device_log.device.id]['failed_ping'] += 1
    return ping_counts