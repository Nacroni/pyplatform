# `pyplatform`

`pyplatform` is a script that shows information about your system. It mainly uses the `platform` module in Python.

## Usage

### Running 

You can use `pyplatform` by either opening it normally using Python, or by opening it directly, as long as the script has the executable permission.

#### Python (All Platforms)

```bash
python ./pyplatform.py
```

#### Direct Execution (only on certain platforms)

```bash
chmod +x ./pyplatform.py # You don't need to do this if it already has the executable permission.
./pyplatform.py
```

### Arguments

#### Freedesktop OS Release info : `-f`, `--freedesktop`

This argument shows the output of `platform.freedesktop_os_release()`, which shows JSON-formatted information about your system.

#### Win32 info : `-w`, `--win32`

This argument shows the output of `platform.win32_ver()`, `platform.win32_edition()`, and `platform.win32_is_iot()`.

- **`platform.win32_ver()`** / **Version**: Shows the version of Windows you are running.

- **`platform.win32_edition()`** / **Edition**: Shows the edition of Windows.

- **`platform.win32_is_iot()`** / **Is IoT / Is Embedded**: Shows whether or not your system is Windows IoT/Embedded (?)

#### macOS info : `-m`, `--mac`

This argument shows the output of `platform.mac_ver()`.

- **`platform.mac_ver()`** / **Version**: Shows the version of macOS you are running.

#### Help : `-h`, `--help`

This argument shows help about how to use the script.
