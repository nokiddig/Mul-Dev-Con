# function/tiktok_actions.py

import subprocess
from manage.device_manager import list_connected_devices

def open_tiktok(log_func=print):
    devices = list_connected_devices()
    if not devices:
        log_func("❌ Không có thiết bị nào được kết nối.")
        return
    for dev in devices:
        subprocess.run([
            "adb", "-s", dev, "shell", "monkey",
            "-p", "com.ss.android.ugc.trill",
            "-c", "android.intent.category.LAUNCHER", "1"
        ])
        log_func(f"🚀 Đã gửi lệnh mở TikTok đến {dev}")
    log_func(f"✅ Đã xử lý xong {len(devices)} thiết bị.\n")
