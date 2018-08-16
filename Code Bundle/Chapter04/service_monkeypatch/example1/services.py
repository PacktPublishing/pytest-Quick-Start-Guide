import subprocess


def start_service(service_name):
    subprocess.run(f"docker run {service_name}")
