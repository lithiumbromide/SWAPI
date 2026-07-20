---
title: "Place Note Behind Drawing Sheet Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Place_Note_Behind_Drawing_Sheet_Example_VBNET.htm"
---

# Place Note Behind Drawing Sheet Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swDrawing As DrawingDoc
        Dim swSelectionMgr As SelectionMgr
        Dim swNote As Note
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        ' Open drawing
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\api\2012-sm.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swDrawing = swModel

        ' Put drawing template and sheet in edit mode
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Sheet1", "SHEET", 0.0399580396732789, 0.20594194865811, 0, False, 0, Nothing, 0)
        swDrawing.EditTemplate()
        swDrawing.EditSheet2()

        swModel.ClearSelection2(True)

        ' Select note to place behind the sheet
        status = swModelDocExt.SelectByID2("DetailItem3@Sheet Format1", "NOTE", 0.155548914819136, 0.017885845974329, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swNote = swSelectionMgr.GetSelectedObject6(1, -1)
        swNote.BehindSheet = True
        Debug.Print("Was the selected note placed behind the sheet? " & status)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
