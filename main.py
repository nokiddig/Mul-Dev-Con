# main.py

import customtkinter as ctk
from manage.device_manager import list_connected_devices, install_apk_for_all_devices
from function.tiktok_actions import open_tiktok

def log(message):
    log_box.insert("end", message + "\n")
    log_box.see("end")

def refresh_devices():
    device_listbox.delete("0.0", "end")
    devices = list_connected_devices()
    for dev in devices:
        device_listbox.insert("end", f"{dev}\n")
    log(f"🔄 Đã tìm thấy {len(devices)} thiết bị.")

# Giao diện
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("450x400")
app.title("TikTok Device Controller")

label = ctk.CTkLabel(app, text="Danh sách thiết bị:")
label.pack(pady=10)

device_listbox = ctk.CTkTextbox(app, height=100, width=350)
device_listbox.pack()

refresh_btn = ctk.CTkButton(app, text="🔄 Làm mới danh sách", command=refresh_devices)
refresh_btn.pack(pady=5)

launch_btn = ctk.CTkButton(app, text="🚀 Mở TikTok", command=lambda: open_tiktok(log))
launch_btn.pack(pady=5)

install_btn = ctk.CTkButton(app, text="📦 Cài APK", command=lambda: install_apk_for_all_devices(log))
install_btn.pack(pady=5)

log_box = ctk.CTkTextbox(app, height=120, width=350)
log_box.pack(pady=10)

refresh_devices()

app.mainloop()
