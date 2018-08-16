from subprocess import run


def start_service(service_name):
    run(f"docker run {service_name}")
