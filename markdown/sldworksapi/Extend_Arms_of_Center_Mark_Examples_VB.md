---
title: "Extend Arms of Center Mark Examples (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Extend_Arms_of_Center_Mark_Examples_VB.htm"
---

# Extend Arms of Center Mark Examples (VBA)

This example shows how to extend the arms (handles) of a center mark.

```vb
'------------------------------------------
'
' Preconditions: Drawing document is open and
'                has a Drawing View1 with a center mark.
'
' Postconditions: The bottom and right-side arms are extended.
'
'------------------------------------------
Option Explicit

Sub main()

    Dim swApp As SldWorks.SldWorks
    Dim swDraw As SldWorks.DrawingDoc
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swCenterMark As SldWorks.CenterMark
    Dim dExt2 As Double, dExt3 As Double
    Dim boolstatus As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
    Set swDraw = swModel

   ' Active the drawing view and select the center mark
    boolstatus = swDraw.ActivateView("Drawing View1")
    boolstatus = swModelDocExt.SelectByID2("DetailItem353@Drawing View1", "CENTERMARKSYM", 0.09197936270506, 0.1129166587377, 0, False, 0, Nothing, 0)
    Set swCenterMark = swSelMgr.GetSelectedObject6(1, -1)
    swModel.ClearSelection2 True

    ' Get the lengths of the bottom and right-side arms of the center mark
    dExt2 = swCenterMark.GetExtendedLength(0, swCenterMarkHandle_Down)
    dExt3 = swCenterMark.GetExtendedLength(0, swCenterMarkHandle_Right)
    Debug.Print "Length of arms before extension: " & dExt2 & "; " & dExt3

    ' Extend the bottom and right-side arms of the center mark
    boolstatus = swCenterMark.SetExtendedLength(0, swCenterMarkHandle_Down, 0.03)
    boolstatus = swCenterMark.SetExtendedLength(0, swCenterMarkHandle_Right, 0.02)

    ' Get the revised lengths of the bottom and right-side arms of the center mark
    dExt2 = swCenterMark.GetExtendedLength(0, swCenterMarkHandle_Down)
    dExt3 = swCenterMark.GetExtendedLength(0, swCenterMarkHandle_Right)
    Debug.Print "Length of arms after extension: " & dExt2 & "; " & dExt3

End Sub
```
