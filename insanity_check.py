import subprocess
import tempfile
import sys
import time

exec_path = './tools/sanitycheck'
iters = 10
if len(sys.argv) > 1: iters = int(sys.argv[2])

failures = 0
successes = 0
for i in range(iters):
        ptime_start = time.clock();
        wtime_start = time.time();
        with tempfile.TemporaryFile() as tempf:
            proc = subprocess.Popen([exec_path], stdout=tempf)
            proc.wait()
            tempf.seek(0) 
            res = tempf.read()
            passcheck = res.find("This project passes all of the default sanity check cases.") 
            if (passcheck == -1):
                print "[WARNING: Sanitycheck " + str(i) + " failed! (user: " + str(time.time() - wtime_start) + ", cpu: " + str(time.clock() - ptime_start) + ")"
                print(res)
                failures+=1
            else:
                print "[NOTE: Sanitycheck " + str(i) + " passed (" + str(successes) + "/" + str(iters) " overall). Code: " + str(passcheck) + " (user: " + str(time.time() - wtime_start) + "s, cpu: " + str(time.clock() - ptime_start) + "s)]"
                successes+=1
print str(successes) + "/" + str(iters) + " iterations passed."
