[![Test](https://github.com/salmiyounes/pcmffi/actions/workflows/test.yml/badge.svg)](https://github.com/salmiyounes/pcmffi/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/github/license/salmiyounes/pcmffi)](https://github.com/salmiyounes/pcmffi/blob/master/LICENSE.txt)

pcmffi
======

Python [CFFI](https://cffi.readthedocs.io/en/stable/) bindings for [proc_maps_parser](https://github.com/ouadev/proc_maps_parser) 
lightweight library to parse Linux's /proc/[pid]/maps file.

## Usage

```python
from pcmffi import ProcMaps

with ProcMaps.from_pid(2049) as maps:
    for map_ in maps:
        if map_.contains(0x58dd77541000): # Or `in` can be used to check address inclusion
            print("this map contains some address!")
        print(f"{map_.start_addr}: {map_.pathname}")
```
For a usage example see [examples](https://github.com/salmiyounes/pcmffi/tree/master/examples)

## Contribution

Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

## License

pcmffi is under the MIT License. Check out [LICENSE.txt](https://github.com/salmiyounes/pcmffi/blob/master/LICENSE.txt) for the full text.
