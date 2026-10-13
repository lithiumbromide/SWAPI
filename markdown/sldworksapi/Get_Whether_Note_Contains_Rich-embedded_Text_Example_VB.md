---
title: "Get Whether Note Contains Rich Embedded Text Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Note_Contains_Rich-embedded_Text_Example_VB.htm"
---

# Get Whether Note Contains Rich Embedded Text Example (VBA)

This example shows how to find out if a note contains rich embedded text.

```
'-----------------------------------
' Preconditions:
' 1. Open a model document containing a
'    multi-string note.
' 2. Italicize one of the strings in the note.
' 3. Select the note.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Gets:
'    a. selected note.
'    b. whether the note contains rich-embedded
'       text.
' 2. Examine the Immediate window.
' 3. Uncomment the executable commented code statements.
' 4. Run the macro again.
' 5. Examine the Immediate window.
'-----------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swNote As SldWorks.Note
Dim swTextFormat As SldWorks.TextFormat
Dim swAnnotation As SldWorks.Annotation
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModelDoc = swApp.ActiveDoc
    Set swSelMgr = swModelDoc.SelectionManager
    Set swNote = swSelMgr.GetSelectedObject6(1, 0)
    'Set swAnnotation = swNote.GetAnnotation
    'Set swTextFormat = swAnnotation.GetTextFormat(0)
    'swTextFormat.Bold = True
    ' IAnnotation::SetTextFormat should return false because
    ' note contains rich-embedded text
    'boolstatus = swAnnotation.SetTextFormat(0, False, swTextFormat)
    'Debug.Print "Text format set? " & boolstatus
    boolstatus = swNote.HasMultipleFonts
    Debug.Print "Does selected note have multiple fonts? " & boolstatus
```

```
End Sub
```
