import subprocess

# Specify the path to your PowerShell script
script_path = "/content/smhcli/node1.ps1"

# Run the PowerShell script
subprocess.run(["pwsh", "-File", script_path])