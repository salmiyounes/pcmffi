from ctypes import sizeof, c_void_p

IS_64BIT = sizeof(c_void_p) == 8


def format_uint_hex64(value: int) -> str:
    """
    Format an 64 bits unsigned integer.
    """
    return "0x%016x" % value


def format_uint_hex32(value: int) -> str:
    """
    Format an 32 bits unsigned integer.
    """
    return "0x%08x" % value


def to_bytes(s: str | bytes) -> bytes:
    if isinstance(s, bytes):
        return s
    return str(s).encode()


def to_str(s: str | bytes) -> str:
    if isinstance(s, str):
        return s
    return bytes(s).decode()


if IS_64BIT:
    format_word_hex = format_uint_hex64
else:
    format_word_hex = format_uint_hex32


def format_address(address: int) -> str:
    if address:
        return format_word_hex(address)
    else:
        return "NULL"


def format_address_range(start: int, end: int) -> str:
    return "{}-{}".format(format_address(start), format_address(end))
