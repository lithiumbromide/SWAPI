---
title: "Get Base Views Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Base_Views_Example_VB.htm"
---

# Get Base Views Example (VBA)

This example shows how to get the names of the base views for all of the views in a drawing.

```vb
'-------------------------------------
'
' Preconditions: Drawing document is open.
'
' Postconditions: None
'
'--------------------------------------
Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim swView                      As SldWorks.View
    Dim swBaseView                  As SldWorks.View
    Dim bRet                        As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swView = swDraw.GetFirstView

    Debug.Print "File = " & swModel.GetPathName

    Do While Not swView Is Nothing
        ' Returns NULL if no parent
        Set swBaseView = swView.GetBaseView

        Debug.Print "  " & swView.Name

        If Not swBaseView Is Nothing Then
            Debug.Print "    --> " & swBaseView.Name
        End If

        Set swView = swView.GetNextView
    Loop
End Sub
'-------------------------------------
```
