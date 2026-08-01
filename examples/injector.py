from typing import List
import sys
import argparse
from ptrace import debugger
from ptrace.debugger.process import PtraceProcess
from pcmffi import ProcMaps 

'''
    1250:       e8 2b fe ff ff          call   1080 <strcmp@plt>
    1255:       85 c0                   test   %eax,%eax
    1257:       75 69                   jne    12c2 <main+0x139>
    1259:       48 8d 05 42 0e 00 00    lea    0xe42(%rip),%rax        # 20a2 <_IO_stdin_used+0xa2>
    1260:       48 89 c7                mov    %rax,%rdi
    1263:       e8 c8 fd ff ff          call   1030 <puts@plt>
    1268:       c7 85 44 ff ff ff 00    movl   $0x0,-0xbc(%rbp)
'''

def runtime_memory_address(pid: int, offset: int) -> int:
    with ProcMaps.from_pid(pid) as maps:
        m = iter(maps).__next__()
        return offset + m.start_addr

def inject(pid: int, offset: int = 0x1257, shellcode: bytes = b'\x90\x90') -> None:
    dbg = debugger.PtraceDebugger()
    process = dbg.addProcess(pid=pid, is_attached=False)
    
    # Inject code
    target_addr = runtime_memory_address(
        pid=pid,
        offset=offset
    )
    tracer = PtraceProcess(debugger=dbg, pid=pid, is_attached=True)
    tracer.writeBytes(
        address=target_addr,
        bytes=shellcode
    )

    process.detach()
    dbg.quit()

def main(args: List[str]) -> None:
    parser = argparse.ArgumentParser(description="Runtime patcher")
    parser.add_argument("-p", "--pid", type=int, required=True, help="Target PID")
    parser.add_argument("-o", "--offset", type=int, default=0x1257, help="Offset value")
    
    parsed_args = parser.parse_args(args[1:])
    inject(pid=parsed_args.pid, offset=parsed_args.offset)
    return

if __name__ == "__main__":
    main(sys.argv)
