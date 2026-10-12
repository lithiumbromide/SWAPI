---
title: "Show Named View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Show_Named_View_Example_VB.htm"
---

# Show Named View Example (VBA)

This example shows how to get the name of a named view in an open model document.

```vb
'--------------------------------------
'
' Preconditions: Model document is open.
'
' Postconditions: None
'
'---------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Sub main()
    Dim swModel      As SldWorks.ModelDoc2
    Dim lIdx         As Long
    Dim vTransform   As Variant

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    For lIdx = swStandardViews_e.swFrontView To swStandardViews_e.swDimetricView
        Debug.Print "View = " & PrintViewName(lIdx) & " (" & lIdx & ")"
        vTransform = swModel.GetStandardViewRotation(lIdx)
        swModel.ShowNamedView2 "", lIdx
        Stop
    Next lIdx
End Sub
Private Function PrintViewName(ByVal nView As swStandardViews_e) As String
    PrintViewName = "<not a standard view>"
    Select Case (nView)
        Case swStandardViews_e.swBackView
            PrintViewName = "Back"
        Case swStandardViews_e.swBottomView
            PrintViewName = "Bottom"
        Case swStandardViews_e.swDimetricView
            PrintViewName = "Dimetric"
        Case swStandardViews_e.swFrontView
            PrintViewName = "Front"
        Case swStandardViews_e.swIsometricView
            PrintViewName = "Isometric"
        Case swStandardViews_e.swLeftView
            PrintViewName = "Left"
        Case swStandardViews_e.swRightView
            PrintViewName = "Right"
        Case swStandardViews_e.swTopView
            PrintViewName = "Top"
        Case swStandardViews_e.swTrimetricView
            PrintViewName = "Trimetric"
    End Select
End Function
```
