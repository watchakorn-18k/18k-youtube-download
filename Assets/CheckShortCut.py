import os,winshell,sys,ctypes

desktop = winshell.desktop()
files = os.listdir(desktop)
print()
# exit()
def AlertCreateShortCut(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def CheckShortCut():
  if "18k-youtube-download.lnk" not in files:
      CheckYesNo = AlertCreateShortCut('สร้างทางลัด 18k youtube download ไปหน้าเดสก์ท็อป', 'คุณต้องการสร้างทางลัด 18k youtube download ไปหน้าเดสก์ท็อปหรือไม่',4)
      if CheckYesNo == 6:
        winshell.CreateShortcut(
  Path=os.path.join(winshell.desktop(), "18k-youtube-download.lnk"),
  Target=f"{os.getcwd()}\\18k-youtube-download.exe",
  Icon=(f"{os.getcwd()}\\18k-youtube-download.exe", 0),
  Description="18k youtube download"
  )