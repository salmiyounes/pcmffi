pcmffi
======

Python [CFFI](https://cffi.readthedocs.io/en/stable/) bindings for [proc_maps_parser](https://github.com/ouadev/proc_maps_parser) 

## Usage

```python
from pcmffi import ProcMaps

with ProcMaps.from_pid(2049) as maps:
    for map_ in maps:
        if map_.contains(0x58dd77541000): # Or `in` can be used to check address inclusion
            print("this map contains some address!")
        print(f"{map_.start_addr}: {map_.pathname}")
```