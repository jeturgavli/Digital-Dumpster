Start-Process "C:\Program Files (x86)\epson\Epson Scan 2\Core\es2launcher.exe"

# Wait a bit for the program to open (adjust 3-5 sec if needed)
Start-Sleep -Seconds 2

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
