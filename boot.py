import storage, os
storage.remount("/", readonly=False)
os.rename("/boot.py", "/bootX.py")
