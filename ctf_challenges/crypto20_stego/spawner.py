# spawner.py
import subprocess, sys
if len(sys.argv) != 3:
    print("usage: spawner.py <team> <flag>")
    sys.exit(1)
team = sys.argv[1]; flag = sys.argv[2]
name = f"crypto20_{team}"
cmd = ["docker","run","-d","--name",name,"--network","ctf_net","-e",f"FLAG={flag}",
       "--memory=200m","--cpus=.25","-p","0:8080","crypto20_stego:latest"]
p = subprocess.run(cmd, capture_output=True, text=True)
if p.returncode:
    print("error:", p.stderr); sys.exit(2)
print("started:", p.stdout.strip())
print("mapping:", subprocess.run(["docker","port",name,"8080"], capture_output=True, text=True).stdout.strip())
