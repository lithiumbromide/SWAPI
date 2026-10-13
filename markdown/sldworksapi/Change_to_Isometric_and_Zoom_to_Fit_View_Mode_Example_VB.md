---
title: "Change to Isometric and Zoom to Fit View Mode Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_to_Isometric_and_Zoom_to_Fit_View_Mode_Example_VB.htm"
---

# Change to Isometric and Zoom to Fit View Mode Example (VBA)

This example shows how to change the current view mode to isometric and Zoom to Fit.

```vb
'-----------------------------------------------
'
' Preconditions: Model document is open.
'
' Postconditions: Current view mode is changed to isometric and Zoom to Fit.
'
'-----------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc

    ' Not quite the same as when done through the user interface;
    ' model is zoomed out a bit further
    swModel.ShowNamedView2 "*Isometric", -1

    ' Now view the same as done through the user interface
    swModel.ViewZoomtofit2
End Sub
'-----------------------------------------------
```
