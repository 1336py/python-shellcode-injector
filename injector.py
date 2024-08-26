import pymem
import subprocess

class Injector:
    def __init__(self, proc):
        self.proc = proc
        try:
            self.mem = pymem.Pymem(self.proc)  # Attach to the process
          
        except pymem.exception.ProcessNotFound:
            subprocess.Popen(self.proc)  # Start the process if it's not running
            self.mem = pymem.Pymem(self.proc)

    def inject(self, code):
        """
        Injects Python shellcode into the target process.
        """
      
        # Inject the shellcode
        self.mem.inject_python_shellcode(code)
