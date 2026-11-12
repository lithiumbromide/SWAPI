---
title: "Get Crosshatches on View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Crosshatches_on_View_Example_VB.htm"
---

# Get Crosshatches on View Example (VBA)

## Get Crosshatches on the View Example (VBA)

This example shows how to iterate the drawing views and get the crosshatches in the current drawing view.

```vb
'----------------------------------------------
'
' Preconditions: Drawing document is open and contains at least one drawing view.
'
' Postconditions: None
'
'----------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swDrawing As SldWorks.DrawingDoc
Dim currentView As SldWorks.View

Sub main()

Set swApp = Application.SldWorks
Set swDrawing = swApp.ActiveDoc

' Iterate the drawing views
Set currentView = swDrawing.GetFirstView
While Not currentView Is Nothing
    ' Get the crosshatch count on the view
    Debug.Print currentView.GetFaceHatchCount
    If currentView.GetFaceHatchCount = 0 Then
        Set currentView = currentView.GetNextView
    Else
        ' Get the crosshatches on the view
        Dim hatcharray As Variant
        hatcharray = currentView.GetFaceHatches

        ' Following FaceHatch properties are accessible to you
        Debug.Print hatcharray(1).Pattern
        Debug.Print hatcharray(1).angle
        Debug.Print hatcharray(1).Color
        Debug.Print hatcharray(1).Layer
        Debug.Print hatcharray(1).Scale2
        Debug.Print hatcharray(1).SolidFill

        Set currentView = currentView.GetNextView

    End If
Wend
End Sub
```
