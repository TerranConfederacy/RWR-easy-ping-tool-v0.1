import subprocess
import re
import tkinter as tk
import tkinter.messagebox

class PingTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RWR Server Ping Tool")
        self.server_ips = {
            "CN11服": "47.102.147.209",
            "CN10服": "47.102.147.209",
            "CN9服": "47.102.147.209",
            "CN4服": "121.43.113.162",
            "JP1服": "45.32.63.85",
            "WW2CN1服": "106.14.142.100",
            "WW2CN3服": "47.107.163.15",
            "WW2JP1服": "45.32.63.85",
            "EU2服": "31.186.250.67",
            "EU1服": "31.186.250.67"
        }
        self.server_labels = []
        self.server_buttons = []
        for i, (server_name, server_ip) in enumerate(self.server_ips.items()):
            label = tk.Label(self.root, text=server_name)
            button = tk.Button(self.root, text="Ping!", command=lambda ip=server_ip: self.ping(ip))
            label.grid(row=i, column=0)
            button.grid(row=i, column=1)
            self.server_labels.append(label)
            self.server_buttons.append(button)

    def run(self):
        self.root.mainloop()

    def ping(self, ip):
        cmd = ["ping", "-n", "1", "-w", "2000", f"{ip}"]
        ping_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = ping_process.communicate()
        output_str = output.decode("gbk") + error.decode("gbk")
        delay_match = re.search(r"时间=(\d+)ms", output_str)
        if delay_match:
            delay = int(delay_match.group(1))
            tkinter.messagebox.showinfo("Ping Result", f"Delay: {delay} ms")
        else:
            tkinter.messagebox.showerror("Ping Error", "Failed to ping the server.")

if __name__ == "__main__":
    tool = PingTool()
    tool.run()