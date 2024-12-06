#!/usr/bin/env python3
import platform, argparse, os, time

parser = argparse.ArgumentParser('pyplatform', description='Python-based system information giver using platform module', epilog='thanks! ;  main Branch ; updated 2024-12-5 ; by Nacroni')
parser.add_argument('-f', '--freedesktop', help='[bool] prints the freedesktop.org OS release information', nargs='?', const=True, default=False, type=bool)
parser.add_argument('-w', '--win32', help='[bool] prints Win32 information', nargs='?', const=True, default=False, type=bool)
parser.add_argument('-m', '--mac', help='[bool] prints macOS information', nargs='?', const=True, default=False, type=bool)
args = parser.parse_args()

freedesktop_enable = args.freedesktop
win32_enable = args.win32
mac_enable = args.mac

print('System Information')

system = platform.system()
user = os.getlogin()
node = platform.node()
release = platform.release()
version = platform.version()
machine = platform.machine()
processor = platform.processor()
uptime_monotonic = time.monotonic()
uptime_boottime = time.clock_gettime(time.CLOCK_BOOTTIME)

print(f'    System:       {system}'          )
print(f'    User:         {user}'            )
print(f'    Node:         {node}'            )
print(f'    Uptime Awake: {uptime_monotonic}') # nac: should we call this monotonic or awake?
print(f'    Uptime:       {uptime_boottime}' )
print(f'    Release:      {release}'         )
print(f'    Version:      {version}'         )
print(f'    Machine:      {machine}'         )
print(f'    Processor:    {processor}'       )

if freedesktop_enable:
    print()
    print('freedesktop.org Information')
    
    freedesktop_release = platform.freedesktop_os_release()
    
    print(f'    OS Release: {freedesktop_release}')

if 'Windows' in system or win32_enable:
    print()
    print('Windows (Win32) Information')
    
    win32_ver = platform.win32_ver()
    win32_ed = platform.win32_edition()
    win32_is_iot = platform.win32_is_iot()
    
    print(f'    Version: {win32_ver}'   )
    print(f'    Edition: {win32_ed}'    )
    print(f'    Is IoT:  {win32_is_iot}')
    
if 'macOS' in system or 'Mac' in system or mac_enable:
    print()
    print('macOS Information')
    
    mac_ver = platform.mac_ver()
    
    print(f'    Version: {mac_ver}')

print()
print('Python Information')

python_ver = platform.python_version()
python_br = platform.python_branch()
python_build = platform.python_build()
python_comp =  platform.python_compiler()
python_imp = platform.python_implementation()
python_rev = platform.python_revision()

print(f'    Version:        {python_ver}'  )
print(f'    Branch:         {python_br}'   )
print(f'    Build:          {python_build}')
print(f'    Compiler:       {python_comp}' )
print(f'    Implementation: {python_imp}'  )
print(f'    Revision:       {python_rev}'  )
