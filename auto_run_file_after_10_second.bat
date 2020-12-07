@echo off
:TOP
@ECHO … Please wait 10 second open …..
@ECHO … 10 giay nua phan mem CCleaner se duoc kich hoat…
@ECHO … viet them nhung gi ban muon vao day …



:loop

@ping 127.0.0.1 -n 10 > NUL
start /d "C:\Program Files\Google\Chrome\Application\" chrome.exe

goto loop