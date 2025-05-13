import subprocess
from tkinter import filedialog

def list_connected_devices():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")[1:]
    devices = [line.split()[0] for line in lines if "device" in line]
    return devices

def install_apk_for_all_devices(log_func=print):
    filepath = filedialog.askopenfilename(
        filetypes=[("APK files", "*.apk")],
        title="Chọn file APK để cài đặt"
    )
    if not filepath:
        log_func("❌ Không chọn file APK nào.")
        return

    devices = list_connected_devices()
    if not devices:
        log_func("❌ Không có thiết bị nào được kết nối.")
        return

    for dev in devices:
        log_func(f"📤 Đang cài APK lên thiết bị {dev}...")
        result = subprocess.run(["adb", "-s", dev, "install", "-r", filepath], capture_output=True, text=True)
        if "Success" in result.stdout:
            log_func(f"✅ Cài đặt thành công trên {dev}")
        else:
            log_func(f"❌ Cài thất bại trên {dev}: {result.stdout.strip() or result.stderr.strip()}")

    log_func("🎉 Hoàn tất quá trình cài đặt.\n")
