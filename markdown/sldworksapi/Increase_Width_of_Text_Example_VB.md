---
title: "Increase Width of Text Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Increase_Width_of_Text_Example_VB.htm"
---

# Increase Width of Text Example (VBA)

This example shows how to increase the width of the text in a note by a factor of 2.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.slddrw.
' 2. Select the note Fixed Face.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Increases the width of the text in the selected note
'    by a factor of 2.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not
' save changes.
'-------------------------------------------------------
```

```vb
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.modelDoc
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swAnnObj                    As Object
    Dim swAnnotation                As SldWorks.Annotation
    Dim swTextFormat                As SldWorks.textFormat
    Dim dWidth                      As Double
    Dim bRet                        As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swAnnObj = swSelMgr.GetSelectedObject5(1)
    Set swAnnotation = swAnnObj.GetAnnotation
    Set swTextFormat = swAnnotation.GetTextFormat(0)

    dWidth = swTextFormat.WidthFactor
    Debug.Print "Old width = " & dWidth

    swTextFormat.WidthFactor = 2# * dWidth

    bRet = swAnnotation.SetTextFormat(0, False, swTextFormat)
    dWidth = swTextFormat.WidthFactor
    Debug.Print "New width = " & dWidth
End Sub
```
