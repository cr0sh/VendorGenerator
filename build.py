from cx_Freeze import setup, Executable
setup(
    name = "VendorGenerator",
    version = "0.1b",
    description = "Android vender-blobs.mk generator",
    executables = [Executable("main.py")]
    )
