# Cloud Management System

## 1. Introduction

The Cloud Management System is a user-friendly application designed to interact with cloud infrastructure, specifically focusing on virtual machine and Docker container management. It provides functionalities such as creating virtual disks, managing virtual machines, building Docker images, and interacting with DockerHub. The project integrates `qemu` for virtual disk and machine management, along with `Docker` for container and image management.

## 2. Objective

The primary objective of this project is to develop a graphical user interface (GUI) that enables users to easily manage cloud-based resources such as virtual disks, virtual machines, and Docker containers. The goal is to simplify the process of managing virtual environments and containerized applications by abstracting complex command-line operations into a user-friendly interface.

## 3. Functionalities

The system supports the following key functionalities:

- **Create Virtual Disk**: Allows the user to create a virtual disk by selecting a path, size, and format (e.g., `qcow2`, `raw`).
- **Create Virtual Machine**: Enables the user to create and start a virtual machine by selecting an ISO image, disk, and specifying memory and CPU configuration.
- **Create Dockerfile**: Allows the user to create a Dockerfile by specifying custom content and saving it as a file.
- **Build Docker Image**: Facilitates building Docker images using the provided Dockerfile and a user-defined image tag.
- **List Docker Images**: Displays a list of all available Docker images on the system.
- **List Running Containers**: Shows all running Docker containers.
- **Stop Container**: Allows the user to stop a running Docker container by specifying its container ID or name.
- **Search Local Docker Images**: Enables searching for Docker images available locally.
- **Search DockerHub**: Searches for Docker images on DockerHub.
- **Pull Docker Image**: Facilitates pulling Docker images from DockerHub.

## 4. Technologies Used

- **Python 3.x**: Programming language used for the implementation of the application.
- **Tkinter**: GUI library for creating the graphical user interface.
- **Subprocess Module**: Used to execute shell commands (e.g., `qemu-img`, `docker`).
- **QEMU**: Virtualization tool for creating virtual disks and managing virtual machines.
- **Docker**: Platform used for managing containerized applications.

## 5. System Requirements

- **Operating System**: Windows/Linux/macOS
- **Dependencies**:
  - Python 3.x
  - Tkinter (comes with Python)
  - QEMU (for virtual machine management)
  - Docker (for container management)
  - cURL (for DockerHub search functionality)

## 6. GUI Layout

The user interface consists of a simple, easy-to-navigate window with the following components:

- **Header**: Displays the title "Cloud Management System".
- **Buttons**: Each button corresponds to a specific operation (e.g., "Create Virtual Disk", "Build Docker Image").
- **File Dialogs**: Users can select files (e.g., ISO, virtual disk, Dockerfile) via file dialogs.
- **Input Dialogs**: Users are prompted to enter specific parameters like disk size, memory size, or CPU count.

## 7. User Flow

1. **Start the Application**: When the application is run, the main window is displayed with various options.
2. **Select an Operation**: The user selects an operation, such as "Create Virtual Disk" or "Build Docker Image".
3. **Input Parameters**: Depending on the operation, the user may be asked to input or select values like paths, sizes, or configurations.
4. **Execute the Operation**: After providing the required input, the user clicks the corresponding button, and the system executes the command.
5. **Display Results**: The results of the operation are displayed through pop-up messages, informing the user whether the operation was successful or failed.

## 8. Error Handling

The system includes error handling mechanisms to ensure smooth user experience:

- **Tool Availability Check**: Before executing commands, the system checks if required tools (e.g., `qemu-img`, `docker`, `curl`) are installed. If not, an error message is shown.
- **Subprocess Error Handling**: If any command execution fails, an error message is displayed through a pop-up dialog, informing the user of the failure.

## 9. Limitations

- The system does not handle advanced configurations or the management of other types of virtual environments (e.g., AWS, Azure).
- The DockerHub search feature retrieves raw data and is not currently parsed for better readability.

## 10. Conclusion

The Cloud Management System provides an intuitive interface for managing virtual disks, virtual machines, and Docker containers. By abstracting the complexity of command-line operations, it enhances user productivity and simplifies cloud resource management. While the system currently focuses on basic cloud management tasks, future enhancements could include support for more cloud platforms and additional features for virtual machine and container orchestration.

## 11. Future Work

- **Support for Additional Cloud Providers**: Integrate with cloud providers like AWS, GCP, and Azure to manage virtual machines and containers.
- **Improved DockerHub Search**: Enhance the DockerHub search functionality to parse JSON data and display more relevant information.
- **Asynchronous Operations**: Implement threading or asynchronous methods to prevent the UI from freezing during long-running operations.

## 12. References

- [QEMU Documentation](https://www.qemu.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)