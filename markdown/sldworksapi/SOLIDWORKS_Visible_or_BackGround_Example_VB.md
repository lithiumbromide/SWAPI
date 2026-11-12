---
title: "SOLIDWORKS Design Visible or BackGround Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/SOLIDWORKS_Visible_or_BackGround_Example_VB.htm"
---

# SOLIDWORKS Design Visible or BackGround Example (VBA)

## SOLIDWORKS Design Visible or Background Example (VBA)

These examples show several situations for running or attaching to SOLIDWORKS Design sessions through the API.

### SOLIDWORKS Design not running: Launch invisibly and end SOLIDWORKS Design session

```vb
Sub Macro1()
     Dim swApp As Object
     Set swApp = CreateObject("SldWorks.Application")
     ' Close the SOLIDWORKS Design application. If you do not perform this step, SOLIDWORKS Design
      ' continues to run. If SOLIDWORKS Design is running in the background, the user is
      ' unaware that SOLIDWORKS Design is running and consuming their system resources.
     swApp.ExitApp

     Set swApp = Nothing
 End Sub
```

### SOLIDWORKS Design running: Attach to existing SOLIDWORKS Design session and end SOLIDWORKS Design session

```vb
Sub Macro2()
     Dim swApp As Object
     Set swApp = CreateObject("SldWorks.Application")
     swApp.ExitApp
     Set swApp = Nothing
 End Sub
```

### SOLIDWORKS Design not running: Launch invisibly, become visible, and end SOLIDWORKS Design session

```vb
Sub Macro3()
     Dim swApp As Object
     Dim Part As Object
     Set swApp = CreateObject("SldWorks.Application")
     swApp.Visible = True
     swApp.ExitApp
     Set swApp = Nothing
End Sub
```

### SOLIDWORKS Design not running: Launch invisibly, become visible, and leave SOLIDWORKS Design running

```vb
Sub Macro4()
     Dim swApp As Object
     Set swApp = CreateObject("SldWorks.Application")
     swApp.Visible = True
     swApp.UserControl = True
     ' Give control to the user, which leaves SOLIDWORKS Design running
End Sub
```

### SOLIDWORKS Design not running: Launch invisibly, create part invisibly, close part, and end SOLIDWORKS Design session

```vb
Sub Macro5()
     Dim swApp As Object
     Dim Part As Object
     ' This must be explicitly defined for ISldWorks::ActivateDoc2
     Dim errors As Long
     Set swApp = CreateObject("SldWorks.Application")
     Set Part = swApp.NewPart
     Set Part = swApp.ActivateDoc2("Part1",True,errors)
     Set Part = Nothing
     swApp.CloseDoc "Part1"
     swApp.ExitApp
     Set swApp = Nothing
End Sub
```

### SOLIDWORKS Design not running: Launch invisibly, create part invisibly, make the part and SOLIDWORKS Design visible, and leave SOLIDWORKS Design running

```vb
Sub Macro6()
     Dim swApp As Object
     Dim Part As Object
     Set swApp = CreateObject("SldWorks.Application")
     Set Part = swApp.NewPart
     Set Part = swApp.ActivateDoc("Part1")
     Part.Visible = True
     ' Make the part and SOLIDWORKS Design visible
     swApp.UserControl = True
     ' Give control to the user, which leaves SOLIDWORKS Design running
     Set Part = Nothing
     swApp.CloseDoc "Part1"
End Sub
```
