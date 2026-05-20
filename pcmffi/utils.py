from ctypes import sizeof, c_void_p

CPU_64BITS = sizeof(c_void_p) == 8


def formatUintHex64(value: int) -> str:
    """
    Format an 64 bits unsigned integer.
    """
    return "0x%016x" % value


def formatUintHex32(value: int) -> str:
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


if CPU_64BITS:
    formatWordHex = formatUintHex64
else:
    formatWordHex = formatUintHex32


def format_address(address: int) -> str:
    if address:
        return formatWordHex(address)
    else:
        return "NULL"


def format_address_range(start: int, end: int) -> str:
    return "{}-{}".format(format_address(start), format_address(end))
