---
title: "List Center Marks in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/List_Center_Marks_in_Drawing_Example_VB.htm"
---

# List Center Marks in Drawing Example (VBA)

This example shows how to list all of the center marks in all of the drawing views in a drawing.

```vb
'-------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing with one or more center marks in any view.
 ' 2. Open the Immediate window.
 '
 ' Postconditions: Examine the Immediate window.
 '-------------------------------------------------------------------
Option Explicit

Public Enum swCenterMarkStyle_e
    swCenterMark_NonAnnotation = 1
    swCenterMark_Single = 2
    swCenterMark_LinearGroup = 3
    swCenterMark_CircularGroup = 4
End Enum

Sub main()

    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim swView                      As SldWorks.View
    Dim vCenterMarkArr              As Variant
    Dim vCenterMark                 As Variant
    Dim swCenterMark                As SldWorks.CenterMark
    Dim bRet                        As Boolean

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swView = swDraw.GetFirstView

    Debug.Print "File = " & swModel.GetPathName

    Do While Not swView Is Nothing
        Debug.Print "  View = " + swView.GetName2

        Set swCenterMark = swView.GetFirstCenterMark2
        Do While Not swCenterMark Is Nothing
            vCenterMarkArr = swView.GetCentermarks
            Debug.Assert Not IsEmpty(vCenterMarkArr)
            Debug.Print "    CenterLineFont           = " & swCenterMark.CenterLineFont
            Debug.Print "    ConnectionLines          = " & swCenterMark.ConnectionLines
            ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
            Debug.Print "    RotationAngle            = " & swCenterMark.RotationAngle * 57.3 & " degrees"
            Debug.Print "    ShowLines                = " & swCenterMark.ShowLines
            Debug.Print "    Size                     = " & swCenterMark.Size
            Debug.Print "    Style                    = " & swCenterMark.Style
            Debug.Print "    UseDocDisplaySettings    = " & swCenterMark.UseDocDisplaySettings
            Debug.Print ""

            Set swCenterMark = swCenterMark.GetNext
        Loop

        Set swView = swView.GetNextView
    Loop
End Sub
```
