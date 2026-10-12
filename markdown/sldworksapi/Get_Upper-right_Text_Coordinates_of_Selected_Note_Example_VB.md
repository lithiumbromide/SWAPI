---
title: "Get Upper-right Text Coordinates of Selected Note Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Upper-right_Text_Coordinates_of_Selected_Note_Example_VB.htm"
---

# Get Upper-right Text Coordinates of Selected Note Example (VBA)

This example shows how to get the coordinates for the upper-right text point in a selected note.

```
'----------------------------------------
' Preconditions:
' 1. Open a model document containing a note.
' 2. Select the note.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets:
'    a. selected note.
'    b. name of the note.
'    c. note's upper-right text point's coordinates.
' 2. Examine the Immediate window.
'-----------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swNote As SldWorks.Note
    Dim vpoints  As Variant
    Dim i As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swNote = swSelMgr.GetSelectedObject6(1, 0)
    Debug.Print swNote.GetName
        vpoints = swNote.GetUpperRight
        For i = 0 To UBound(vpoints)
            Debug.Print vpoints(i)
        Next i
End Sub
```
