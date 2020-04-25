# Python Script for Enabling Hot Reloading

- This file contains a function, `restart()` that checks for modifications to the current file
- Upon modification, the script re-runs itself



## How it works

- Creates a thread for the `restart()` function to run
- Loops forever, checking whether the `mtime` (modification time) has changed since the script was last run


## TODO
- Make this whole thing a class
- Use subprocesses so that an error in the file will still hot reload correctly


## Note

- If you are getting `OSError: [Errno 8] Exec format error`
  - Try making the file executable using `chmod +x <your_file_name.py>`
  - Try adding a shebang to the top of the file, e.g. `#!/usr/bin/env python`

- This should work as is on `Windows 10` - have not tested on `OSX`
