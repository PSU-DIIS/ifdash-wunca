from .server import WorkerServer


def create_server():
    from ifdash.utils import config

    settings = config.get_settings()
    server = WorkerServer(settings)

    return server
