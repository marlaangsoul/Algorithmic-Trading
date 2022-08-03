from pywinauto import application
from pywinauto import timings
import time
import os

app = application.Application()
app.start(r"C:\KiwoomFlash3\Bin\NKMiniStarter.exe")

title = "번개 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('yyyy')

cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys('xxxx')

btn_ctrl = dlg.Button0
btn_ctrl.Click()

