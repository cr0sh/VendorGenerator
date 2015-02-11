from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "sys"], "excludes": ["tkinter"]}
includes = ["sys", "os", "time", "subprocess"]
setup(
    name = "VendorGenerator",
    version = "0.1b",
    description = "Android vender-blobs.mk generator",
    executables = [Executable("main.py")]
    )
