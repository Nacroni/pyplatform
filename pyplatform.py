#!/usr/bin/env python3
import platform, argparse, os

pyplatform_version = 0.8

parser = argparse.ArgumentParser('platform_test')
parser.add_argument('-f', '--freedesktop', help='prints the freedesktop.org OS release information', action='store_true')
parser.add_argument('-w', '--win32', help='prints Win32 information', action='store_true')
parser.add_argument('-m', '--mac', help='prints macOS information', action='store_true')
parser.add_argument('-v', '--version', help='prints pyplatform version', action='store_true')
args = parser.parse_args()

freedesktop_enable = args.freedesktop
win32_enable = args.win32
mac_enable = args.mac
version_enable = args.version

if version_enable:
    print(f'{str(pyplatform_version)}')
    exit()

print('System Information')

system = platform.system()
user = os.getlogin()
node = platform.node()
release = platform.release()
version = platform.version()
machine = platform.machine()
processor = platform.processor()

print(f'    System:    {system}'   )
print(f'    User:      {user}'     )
print(f'    Node:      {node}'     )
print(f'    Release:   {release}'  )
print(f'    Version:   {version}'  )
print(f'    Machine:   {machine}'  )
print(f'    Processor: {processor}')

if freedesktop_enable:
    freedesktop_release = platform.freedesktop_os_release()
    print()
    print(f'Freedesktop OS Release: {freedesktop_release}')

if 'Windows' in system or win32_enable:
    win32_ver = platform.win32_ver()
    win32_ed = platform.win32_ver()
    win32_is_iot = platform.win32_is_iot()
    print()
    print('Win32 Information')
    print(f'    Version: {win32_ver}'   )
    print(f'    Edition: {win32_ed}'    )
    print(f'    Is IOT:  {win32_is_iot}')
    
if ['macOS', 'Mac'] in system or mac_enable:
    mac_ver = platform.mac_ver()
    print()
    print('macOS Information')
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