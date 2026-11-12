---
title: "Run Macro"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapi/Run_Macro_VB.htm"
---

# Run Macro

This example shows how to use ISldWorks::RunMacro.

You can only:

- Execute a Sub that takes no arguments and that is not part of a class or form.
- Open forms from within a Sub; you cannot start a form directly.

```vb
'--------------------------------------
'
' RunMacroMain.swp
'
'--------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim boolstatus As Boolean

Sub main()

Set swApp = Application.SldWorks

Dim filename As String
filename = swApp.GetCurrentMacroPathName
filename = Left(filename, InStrRev(filename, "\")) + "RunMacroSub.swp"
boolstatus = swApp.RunMacro(filename, "RunMacroSub1", "alternate")
boolstatus = swApp.RunMacro(filename, "RunMacroSub1", "main")
End Sub

'---------------------------------------
'
' RunMacroSub.swp
'
'---------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks

Sub alternate()

Set swApp = Application.SldWorks
swApp.SendMsgToUser "RunMacroSub1:alternate() called"
End Sub

Sub main()

Set swApp = Application.SldWorks
swApp.SendMsgToUser "RunMacroSub1:main() called"
End Sub
```
