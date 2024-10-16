import flet as ft
import requests
import os
import shutil
import subprocess
import re
from flet import Page, ElevatedButton, Text, Column, Row, Container, Divider, padding, alignment, colors, IconButton, icons

class AnonToolkit:
    def __init__(self):
        self.app = ft.app(target=self.main)

    def main(self, page: Page):
        page.title = "AnonToolkit"
        page.window.resizable = True
        page.window.width = 1200
        page.window.height = 900
        page.vertical_alignment = "start"
        page.horizontal_alignment = "center"
        page.theme_mode = "dark"
        page.padding = padding.symmetric(horizontal=20, vertical=20)
        page.spacing = 20

        # Widgets creation
        self.title = Text("AnonToolkit", size=50, weight="bold", color=colors.LIGHT_BLUE_400, text_align="center")
        self.github_link = Text("GitHub: https://github.com/phpont", size=14, italic=True, color=colors.GREY, text_align="right")
        self.output_text = Text("", size=16, selectable=True, color=colors.WHITE, width=700)

        # Buttons with icons for more user-friendly interaction
        self.ip_button = ElevatedButton(text="Check IP and Geolocation", icon=icons.PUBLIC, on_click=self.check_ip)
        self.clear_browser_button = ElevatedButton(text="Clear Browser Fingerprints", icon=icons.BROWSER_NOT_SUPPORTED, on_click=self.clear_browser_fingerprints)
        self.flush_dns_button = ElevatedButton(text="Flush DNS Cache", icon=icons.REFRESH, on_click=self.flush_dns)
        self.mac_change_button = ElevatedButton(text="Change MAC Address", icon=icons.NETWORK_CELL, on_click=self.change_mac_address)
        self.change_user_agent_button = ElevatedButton(text="Change User-Agent (Placeholder)", icon=icons.DEVICE_UNKNOWN, on_click=self.change_user_agent)
        self.vpn_check_button = ElevatedButton(text="Check VPN Connection", icon=icons.LOCK, on_click=self.check_vpn)
        self.system_cleanup_button = ElevatedButton(text="System Cleanup", icon=icons.DELETE, on_click=self.system_cleanup)
        self.clear_cookies_button = ElevatedButton(text="Clear Cookies", icon=icons.CLEAR, on_click=self.clear_cookies)
        self.disable_webrtc_button = ElevatedButton(text="Disable WebRTC (Firefox)", icon=icons.VISIBILITY_OFF, on_click=self.disable_webrtc)
        self.browser_choice_button = ElevatedButton(text="Browser Specific Options", icon=icons.WEB, on_click=self.browser_specific_options)

        # Layout adjustments for better alignment and consistency
        buttons_container = Container(
            content=Column(
                [
                    self.ip_button,
                    self.clear_browser_button,
                    self.flush_dns_button,
                    self.mac_change_button,
                    self.change_user_agent_button,
                    self.vpn_check_button,
                    self.system_cleanup_button,
                    self.clear_cookies_button,
                    self.disable_webrtc_button,
                    self.browser_choice_button,
                ],
                spacing=15,
                alignment="start"
            ),
            padding=padding.all(20),
            bgcolor=colors.BLUE_GREY_900,
            border_radius=10,
            expand=True
        )

        # Main layout with improved alignment
        page.add(
            Column(
                [
                    Container(self.title, padding=padding.symmetric(vertical=20), alignment=alignment.center),
                    Row([
                        buttons_container,
                        Container(
                            Column([
                                self.output_text
                            ], spacing=20),
                            padding=padding.all(20),
                            border_radius=20,
                            bgcolor=colors.BLUE_GREY_800,
                            alignment=alignment.center,
                            expand=True
                        ),
                    ], alignment="center", spacing=30, expand=True),
                    Divider(height=1, color=colors.GREY),
                    Container(self.github_link, alignment=alignment.bottom_right, padding=padding.only(top=10))
                ],
                alignment="start",
                horizontal_alignment="center",
                spacing=12,
                expand=True
            )
        )

    def update_output(self, page: Page, message: str, success: bool = True):
        self.output_text.value = message
        self.output_text.color = "green" if success else "red"
        page.update()

    def check_ip(self, e):
        try:
            response = requests.get("https://ipinfo.io")
            if response.status_code == 200:
                data = response.json()
                ip = data.get("ip", "N/A")
                loc = data.get("loc", "N/A")
                city = data.get("city", "N/A")
                region = data.get("region", "N/A")
                country = data.get("country", "N/A")
                if loc != "N/A":
                    latitude, longitude = loc.split(",")
                    self.update_output(e.page, f"IP: {ip}\nCity: {city}\nRegion: {region}\nCountry: {country}\nCoordinates: Latitude {latitude}, Longitude {longitude}")
                else:
                    self.update_output(e.page, f"IP: {ip}\nLocation: Not available")
            else:
                self.update_output(e.page, "Failed to fetch IP information", success=False)
        except requests.RequestException as ex:
            self.update_output(e.page, f"Network error: {ex}", success=False)

    def clear_browser_fingerprints(self, e):
        try:
            paths = [
                os.path.expanduser("~/.mozilla/firefox"),
                os.path.expanduser("~/.config/google-chrome"),
                os.path.expanduser("~/.cache/mozilla"),
                os.path.expanduser("~/.cache/google-chrome"),
            ]
            for path in paths:
                if os.path.exists(path):
                    shutil.rmtree(path)
            self.update_output(e.page, "Browser fingerprints cleared successfully")
        except Exception as ex:
            self.update_output(e.page, f"Error clearing fingerprints: {ex}", success=False)

    def flush_dns(self, e):
        try:
            if os.name == "nt":
                subprocess.run("ipconfig /flushdns", check=True, shell=True)
            else:
                subprocess.run(["sudo", "systemd-resolve", "--flush-caches"], check=True)
            self.update_output(e.page, "DNS Cache flushed successfully")
        except subprocess.CalledProcessError as ex:
            self.update_output(e.page, f"Error flushing DNS: {ex}", success=False)

    def change_mac_address(self, e):
        try:
            interface = "eth0"  # Change according to system setup
            new_mac = "00:11:22:33:44:55"  # Example MAC address
            if os.name != "nt":
                subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
                subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac], check=True)
                subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
                self.update_output(e.page, "MAC Address changed successfully")
            else:
                self.update_output(e.page, "MAC address change not supported on Windows via script.", success=False)
        except subprocess.CalledProcessError as ex:
            self.update_output(e.page, f"Error changing MAC Address: {ex}", success=False)
        except Exception as ex:
            self.update_output(e.page, f"Unexpected error: {ex}", success=False)

    def change_user_agent(self, e):
        self.update_output(e.page, "User-Agent change functionality is in development.")

    def check_vpn(self, e):
        try:
            response = requests.get("https://ipinfo.io")
            if response.status_code == 200:
                data = response.json()
                org = data.get("org", "N/A")
                if "VPN" in org or "Hosting" in org:
                    self.update_output(e.page, "VPN Detected: Yes")
                else:
                    self.update_output(e.page, "VPN Detected: No")
            else:
                self.update_output(e.page, "Failed to determine VPN status", success=False)
        except requests.RequestException as ex:
            self.update_output(e.page, f"Network error: {ex}", success=False)

    def system_cleanup(self, e):
        try:
            if os.name == "nt":
                subprocess.run(["cleanmgr"], check=True)
            else:
                subprocess.run(["sudo", "apt", "clean"], check=True)
                subprocess.run(["sudo", "apt", "autoremove"], check=True)
            self.update_output(e.page, "System cleanup completed successfully")
        except subprocess.CalledProcessError as ex:
            self.update_output(e.page, f"Error during system cleanup: {ex}", success=False)

    def clear_cookies(self, e):
        try:
            paths = [
                os.path.expanduser("~/.mozilla/firefox"),
                os.path.expanduser("~/.config/google-chrome"),
            ]
            for path in paths:
                cookies_path = os.path.join(path, "Cookies")
                if os.path.exists(cookies_path):
                    os.remove(cookies_path)
            self.update_output(e.page, "Cookies cleared successfully")
        except Exception as ex:
            self.update_output(e.page, f"Error clearing cookies: {ex}", success=False)

    def disable_webrtc(self, e):
        try:
            prefs_path = os.path.expanduser("~/.mozilla/firefox/*/prefs.js")
            if os.path.exists(prefs_path):
                with open(prefs_path, "a") as prefs_file:
                    prefs_file.write('\nuser_pref("media.peerconnection.enabled", false);')
            self.update_output(e.page, "WebRTC disabled for Firefox successfully")
        except Exception as ex:
            self.update_output(e.page, f"Error disabling WebRTC: {ex}", success=False)

    def browser_specific_options(self, e):
        self.update_output(e.page, "Browser specific options are still in development.")

if __name__ == "__main__":
    toolkit = AnonToolkit()
