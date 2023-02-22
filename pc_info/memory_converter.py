def get_size(bytes):
    """
    Scale bytes to its proper format
    e.g:
    1253656 => '1.20MB'
    1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "KB", "MB", "GB", "TB", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}"
        bytes /= factor
        