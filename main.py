import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import subprocess
import os

def style_button(btn):
    """
    Style the button with background color, font, border, etc.
    """
    btn.config(bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=3, padx=10, pady=5)

def check_tool_availability(tool_name):
    """
    Check if a tool is available in the system.
    """
    try:
        subprocess.run([tool_name, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def run_command(command, error_message):
    """
    Run a command and display an error message if the command fails.
    """
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", error_message)

def create_virtual_disk():
    """
    Create a virtual disk by prompting the user for path, size, and format.
    """
    path = filedialog.asksaveasfilename(title="Select path for virtual disk")
    size = simpledialog.askstring("Input", "Enter disk size (e.g., 10G):")
    fmt = simpledialog.askstring("Input", "Enter disk format (e.g., qcow2):")

    if path and size and fmt:
        run_command(["qemu-img", "create", "-f", fmt, path, size], "Failed to create virtual disk.")
        messagebox.showinfo("Success", "Virtual disk created successfully.")

def create_virtual_machine():
    """
    Create and start a virtual machine by selecting an ISO, disk, memory, and CPU options.
    """
    iso = filedialog.askopenfilename(title="Select ISO image")
    disk = filedialog.askopenfilename(title="Select virtual disk")
    memory = simpledialog.askstring("Input", "Enter memory size (e.g., 1024):")
    cpus = simpledialog.askstring("Input", "Enter number of CPUs (e.g., 2):")

    if iso and disk and memory and cpus:
        try:
            subprocess.Popen([
                "qemu-system-x86_64",
                "-m", memory,
                "-smp", cpus,
                "-hda", disk,
                "-cdrom", iso,
                "-boot", "d",
                "-enable-kvm"
            ])
            messagebox.showinfo("Started", "VM started successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def create_dockerfile():
    """
    Create a Dockerfile by allowing the user to enter content and select a save location.
    """
    path = filedialog.asksaveasfilename(title="Save Dockerfile as", defaultextension="Dockerfile")
    content = simpledialog.askstring("Dockerfile", "Enter Dockerfile content:")

    if path and content:
        with open(path, "w") as f:
            f.write(content)
        messagebox.showinfo("Success", "Dockerfile created successfully.")

def build_docker_image():
    """
    Build a Docker image by selecting a Dockerfile and providing an image tag.
    """
    dockerfile = filedialog.askopenfilename(title="Select Dockerfile")
    tag = simpledialog.askstring("Input", "Enter image name:tag")

    if dockerfile and tag:
        run_command(["docker", "build", "-t", tag, "-f", dockerfile, os.path.dirname(dockerfile)], "Failed to build Docker image.")
        messagebox.showinfo("Success", "Docker image built successfully.")

def list_docker_images():
    """
    List all Docker images in the system.
    """
    result = subprocess.run(["docker", "images"], capture_output=True, text=True)
    messagebox.showinfo("Docker Images", result.stdout)

def list_running_containers():
    """
    List all running Docker containers.
    """
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    messagebox.showinfo("Running Containers", result.stdout)

def stop_container():
    """
    Stop a running Docker container by entering its container ID or name.
    """
    cid = simpledialog.askstring("Input", "Enter container ID or name to stop:")
    if cid and messagebox.askyesno("Confirm", f"Are you sure you want to stop container {cid}?"):
        subprocess.run(["docker", "stop", cid])
        messagebox.showinfo("Stopped", f"Container {cid} stopped.")

def search_local_image():
    """
    Search for a local Docker image by name.
    """
    name = simpledialog.askstring("Input", "Enter image name to search:")
    if name:
        result = subprocess.run(["docker", "images", name], capture_output=True, text=True)
        messagebox.showinfo("Search Result", result.stdout)

def search_dockerhub():
    """
    Search for a Docker image on DockerHub.
    """
    name = simpledialog.askstring("Input", "Enter image name to search on DockerHub:")
    if name:
        result = subprocess.run(["curl", f"https://hub.docker.com/v2/search/repositories/?query={name}"], capture_output=True, text=True)
        messagebox.showinfo("DockerHub Search Result", result.stdout)

def pull_docker_image():
    """
    Pull a Docker image from DockerHub by name.
    """
    name = simpledialog.askstring("Input", "Enter image name to pull:")
    if name:
        subprocess.run(["docker", "pull", name])
        messagebox.showinfo("Success", f"Image {name} pulled.")

# GUI
root = tk.Tk()
root.title("Cloud Management System")
root.geometry("550x650")
root.configure(bg="#f0f0f0")

header = tk.Label(root, text="Cloud Management System", font=("Arial", 18, "bold"), bg="#f0f0f0", pady=20)
header.pack()

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

options = [
    ("Create Virtual Disk", create_virtual_disk),
    ("Create Virtual Machine", create_virtual_machine),
    ("Create Dockerfile", create_dockerfile),
    ("Build Docker Image", build_docker_image),
    ("List Docker Images", list_docker_images),
    ("List Running Containers", list_running_containers),
    ("Stop Container", stop_container),
    ("Search Local Image", search_local_image),
    ("Search Image on DockerHub", search_dockerhub),
    ("Pull Docker Image", pull_docker_image)
]

for text, command in options:
    btn = tk.Button(frame, text=text, command=command, width=40)
    style_button(btn)
    btn.pack(pady=5)

root.mainloop()