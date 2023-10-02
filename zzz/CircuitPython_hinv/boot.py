# boot.py
import storage, os
storage.remount("/", readonly=False)
# move this file, so it won't be loaded on next boot.
os.rename("/boot.py", "/boot.py_")
