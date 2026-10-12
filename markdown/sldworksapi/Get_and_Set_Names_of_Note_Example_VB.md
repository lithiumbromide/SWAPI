---
title: "Get and Set Names of Note Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Names_of_Note_Example_VB.htm"
---

# Get and Set Names of Note Example (VBA)

## Get and Set Name of Note Example (VBA)

This example shows how to get the name of the selected note and change its name.

```
'-----------------------------------------------------------------
' Precondition:
' 1. Open public_documents\samples\tutorial\api\2012-sm.slldrw.
' 2. Select the Fixed face note.
'
' Postcondition:
' 1. Changes the name of the selected note to SM Fixed face.
' 2. Click OK to close each message box.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swSelMgr As SldWorks.SelectionMgr
Dim swNote As SldWorks.Note
Dim swAnn As SldWorks.Annotation
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swNote = swSelMgr.GetSelectedObject6(1, 0)
```

```
    ' Get note annotation
    Set swAnn = swNote.GetAnnotation
    ' Get annotation name
    MsgBox swAnn.GetName
    ' Change annotation name; new name must be unique
    swAnn.SetName "SM Fixed face"
    MsgBox swAnn.GetName
```

```
End Sub
```
