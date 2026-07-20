---
title: "Place Note Behind Drawing Sheet Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Place_Note_Behind_Drawing_Sheet_Example_VB.htm"
---

# Place Note Behind Drawing Sheet Example (VBA)

This example shows how to place a note behind a drawing sheet.

```
'----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing file to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Places the selected note, 2012-sm in the drawing template,
'    behind the drawing sheet.
' 2. To verify:
'    a. Examine the Immediate window.
'    b. Right-click the drawing and click
'       Edit Sheet Format.
'    c. Right-click 2012-sm and examine the
'       the short-cut menu to verify that Display
'       Note Behind Sheet is selected.
'    d. Exit drawing sheet edit mode.
'
' NOTE: Because this drawing is used elsewhere, do not
' save changes.
'-----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swNote As SldWorks.Note
Dim fileName As String
Dim status As Boolean
Dim errors As Long, warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open drawing
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\api\2012-sm.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
    Set swDrawing = swModel
```

```
    ' Put drawing template and sheet in edit mode
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Sheet1", "SHEET", 3.99580396732789E-02, 0.20594194865811, 0, False, 0, Nothing, 0)
    swDrawing.EditTemplate
    swDrawing.EditSheet2
```

```
    swModel.ClearSelection2 True
```

```
    ' Select note to place behind the sheet
    status = swModelDocExt.SelectByID2("DetailItem3@Sheet Format1", "NOTE", 0.155548914819136, 0.017885845974329, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swNote = swSelectionMgr.GetSelectedObject6(1, -1)
    swNote.BehindSheet = True
    Debug.Print ("Was the selected note placed behind the sheet? " & status)
```

```
End Sub
```
