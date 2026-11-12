---
title: "Set BOM Balloon Text Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_BOM_Balloon_Example_VB.htm"
---

# Set BOM Balloon Text Example (VBA)

This example shows how to set the text in a BOM balloon with custom text.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a drawing document with a split-circle BOM balloon
'    with custom text in the upper and lower portions of
'    of the balloon.
' 2. Select the balloon specified in step 1.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Appends new text to the existing text in the selected balloon.
' 2. Examine the selected balloon in the drawing and the
'    the Immediate window.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swNote                      As SldWorks.Note
    Dim swAnn                       As SldWorks.Annotation
    Dim bRet                        As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swNote = swSelMgr.GetSelectedObject6(1, -1)
    Set swAnn = swNote.GetAnnotation
    Debug.Assert swNote.IsBomBalloon
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Name = " & swAnn.GetName
    Debug.Print "    Upper text = " & swNote.GetBomBalloonText(True) & " [" & swNote.GetBomBalloonTextStyle(True) & "]"
    Debug.Print "    Lower text = " & swNote.GetBomBalloonText(False) & " [" & swNote.GetBomBalloonTextStyle(False) & "]"
```

```
    ' Append new text to existing text if balloon has custom text
    bRet = swNote.SetBomBalloonText(swNote.GetBomBalloonTextStyle(True), swNote.GetBomBalloonText(True) & " Upper", swNote.GetBomBalloonTextStyle(False), swNote.GetBomBalloonText(False) & " Lower")
```

```
End Sub
```
