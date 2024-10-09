import os

mime_types = {
    "html": "text/html",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "htm": "text/html",
    "txt": "text/plain",
}
def invalid_path(path, server_root):
    file_path = os.path.join(server_root, path[1:])
    file_path = os.path.abspath(file_path)
    if not file_path.startswith(server_root):
        return True
def get_mime_type(file_path):
    ext = file_path.split('.')[-1]
    return mime_types.get(ext, "application/octet-stream")
def read_file(file_path, server_root):
    file_path = os.path.join(server_root, file_path[1:])
    file_path = os.path.abspath(file_path)
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return None