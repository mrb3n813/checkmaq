# checkmaq
---

Simple Python/executable tool to check the value of the ms-DS-MachineAccountQuota attribute in Active Directory. May add more to it later. Was born out of the need to be able to check the MAQ value on a Windows machine with endpoint protection when tools such as NetExec and StandIn are blocked/when the PowerShell ActiveDirectory module is not present.

---

## Compiling to EXE with Nuitka

1. Install Nuitka and other dependencies
   
```
C:\Users\ben\Desktop>python -m pip install numpy zstandard nuitka
```

2. Compile to Executable

While this could probably be done on Linux, the easiest/fastest way is from a Windows VM.

```
C:\Users\ben\Desktop>python -m nuitka --onefile --standalone checkmaq.py

Nuitka-Options: Used command line options: --onefile --standalone checkmaq.py
Nuitka: Starting Python compilation with Nuitka '2.4.11' on Python '3.12' commercial grade 'not installed'.
Nuitka: Completed Python level compilation and optimization.
Nuitka: Generating source code for C backend compiler.
Nuitka: Running data composer tool for optimal constant value handling.
Nuitka: Running C compilation via Scons.
Nuitka-Scons: Backend C compiler: cl (cl 14.3).
Nuitka-Scons: Backend linking program with 210 files (no progress information available for this stage).
Nuitka-Scons: Compiled 210 C files using clcache with 209 cache hits and 1 cache misses.
Nuitka-Plugins:data-files: Included data file 'Crypto\Util\.keep_dir.txt' due to empty dir needed for
Nuitka-Plugins:data-files: 'Crypto.Util._raw_api'.
Nuitka-Postprocessing: Creating single file from dist folder, this may take a while.
Nuitka-Onefile: Running bootstrap binary compilation via Scons.
Nuitka-Scons: Onefile C compiler: cl (cl 14.3).
Nuitka-Scons: Onefile linking program with 1 files (no progress information available for this stage).
Nuitka-Scons: Compiled 1 C files using clcache with 1 cache hits and 0 cache misses.
Nuitka-Onefile: Using compression for onefile payload.
Nuitka-Onefile: Onefile payload compression ratio (25.10%) size 45091958 to 11318390.
Nuitka-Onefile: Keeping onefile build directory 'checkmaq.onefile-build'.
Nuitka: Keeping dist folder 'checkmaq.dist' for inspection, no need to use it.
Nuitka: Keeping build directory 'checkmaq.build'.
Nuitka: Successfully created 'checkmaq.exe'.
```

---

## Usage

You will need a value domain user/password, the domain name and the Distinguished Name (dn) of the domain, i.e. DC=ACME,DC=LOCAL

```
C:\Users\ben\Desktop>checkmaq.exe -h

usage: checkmaq.exe [-h] -u USERNAME -p PASSWORD -d DOMAIN -dn DISTINGUISHED_NAME

Check ms-DS-MachineAccountQuota for a domain.

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username (without domain)
  -p PASSWORD, --password PASSWORD
                        Password
  -d DOMAIN, --domain DOMAIN
                        Domain (e.g., acme.local)
  -dn DISTINGUISHED_NAME, --distinguished-name DISTINGUISHED_NAME
                        Target Distinguished Name (e.g., DC=acme,DC=local)
```

---

## Future Additions

I may eventually add some additional functionality such as:

- Suppressing certificate validation for LDAPS
- Outputting results in JSON format, or other formats
- Writing to a log file
- Username/password prompt instead of command-line args (to avoid showing them in process list) (ie. `--prompt`)
- `--use-ldaps`
- Some verbosity

