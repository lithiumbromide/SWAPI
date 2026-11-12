---
title: "Create Compound Note Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Compound_Note_Example_VB.htm"
---

# Create Compound Note Example (VBA)

This example shows how to create a compound note in a drawing document.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.slddrw.
' 2. Click the letter E in the drawing view.
'
' Postconditions:
' 1. Creates a compound note.
' 2. Click the compound note and drag it to a different
'    location in the drawing.
'
' NOTE: Because this drawing is used elsewhere, do not save
' changes.
'------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim swNote As SldWorks.note
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swDrawing = swModel
```

```
    ' Create the compound note
    makeCnote
```

```
End Sub
```

```
Sub makeCnote()
```

```
    Set swNote = swDrawing.CreateCompoundNote(0.00635, 0.05, 0.2, 0#)
```

```
     ' Add text to note
     swNote.AddText "zero pt", 0, 0, 0
     swNote.AddText "top", 0.01, 0.01, 0
```

```
     ' Prepare note for geometry
     swNote.BeginSketchEdit
```

```
     ' Add geometry to note
     swDrawing.CreateLineVB 0, 0, 0, 0.01, 0.01, 0
     swDrawing.CreateCircleVB 0, 0, 0, 0.01414
```

```
     ' Finish
     swNote.EndSketchEdit
```

```
    ' Do some queries
    If (swNote.IsCompoundNote()) Then
        Dim count As Long
        Dim n2 As String
        Dim n1 As String
        Dim ht2 As Double
        ' If object is compound note
        ' Get number of text items
        count = swNote.GetTextCount()
        ' Get the second piece of text
        n2 = swNote.GetTextAtIndex(2)
        ' Get the first piece of text
        n1 = swNote.GetTextAtIndex(1)
        ' Get height of 2nd piece of text
        ht2 = swNote.GetHeightAtIndex(2)
```

```
    End If
```

```
End Sub
```
