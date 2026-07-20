---
title: "Get All Notes in Drawing Template Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_All_Notes_in_Drawing_Template_Example_VB.htm"
---

# Get All Notes in Drawing Template Example (VBA)

This example shows how to get all of the notes in a drawing template.

```
'---------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects all notes in the drawing template.
' 2. Examine the Immediate window and title block in the drawing.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim swNote As SldWorks.Note
    Dim swAnn As SldWorks.Annotation
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swView = swDraw.GetFirstView ' This is the drawing template
    Set swNote = swView.GetFirstNote2
```

```
    swModel.ClearSelection2 (True)
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    Do While Not swNote Is Nothing
        Set swAnn = swNote.GetAnnotation
        bRet = swAnn.Select2(True, 0)
        Debug.Print "  " & swNote.GetName
        Debug.Print "    " & swNote.GetText
        Set swNote = swNote.GetNext
    Loop
```

```
End Sub
```
