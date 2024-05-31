# import platform
# import pynvml


# def get_cpu_info():
#     system_info = platform.uname()
#     return {
#         "System": system_info.system,
#         "Node Name": system_info.node,
#         "Release": system_info.release,
#         "Version": system_info.version,
#         "Machine": system_info.machine,
#         "Processor": system_info.processor,
#     }


# def get_cuda_info():
#     try:
#         pynvml.nvmlInit()
#         device_count = pynvml.nvmlDeviceGetCount()
#         cuda_devices = []
#         for i in range(device_count):
#             handle = pynvml.nvmlDeviceGetHandleByIndex(i)
#             device_name = pynvml.nvmlDeviceGetName(handle).decode("utf-8")
#             cuda_devices.append({"Device Index": i, "Device Name": device_name})
#         return cuda_devices
#     except pynvml.NVMLError as e:
#         return str(e)


# if __name__ == "__main__":
#     print("CPU Information:")
#     cpu_info = get_cpu_info()
#     for key, value in cpu_info.items():
#         print(f"{key}: {value}")

#     print("\nCUDA Device Information:")
#     cuda_info = get_cuda_info()
#     if isinstance(cuda_info, list):
#         for device in cuda_info:
#             for key, value in device.items():
#                 print(f"{key}: {value}")
#             print()
#     else:
#         print(cuda_info)


# import torch


# def get_available_cuda_versions():
#     cuda_versions = []
#     if torch.cuda.is_available():
#         cuda_devices = torch.cuda.device_count()
#         for i in range(cuda_devices):
#             cuda_version = torch.cuda.get_device_properties(i).major
#             cuda_versions.append(cuda_version)
#     return cuda_versions


# if __name__ == "__main__":
#     cuda_versions = get_available_cuda_versions()
#     if cuda_versions:
#         print("Available CUDA versions:", cuda_versions)
#         # Use the first CUDA device
#         device = torch.device(f"cuda:0")
#     else:
#         print("No CUDA devices available.")
#         device = torch.device("cpu")

#     print("Using device:", device)


import torch


def get_available_cuda_versions():
    cuda_versions = []
    if torch.cuda.is_available():
        cuda_devices = torch.cuda.device_count()
        for i in range(cuda_devices):
            properties = torch.cuda.get_device_properties(i)
            major_version = properties.major
            minor_version = properties.minor
            cuda_versions.append((major_version, minor_version))
    return cuda_versions


if __name__ == "__main__":
    cuda_versions = get_available_cuda_versions()
    if cuda_versions:
        print("Available CUDA versions:")
        for idx, (major, minor) in enumerate(cuda_versions):
            print(f"CUDA device {idx}: version {major}.{minor}")
        # Use the first CUDA device
        device = torch.device(f"cuda:0")
    else:
        print("No CUDA devices available.")
        device = torch.device("cpu")

    print("Using device:", device)
