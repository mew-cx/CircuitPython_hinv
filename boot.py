import storage, os
storage.remount("/", readonly=False)
os.rename("/boot.py", "/boot.py_")
