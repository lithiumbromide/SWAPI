---
title: "Rotate Drawing Views 45 Degrees Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Drawing_View_45_Degrees_Example_VB.htm"
---

# Rotate Drawing Views 45 Degrees Example (VBA)

This example shows how to rotate the selected drawing view 45º .

```
'--------------------------------------------------------------
' Preconditions: Verify that the specified file to open exists.
'
' Postconditions: Rotates the selected drawing view 45º.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\driveworksxpress\mobile gantry.slddrw", swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
swModel.ViewZoomtofit2
Set swDrawing = swModel
```

```
status = swDrawing.ActivateView("Drawing View4")
status = swModelDocExt.SelectByID2("Drawing View4", "DRAWINGVIEW", 0.1122300799499, 0.1471819585104, 0, False, 0, Nothing, 0)
```

```
'Convert degrees to radians, the default system unit
' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
status = swDrawing.DrawingViewRotate(45 / 57.3)
```

```
End Sub
```
