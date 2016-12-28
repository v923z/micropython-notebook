def calcsize(fmt):
    """Return the number of bytes needed to store the given fmt."""
    pass

def pack(fmt, v1, v2, ):
    """Pack the values v1, v2, ... according to the format string fmt. The return value is a bytes object encoding the values."""
    pass

def pack_into(fmt, buffer, offset, v1, v2, ):
    """Pack the values v1, v2, ... according to the format string fmt into a buffer starting at offset. offset may be negative to count from the end of buffer."""
    pass

def unpack(fmt, data):
    """Unpack from the data according to the format string fmt. The return value is a tuple of the unpacked values."""
    pass

def unpack_from(fmt, data, offset=0):
    """Unpack from the data starting at offset according to the format string fmt. offset may be negative to count from the end of buffer. The return value is a tuple of the unpacked values."""
    pass